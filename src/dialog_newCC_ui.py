# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_newCC.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_dialog_newCC(object):
    def setupUi(self, dialog_newCC):
        if not dialog_newCC.objectName():
            dialog_newCC.setObjectName(u"dialog_newCC")
        dialog_newCC.setWindowModality(Qt.WindowModality.ApplicationModal)
        dialog_newCC.resize(380, 450)
        font = QFont()
        font.setFamilies([u"Lexend"])
        dialog_newCC.setFont(font)
        dialog_newCC.setStyleSheet(u"background-color: rgb(18, 26, 39);\n"
"font-family: 'Lexend';\n"
"font-size: 14px;")
        self.verticalLayout = QVBoxLayout(dialog_newCC)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lb_newCardTitle = QLabel(dialog_newCC)
        self.lb_newCardTitle.setObjectName(u"lb_newCardTitle")
        self.lb_newCardTitle.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setFamilies([u"Lexend"])
        font1.setBold(True)
        self.lb_newCardTitle.setFont(font1)
        self.lb_newCardTitle.setStyleSheet(u"font-size: 16px;\n"
"font-weight: bold;")

        self.verticalLayout.addWidget(self.lb_newCardTitle)

        self.widget = QWidget(dialog_newCC)
        self.widget.setObjectName(u"widget")
        self.widget.setFont(font)
        self.widget.setStyleSheet(u"background-color: #23334c;")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.le_ccName = QLineEdit(self.widget)
        self.le_ccName.setObjectName(u"le_ccName")
        self.le_ccName.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.le_ccName, 2, 0, 1, 3)

        self.lbl_nickname = QLabel(self.widget)
        self.lbl_nickname.setObjectName(u"lbl_nickname")
        self.lbl_nickname.setMaximumSize(QSize(120, 35))

        self.gridLayout.addWidget(self.lbl_nickname, 0, 0, 1, 1)

        self.cb_expMonth = QComboBox(self.widget)
        self.cb_expMonth.setObjectName(u"cb_expMonth")
        self.cb_expMonth.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.cb_expMonth, 4, 0, 1, 2)

        self.le_nickname = QLineEdit(self.widget)
        self.le_nickname.setObjectName(u"le_nickname")
        self.le_nickname.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.le_nickname, 0, 1, 1, 2)

        self.le_ccNumber = QLineEdit(self.widget)
        self.le_ccNumber.setObjectName(u"le_ccNumber")
        self.le_ccNumber.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.le_ccNumber, 1, 0, 1, 3)

        self.le_ccCode = QLineEdit(self.widget)
        self.le_ccCode.setObjectName(u"le_ccCode")
        self.le_ccCode.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.le_ccCode, 3, 0, 1, 3)

        self.cb_expYear = QComboBox(self.widget)
        self.cb_expYear.setObjectName(u"cb_expYear")
        self.cb_expYear.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.cb_expYear, 4, 2, 1, 1)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(dialog_newCC)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 50))
        self.widget_2.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 5, 0, 5)
        self.pb_ccSave = QPushButton(self.widget_2)
        self.pb_ccSave.setObjectName(u"pb_ccSave")
        self.pb_ccSave.setMaximumSize(QSize(16777215, 35))
        self.pb_ccSave.setStyleSheet(u"background-color: rgb(0, 85, 255);\n"
"font-weight: bold;")

        self.horizontalLayout.addWidget(self.pb_ccSave)

        self.pb_ccClose = QPushButton(self.widget_2)
        self.pb_ccClose.setObjectName(u"pb_ccClose")
        self.pb_ccClose.setMaximumSize(QSize(16777215, 35))
        self.pb_ccClose.setStyleSheet(u"background-color: rgb(255, 62, 65);\n"
"font-weight: bold;")

        self.horizontalLayout.addWidget(self.pb_ccClose)


        self.verticalLayout.addWidget(self.widget_2)

        self.lb_ccMessage = QLabel(dialog_newCC)
        self.lb_ccMessage.setObjectName(u"lb_ccMessage")
        self.lb_ccMessage.setMaximumSize(QSize(16777215, 25))
        self.lb_ccMessage.setStyleSheet(u"font-size: 11px;")

        self.verticalLayout.addWidget(self.lb_ccMessage)

#if QT_CONFIG(shortcut)
        self.lb_newCardTitle.setBuddy(self.le_nickname)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.le_nickname, self.le_ccNumber)
        QWidget.setTabOrder(self.le_ccNumber, self.le_ccName)
        QWidget.setTabOrder(self.le_ccName, self.le_ccCode)
        QWidget.setTabOrder(self.le_ccCode, self.cb_expMonth)
        QWidget.setTabOrder(self.cb_expMonth, self.cb_expYear)
        QWidget.setTabOrder(self.cb_expYear, self.pb_ccSave)
        QWidget.setTabOrder(self.pb_ccSave, self.pb_ccClose)

        self.retranslateUi(dialog_newCC)

        QMetaObject.connectSlotsByName(dialog_newCC)
    # setupUi

    def retranslateUi(self, dialog_newCC):
        dialog_newCC.setWindowTitle(QCoreApplication.translate("dialog_newCC", u"Dialog", None))
        self.lb_newCardTitle.setText(QCoreApplication.translate("dialog_newCC", u"Add New Credit/Debit Card", None))
        self.le_ccName.setPlaceholderText(QCoreApplication.translate("dialog_newCC", u"Enter Cardholder name", None))
        self.lbl_nickname.setText(QCoreApplication.translate("dialog_newCC", u"Card Nickname:", None))
        self.cb_expMonth.setPlaceholderText(QCoreApplication.translate("dialog_newCC", u"Select Expiry Month", None))
        self.le_nickname.setPlaceholderText(QCoreApplication.translate("dialog_newCC", u"Set card nickname", None))
        self.le_ccNumber.setPlaceholderText(QCoreApplication.translate("dialog_newCC", u"Enter Card number", None))
        self.le_ccCode.setPlaceholderText(QCoreApplication.translate("dialog_newCC", u"Enter CVC", None))
        self.cb_expYear.setPlaceholderText(QCoreApplication.translate("dialog_newCC", u"Year", None))
        self.pb_ccSave.setText(QCoreApplication.translate("dialog_newCC", u"Save", None))
        self.pb_ccClose.setText(QCoreApplication.translate("dialog_newCC", u"Close", None))
        self.lb_ccMessage.setText(QCoreApplication.translate("dialog_newCC", u"abcdefghijklmnopqrstuvwxyz0123456789", None))
    # retranslateUi

