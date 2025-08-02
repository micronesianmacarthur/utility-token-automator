import logging
import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from mainwindow_ui import Ui_MainWindow
from service.validate import Validate
from service.browser_automator import BrowserAutomator
from service.log_handler import LogHandler
from service.setup_worker import SetupWorker
from static.constants import *


class MainWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.msg_box = None
        self.automator = None
        self.worker = None
        self.thread = None
        self.logger = None
        self.setupUi(self)
        self.set_logging()

        # clear message and token label
        self.lb_token.setText("")
        self.lb_message.setText("")

        # connect buttons
        self.pb_clear.clicked.connect(self.clear_input)
        self.pb_submit.clicked.connect(self.validate_input)

    def handle_error(self, message):
        self.logger.error(message)
        self.statusbar.showMessage(message, 5000)

    def set_logging(self):
        self.logger = logging.getLogger("INFO Logger")
        self.logger.setLevel(logging.INFO)
        # custom handler
        handler = LogHandler(self.statusbar)
        handler.setLevel(logging.INFO)
        self.logger.addHandler(handler)

    def validate_input(self):
        meter_input = self.le_meterNo
        amount_input = self.le_amount
        msg_display = self.lb_message

        msg_display.clear()
        meter_number = meter_input.text()
        amount_str = amount_input.text()

        # validations
        validate = Validate()

        valid, msg = validate.meter_num(meter_number)
        if not valid:
            msg_display.setText(msg)
            meter_input.setFocus()
            meter_input.selectAll()

            return

        valid, amount, msg = validate.amount(amount_str)
        if not valid:
            msg_display.setText(msg)
            amount_input.setFocus()
            amount_input.selectAll()
            return

        valid, msg = validate.cc_details(CC_NAME, CC_NUMBER, CC_CODE, CC_EXP_MONTH, CC_EXP_YEAR)
        if not valid:
            msg_display.setText(msg)
            return

        self.start_purchase()

    def clear_input(self):
        self.le_meterNo.clear()
        self.le_amount.clear()
        self.lb_message.clear()
        self.statusbar.showMessage("Input cleared", timeout=5000)

    def start_purchase(self):
        self.thread = qtc.QThread()
        self.worker = SetupWorker(url=URL, logger=self.logger)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.setup_complete)
        self.worker.error.connect(self.handle_error)

        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()

    def setup_complete(self, automator):
        self.automator = automator
        self.statusbar.clearMessage()
        self.logger.info("WebDriver Setup Complete")

        meter_number = self.le_meterNo.text()
        amount_str = self.le_amount.text()
        msg_display = self.lb_message

        # Entering payment details
        self.statusbar.showMessage("Entering payment details")
        if not self.automator.enter_payment_details(
            meter_number, CC_NUMBER, CC_NAME, CC_CODE, int(CC_EXP_MONTH), int(CC_EXP_YEAR)
        ):
            msg_display.setText("Error entering payment details")
            self.automator.close()
            return

        # click Next button
        if not self.automator.click_next_button():
            msg_display.setText("Error clicking next button")
            self.automator.close()
            return

        # check for invalid meter number message
        self.logger.info("Checking meter number")
        invalid_meter = self.automator.check_meter_message()
        if invalid_meter:
            self.statusbar.clearMessage()
            msg_display.setText(invalid_meter)
            self.automator.close()
            return

        # Enter payment amount
        amount = float(amount_str)
        self.logger.info("Entering payment amount")
        if not self.automator.enter_purchase_amount(amount):
            msg_display.setText("Unable to continue with payment. Check meter number.")
            self.automator.close()
            return

        # get customer name and display at successful payment
        customer_name = self.automator.get_customer_name()
        # self.lb_token.setText(f"Customer Name: {customer_name}")

        # click Next button
        if not self.automator.click_next_button():
            msg_display.setText("Error clicking next button")
            self.automator.close()
            return

        # Confirm Payment Popup
        status, submit = self.automator.load_payment_popup()
        if not status:
            self.logger.error("Error with payment confirmation popup")
            return

        # confirm meter and amount
        self.msg_box = qtw.QMessageBox()
        self.msg_box.setTextFormat(qtc.Qt.RichText)
        self.msg_box.setWindowTitle("Confirm Details")
        self.msg_box.setIcon(qtw.QMessageBox.Question)
        self.msg_box.setText(
            f'Please confirm details are correct:<br><br>Customer Name: <span style="font-weight:bold;color:#1E90FF;"'
            f'>{customer_name}</span><br>Meter No.: <span style="font-weight:bold;color:#1E90FF;">{meter_number}</span>'
            f'<br>Amount: <span style="font-weight:bold;color:#1E90FF;">${amount:.2f}</span>')
        self.msg_box.setStandardButtons(qtw.QMessageBox.Yes | qtw.QMessageBox.Abort)
        response = self.msg_box.exec()

        if response == qtw.QMessageBox.Abort:
            msg_display.setText("Payment aborted.")
            self.automator.close()
            return

        if not self.automator.confirm_payment(submit):
            msg_display.setText("Payment submission failed.")
            # self.automator.close()
            return

        payment_status, msg = self.automator.get_token_or_error()

        # =========== Message display formatting ===========
        stat_color = "rgb(34, 139, 34)" # default to 'Success' color --> ForestGreen
        # ================= End ============================

        if not payment_status:
            stat_color = "rgb(255, 62, 65)"
            self.statusbar.clearMessage()
            self.statusbar.showMessage(msg)
            self.lb_token.setText(
                f"<span style=\"color:{stat_color};font-weight:bold;font-size:18px;\">Payment Failed!!!</span><br><br>"
                f"<span>Customer Name:</span> <span style=\"font-weight:bold;\">{customer_name}</span><br><span>"
                f"Meter No.:</span> <span style=\"font-weight:bold;\">{meter_number}</span>"
                f"<br><br><span style=\"font-weight:bold;color:{stat_color};font-size:18px;\">*** {msg} ***</span>"
                f"<br>")
            self.automator.close()
            return

        if payment_status:
            self.lb_token.setText(
                f"<span style=\"color:{stat_color};font-weight:bold;font-size:18px;\">Payment Successful!!!</span><br><br>"
                f"<span>Customer Name:</span> <span style=\"font-weight:bold;\">{customer_name}</span><br><span>"
                f"Meter No.:</span> <span style=\"font-weight:bold;\">{meter_number}</span>"
                f"<br><br><span style=\"font-weight:bold;color:{stat_color};font-size:18px;\">*** {msg} ***</span>"
                f"<br>")

        self.lb_message.setText("Process completed")
        self.automator.close()
        return



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())