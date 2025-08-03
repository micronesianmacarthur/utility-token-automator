# src/service/purchase_worker.py

from PySide6.QtCore import QObject, Signal
from .browser_automator_optimized import BrowserAutomator
from .locators import FirstPageLocators, SecondPageLocators, ConfirmationPopupLocators, ResultPageLocators


class PurchaseWorker(QObject):
    """
    QObject worker to handle the entire purchase process in a background thread.
    This keeps the UI responsive and separates workflow logic from the UI.
    """
    success = Signal(dict)
    failure = Signal(str)

    def __init__(self, automator: BrowserAutomator, details: dict):
        super().__init__()
        self.automator = automator
        self.details = details

    def run(self):
        """Executes the full purchase workflow."""
        try:
            # Step 1: Enter payment details on the first page
            self.automator.logger.info("Entering payment details.")
            cc = self.details['cc']
            self.automator.send_keys_to_element(FirstPageLocators.METER_INPUT, self.details['meter'])
            self.automator.send_keys_to_element(FirstPageLocators.CC_NUMBER_INPUT, cc['CC_NUMBER'])
            self.automator.send_keys_to_element(FirstPageLocators.CC_NAME_INPUT, cc['CC_NAME'])
            self.automator.send_keys_to_element(FirstPageLocators.CC_CODE_INPUT, cc['CC_CODE'])
            self.automator.select_expiry_date(cc['CC_EXP_MONTH'], cc['CC_EXP_YEAR'])

            self.automator.click_element(FirstPageLocators.NEXT_BUTTON)

            # Step 2: Check for meter error, then enter amount
            error_msg = self.automator.find_optional_element_text(FirstPageLocators.METER_ERROR_LABEL)
            if error_msg:
                raise RuntimeError(f"Invalid Meter: {error_msg}")

            self.automator.logger.info("Entering purchase amount.")
            first_name = self.automator.get_element_text(SecondPageLocators.CUSTOMER_NAME_FIRST).split("(")[0]
            last_name = self.automator.get_element_text(SecondPageLocators.CUSTOMER_NAME_LAST)
            customer_name = f"{first_name} {last_name}"

            self.automator.click_element(SecondPageLocators.OTHER_AMOUNT_RADIO)
            self.automator.send_keys_to_element(SecondPageLocators.AMOUNT_INPUT, str(self.details['amount']))

            self.automator.click_element(SecondPageLocators.NEXT_BUTTON)

            # Step 3: Confirm payment in popup
            self.automator.wait_for_element(ConfirmationPopupLocators.SUBMIT_BUTTON)
            # The confirmation dialog is in the main thread, so we just wait here.
            # The main thread will call confirm_payment() on this worker.

            # The rest of the process is in confirm_payment
            self.details['customer_name'] = customer_name

        except Exception as e:
            self.automator.logger.error(f"Purchase failed during process: {e}", exc_info=True)
            self.failure.emit(str(e))

    def confirm_payment(self):
        """Continues the process after user confirmation."""
        try:
            self.automator.click_element(ConfirmationPopupLocators.SUBMIT_BUTTON)
            self.automator.logger.info("Payment submitted. Waiting for result...")

            # Step 4: Get final token or error message
            self.automator.wait.until(
                lambda driver: driver.find_elements(*ResultPageLocators.TOKEN_LABEL) or \
                               driver.find_elements(*ResultPageLocators.ERROR_TITLE)
            )

            token = self.automator.find_optional_element_text(ResultPageLocators.TOKEN_LABEL)
            if token:
                self.automator.logger.info("Payment successful.")
                result = self.details.copy()
                result['token'] = token
                self.success.emit(result)
                return

            error_title = self.automator.find_optional_element_text(ResultPageLocators.ERROR_TITLE)
            if error_title and "Error Message" in error_title:
                error_detail = self.automator.find_optional_element_text(ResultPageLocators.ERROR_DETAIL_XPATH)
                final_error = error_detail or "Unknown payment error."
                self.automator.logger.warning(f"Payment failed: {final_error}")
                self.failure.emit(final_error)
            else:
                self.failure.emit("Unknown outcome: Neither token nor error found.")

        except Exception as e:
            self.automator.logger.error(f"Purchase failed during confirmation: {e}", exc_info=True)
            self.failure.emit(str(e))