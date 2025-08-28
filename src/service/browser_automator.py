import logging

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from .locators import FirstPageLocators, DatePickerLocators, SecondPageLocators, ResultPageLocators


class BrowserAutomator:
    """
    Class BrowserAutomator.
    Automates the process of purchasing power and water tokens using Selenium.
    """
    def __init__(self, url: str, headless: bool = False, logger = None, skip_setup=False): # headless to True for background processing
        self.url = url
        self.headless = headless
        self.driver = None
        self.wait = None
        self.logger = logger or logging.getLogger("INFO Logger")
        if not skip_setup:
            self.setup_driver()

    def setup_driver(self):
        """
        Sets up Chrome WebDriver by default.
        Falls back to Microsoft Edge WebDriver if Chrome is not available
        """
        log = self.logger
        log.info("Setting up Chrome WebDriver. Please be patient.")

        chrome_options = ChromeOptions()
        edge_options = EdgeOptions()

        if self.headless:
            for opts in [chrome_options, edge_options]:
                opts.add_argument("--headless")
                opts.add_argument("--disable-gpu")
                opts.add_argument("--no-sandbox")
                opts.add_argument("--disable-dev-shm-usage")

        try:
            service = ChromeService(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            self.wait = WebDriverWait(self.driver, 10)
            log.info("Chrome initiated")
        except Exception as chrome_error:
            chrome_msg = f"Chrome WebDriver failed: {chrome_error}"
            log.warning(chrome_msg)
            try:
                service = EdgeService(EdgeChromiumDriverManager().install())
                self.driver = webdriver.Edge(service=service, options=edge_options)
                self.wait = WebDriverWait(self.driver, 10)
                log.info("Edge initiated")
            except Exception as edge_error:
                edge_msg = f"Edge WebDriver failed: {edge_error}"
                log.critical(edge_msg)
                raise RuntimeError("WebDriver initiation failed") from edge_error

    def _setup_chrome(self):
        options = ChromeOptions()

        if self.headless:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

        try:
            service = ChromeService(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=options)
            self.wait = WebDriverWait(self.driver, 10)
            self.logger.info("Chrome initiated")
        except Exception as chrome_error:
            chrome_msg = f"Chrome WebDriver failed: {chrome_error}"
            self.logger.warning(chrome_msg)
            try:
                self._setup_edge()
            except Exception as edge_error:
                self.logger.critical(edge_error)
                raise RuntimeError("WebDriver initiation failed") from edge_error


    def _setup_edge(self):
        options = EdgeOptions()

        if self.headless:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

        service = EdgeService(EdgeChromiumDriverManager().install())
        self.driver = webdriver.Edge(service=service, options=options)
        self.wait = WebDriverWait(self.driver, 10)
        self.logger.info("Edge initiated")


    def close(self):
        """
        Closes the browser.
        """
        if self.driver:
            self.logger.info("Browser closed")
            self.driver.quit()
            self.driver = None
            self.wait = None

    def open_site(self):
        """
        Navigates the browser to the specified URL.
        """
        if not self.driver:
            self.logger.critical("WebDriver initiation failed")
            return False
        try:
            self.logger.info("Loading payment page. Please be patient.")
            self.driver.get(self.url)
            if not self.headless:
                self.driver.maximize_window()

            # wait for key element on the first page to ensure it's loaded correctly
            self.wait_for_element(FirstPageLocators.METER_INPUT)
            self.logger.info("Payment page loaded successfully")
            return True
        except Exception as e:
            self.logger.critical(f"Error: {e}")
            return None

    def wait_for_element(self, locator, timeout = 4):
        """Waits for element to be visible."""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def enter_payment_details(self, meter: str, cc_number: str, cc_name: str, cc_code: str,
                              exp_month: int, exp_year: int):
        """
        Enters the meter number and CC details on the first page
        :param meter: (str) The meter number for power or water
        :param cc_number: (str) The CC number
        :param cc_name: (str) The cardholder name
        :param cc_code: (str) The CC code or CVV
        :param exp_month: (int) The CC expiration month
        :param exp_year: (int) The CC expiration year
        :return: (bool)
        """
        self.logger.info("Initiating payment details.")
        try:
            # input meter
            self.send_keys_to_element(FirstPageLocators.METER_INPUT, meter)

            # input CC number
            self.send_keys_to_element(FirstPageLocators.CC_NUMBER_INPUT, cc_number)

            # input cc holder name
            self.send_keys_to_element(FirstPageLocators.CC_NAME_INPUT, cc_name)

            # input CC code
            self.send_keys_to_element(FirstPageLocators.CC_CODE_INPUT, cc_code)

            try:
                # handle expiry date
                self.click_element(FirstPageLocators.EXPIRY_POPUP_BUTTON)

                # month mapping for IDs
                month_ids = {
                    1: "rcMView_Jan", 2: "rcMView_Feb", 3: "rcMView_Mar", 4: "rcMView_Apr", 5: "rcMView_May",
                    6:"rcMView_Jun", 7: "rcMView_Jul", 8: "rcMView_Aug", 9: "rcMView_Sep", 10: "rcMView_Oct",
                    11: "rcMView_Nov", 12: "rcMView_Dec"
                }

                # select month
                target_month_id = month_ids.get(exp_month)
                if not target_month_id:
                    raise ValueError(f"Invalid month: {exp_month}. Must be between 1 and 12.")

                # find the <a> tag inside the <td> for the month
                month_locator = (By.XPATH, DatePickerLocators.MONTH_XPATH_TEMPLATE.format(month_str=target_month_id))
                self.click_element(month_locator)

            except Exception as e:
                self.logger.critical(f"Error with month picker: {e}")

            # select year
            # loop to navigate years until target year is visible
            while True:
                # get all visible year elements in the current view
                year_elements = self.driver.find_elements(By.XPATH, DatePickerLocators.VISIBLE_YEARS_XPATH)

                current_years = []
                for el in year_elements:
                    try:
                        year_val = int(el.text)
                        current_years.append(year_val)
                    except ValueError:
                        continue # skip elements that don't contain valid year numbers

                if not current_years:
                    break

                min_current_year = min(current_years)
                max_current_year = max(current_years)

                if min_current_year <= exp_year <= max_current_year:
                    break # exit loop when target year is visible

                if exp_year > max_current_year:
                    self.click_element(DatePickerLocators.NEXT_YEAR_BUTTON)

                    # wait for UI to update
                    self.wait_for_element(DatePickerLocators.NEXT_YEAR_BUTTON)
                else:
                    self.logger.error(f"Issue navigating year elements.")
                    break

            # click target year after loop
            year_locator = (By.XPATH, DatePickerLocators.YEAR_XPATH_TEMPLATE.format(year=exp_year))
            self.click_element(year_locator)

            # click OK button in date picker
            self.click_element(DatePickerLocators.OK_BUTTON)

            self.logger.info("All payment details entered successfully.")
            return True
        except Exception as e:
            self.logger.error(str(e))
            return False

    def click_element(self, locator):
        """Finds clickable element and clicks it."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys_to_element(self, locator, keys):
        """Finds element, clears it, and sends keys to it."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(keys)

    def click_next_button(self):
        """
        Clicks the 'Next' button on the current page.
        """
        try:
            self.click_element(FirstPageLocators.NEXT_BUTTON)
            logging.info("Clicked 'Next' button.")
            return True
        except Exception as e:
            logging.error(f"Error clicking 'Next' button: {e}")
            return False

    def check_meter_message(self):
        try:
            # find error message element with id
            error_element = self.wait.until(
                EC.visibility_of_element_located((
                    By.ID, "ContentPlaceHolder1_lblmeter"
                ))
            )
            # extract text
            error_msg = error_element.text.strip()
            return error_msg
        except TimeoutException as te:
            self.logger.error(f"Timeout error: {str(te)}")
            return None

    def get_element_text(self, locator) -> str:
        """Finds element and returns its text."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text.strip()

    def get_customer_name(self):
        try:
            # get parent element by xpath
            self.wait_for_element(SecondPageLocators.CUSTOMER_NAME_FIRST)

            # get first name row
            first_name = self.get_element_text(SecondPageLocators.CUSTOMER_NAME_FIRST)

            # get last name row
            last_name = self.get_element_text(SecondPageLocators.CUSTOMER_NAME_LAST)

            # combine name
            full_name = f"{first_name} {last_name}"
            return full_name
        except Exception:
            self.logger.error("Error getting customer name.")
            return None



    def enter_purchase_amount(self, amount: float):
        """
        Selects the 'Other' radio button and enters the specified purchase amount.

        Args:
            amount (float): The amount of token to purchase.
        """
        try:
            # Click the "Other" radio button
            self.click_element(SecondPageLocators.OTHER_AMOUNT_RADIO)

            # Wait for the amount input field to become visible and clickable
            self.send_keys_to_element(SecondPageLocators.AMOUNT_INPUT, amount)
            logging.info(f"Entered amount: {amount}")
            return True
        except Exception as e:
            logging.error(f"Error entering purchase amount: {e}")
            return False

    def load_payment_popup(self):
        """
        Waits for the payment confirmation modal dialog to appear and clicks the 'Submit' button.
        """
        try:
            # Wait for the modal dialog's submit button to be clickable
            submit_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_RadWindow1_C_rbtnSave_input")))
            return "ready", submit_button
        except Exception as e:
            self.logger.error(f"Unable to load payment popup: {e}")
            return None, None

    def confirm_payment(self, element):
        try:
            # User interaction for confirmation (can be removed for full automation)
            element.click()
            self.logger.info("Payment submitted.")
            return True
        except Exception as e:
            self.logger.error(f"Error confirming payment popup: {e}")
            return False

    def get_token_or_error(self):
        """
        Checks for the presence of the token or an error message on the final page.

        Returns:
            tuple: A tuple containing (success_status, message).
                   success_status is True if token found, False if error, None if neither.
                   message is the token string or the error message.
        """
        self.logger.info("Please be patient as we process the payment.")
        try:
            # Wait for either the token element or the error title to be present
            # Using EC.any_of for more precise waiting
            self.wait.until(
                EC.any_of(
                    EC.visibility_of_element_located(
                        ResultPageLocators.TOKEN_LABEL),
                    EC.visibility_of_element_located(ResultPageLocators.ERROR_TITLE)
                )
            )

            # Check for token first
            try:
                token_text = self.get_element_text(ResultPageLocators.TOKEN_LABEL)
                if token_text:
                    self.logger.info(f"Payment successful. Token received")
                    logging.info(f"Token found: {token_text}")
                    return True, token_text
            except:
                pass  # Token element not found, proceed to check for error

            # Check for error message
            try:
                error_title_text = self.get_element_text(ResultPageLocators.ERROR_TITLE)

                # If "Error Message" is in the title, look for the detailed error
                if "Error Message" in error_title_text:
                    # Look for the specific error detail div
                    error_detail_text = self.get_element_text((By.XPATH, ResultPageLocators.ERROR_DETAIL_XPATH))

                    self.logger.critical(f"Payment failed: {error_detail_text}")
                    logging.warning(f"Error detected: {error_detail_text}")
                    return False, error_detail_text
            except:
                pass  # Error elements not found

            logging.warning("Neither token nor a clear error message found.")
            return None, "Unknown outcome: Neither token nor explicit error found."

        except Exception as e:
            logging.error(f"An error occurred while checking for token/error: {e}")
            return None, f"Automation error during result check: {e}"
