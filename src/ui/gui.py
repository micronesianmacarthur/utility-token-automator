import sys
from datetime import datetime
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from src.dialog_newCC_ui import Ui_dialog_newCC
from src.service.validate import Validate
from src.static.constants import months
from src.service.log_handler import LogHandler


class NewCardDialog(qtw.QDialog, Ui_dialog_newCC):
    def __init__(self, parent=None):
        super(NewCardDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Add New CC')
        self.populate_exp_month()
        self.populate_exp_year()

        # clear message label
        self.lb_ccMessage.setText("")

        # connect button signals
        self.pb_ccSave.clicked.connect(self.save_cc)
        self.pb_ccClose.clicked.connect(self.close)

    def save_cc(self):
        nickname = self.le_nickname.text()
        cc_number = self.le_ccNumber.text()
        cc_name = self.le_ccName.text()
        cc_code = self.le_ccCode.text()
        # get value from expMonth and year

        # validate cc_number
        if Validate.luhn_validation(cc_number):
            print(Validate.luhn_validation(cc_number))

    def populate_exp_month(self):
        for month in months:
            self.cb_expMonth.addItem(months[month], userData=month)

    def populate_exp_year(self):
        current_year = datetime.today().year
        year_range = []

        max_year = current_year + 10
        min_year = current_year - 10

        while min_year <= max_year:
            year_range.append(min_year)
            min_year += 1

        for year in year_range:
            self.cb_expYear.addItem(str(year), userData=year)





