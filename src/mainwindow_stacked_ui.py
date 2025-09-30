# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow_stacked.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import app_icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QSize(600, 600))
        MainWindow.setMaximumSize(QSize(600, 600))
        font = QFont()
        font.setFamilies([u"Spline Sans Mono"])
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/main/receipt-share.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"margin: 0px;\n"
"background-color: rgb(18, 26, 39);\n"
"padding: 0px;")
        self.actionPurchase_History = QAction(MainWindow)
        self.actionPurchase_History.setObjectName(u"actionPurchase_History")
        self.actionWallet = QAction(MainWindow)
        self.actionWallet.setObjectName(u"actionWallet")
        self.actionConsumers = QAction(MainWindow)
        self.actionConsumers.setObjectName(u"actionConsumers")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"margin: 0px;\n"
"padding: 0px;")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font1 = QFont()
        font1.setFamilies([u"Lexend"])
        font1.setPointSize(12)
        self.stackedWidget.setFont(font1)
        self.stackedWidget.setStyleSheet(u"margin-top: 0;\n"
"padding: 0px;")
        self.stack_main = QWidget()
        self.stack_main.setObjectName(u"stack_main")
        self.stack_main.setStyleSheet(u"margin-top: 0;")
        self.verticalLayout = QVBoxLayout(self.stack_main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.stack_main)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 100))
        font2 = QFont()
        font2.setFamilies([u"JetBrains Mono"])
        font2.setPointSize(12)
        self.widget.setFont(font2)
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pb_searchMeter = QPushButton(self.widget)
        self.pb_searchMeter.setObjectName(u"pb_searchMeter")
        self.pb_searchMeter.setMinimumSize(QSize(150, 30))
        font3 = QFont()
        font3.setFamilies([u"Lexend"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.pb_searchMeter.setFont(font3)
        self.pb_searchMeter.setStyleSheet(u"font-weight: bold;\n"
"background-color: rgb(0, 122, 33);")

        self.gridLayout_3.addWidget(self.pb_searchMeter, 0, 1, 1, 1)

        self.le_meterNo = QLineEdit(self.widget)
        self.le_meterNo.setObjectName(u"le_meterNo")
        self.le_meterNo.setMinimumSize(QSize(300, 30))
        font4 = QFont()
        font4.setFamilies([u"Lexend"])
        font4.setPointSize(14)
        self.le_meterNo.setFont(font4)

        self.gridLayout_3.addWidget(self.le_meterNo, 0, 0, 1, 1)

        self.cb_payment = QComboBox(self.widget)
        self.cb_payment.setObjectName(u"cb_payment")
        self.cb_payment.setMinimumSize(QSize(0, 30))
        self.cb_payment.setFont(font4)

        self.gridLayout_3.addWidget(self.cb_payment, 3, 0, 1, 2)

        self.le_amount = QLineEdit(self.widget)
        self.le_amount.setObjectName(u"le_amount")
        self.le_amount.setMinimumSize(QSize(0, 30))
        self.le_amount.setFont(font4)

        self.gridLayout_3.addWidget(self.le_amount, 2, 0, 1, 2)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.stack_main)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pb_submit = QPushButton(self.widget_2)
        self.pb_submit.setObjectName(u"pb_submit")
        self.pb_submit.setMinimumSize(QSize(0, 35))
        self.pb_submit.setFont(font3)
        self.pb_submit.setStyleSheet(u"font-weight: bold;\n"
"background-color: rgb(0, 85, 255);")

        self.horizontalLayout.addWidget(self.pb_submit)

        self.pb_clear = QPushButton(self.widget_2)
        self.pb_clear.setObjectName(u"pb_clear")
        self.pb_clear.setMinimumSize(QSize(0, 35))
        self.pb_clear.setFont(font3)
        self.pb_clear.setStyleSheet(u"font-weight: bold;\n"
"background-color: rgb(255, 62, 65);")

        self.horizontalLayout.addWidget(self.pb_clear)


        self.verticalLayout.addWidget(self.widget_2)

        self.frame = QFrame(self.stack_main)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(35, 51, 76);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lb_token = QLabel(self.frame)
        self.lb_token.setObjectName(u"lb_token")
        self.lb_token.setFont(font4)
        self.lb_token.setStyleSheet(u"\n"
"background-color: rgb(35, 51, 76);")
        self.lb_token.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_2.addWidget(self.lb_token, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.lb_message = QLabel(self.stack_main)
        self.lb_message.setObjectName(u"lb_message")
        self.lb_message.setMaximumSize(QSize(16777215, 40))
        font5 = QFont()
        font5.setFamilies([u"Lexend"])
        font5.setPointSize(11)
        self.lb_message.setFont(font5)

        self.verticalLayout.addWidget(self.lb_message)

        self.stackedWidget.addWidget(self.stack_main)
        self.stack_consumer = QWidget()
        self.stack_consumer.setObjectName(u"stack_consumer")
        self.verticalLayout_2 = QVBoxLayout(self.stack_consumer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lb_cvTitle = QLabel(self.stack_consumer)
        self.lb_cvTitle.setObjectName(u"lb_cvTitle")
        font6 = QFont()
        font6.setFamilies([u"Lexend"])
        font6.setPointSize(16)
        font6.setBold(True)
        self.lb_cvTitle.setFont(font6)

        self.verticalLayout_2.addWidget(self.lb_cvTitle)

        self.widget_3 = QWidget(self.stack_consumer)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.le_searchMeter = QLineEdit(self.widget_3)
        self.le_searchMeter.setObjectName(u"le_searchMeter")
        self.le_searchMeter.setMinimumSize(QSize(0, 35))
        self.le_searchMeter.setMaximumSize(QSize(400, 16777215))
        self.le_searchMeter.setFont(font4)

        self.horizontalLayout_3.addWidget(self.le_searchMeter)

        self.pb_filter = QPushButton(self.widget_3)
        self.pb_filter.setObjectName(u"pb_filter")
        self.pb_filter.setMinimumSize(QSize(0, 35))
        self.pb_filter.setFont(font3)
        self.pb_filter.setStyleSheet(u"font-weight: bold;\n"
"background-color: rgb(0, 122, 33);")

        self.horizontalLayout_3.addWidget(self.pb_filter)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.tbl_consumer = QTableWidget(self.stack_consumer)
        self.tbl_consumer.setObjectName(u"tbl_consumer")
        self.tbl_consumer.setFont(font4)
        self.tbl_consumer.setStyleSheet(u"background-color: #23334c;")

        self.verticalLayout_2.addWidget(self.tbl_consumer)

        self.widget_4 = QWidget(self.stack_consumer)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pb_select = QPushButton(self.widget_4)
        self.pb_select.setObjectName(u"pb_select")
        self.pb_select.setMinimumSize(QSize(0, 35))
        self.pb_select.setFont(font3)
        self.pb_select.setStyleSheet(u"background-color: rgb(0, 85, 255);\n"
"font-weight: bold;")

        self.horizontalLayout_2.addWidget(self.pb_select)

        self.pb_cvClose = QPushButton(self.widget_4)
        self.pb_cvClose.setObjectName(u"pb_cvClose")
        self.pb_cvClose.setMinimumSize(QSize(0, 35))
        self.pb_cvClose.setFont(font3)
        self.pb_cvClose.setStyleSheet(u"font-weight: bold;\n"
"background-color: #ff3e41;")

        self.horizontalLayout_2.addWidget(self.pb_cvClose)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.lb_cvMessage = QLabel(self.stack_consumer)
        self.lb_cvMessage.setObjectName(u"lb_cvMessage")
        self.lb_cvMessage.setFont(font5)

        self.verticalLayout_2.addWidget(self.lb_cvMessage)

        self.stackedWidget.addWidget(self.stack_consumer)
        self.stack_wallet = QWidget()
        self.stack_wallet.setObjectName(u"stack_wallet")
        self.verticalLayout_3 = QVBoxLayout(self.stack_wallet)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lb_wTitle = QLabel(self.stack_wallet)
        self.lb_wTitle.setObjectName(u"lb_wTitle")
        self.lb_wTitle.setFont(font6)

        self.verticalLayout_3.addWidget(self.lb_wTitle)

        self.widget_5 = QWidget(self.stack_wallet)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pb_newCard = QPushButton(self.widget_5)
        self.pb_newCard.setObjectName(u"pb_newCard")
        self.pb_newCard.setMinimumSize(QSize(0, 35))
        self.pb_newCard.setFont(font3)
        self.pb_newCard.setStyleSheet(u"background-color: #0055ff;")

        self.horizontalLayout_4.addWidget(self.pb_newCard)

        self.pb_manage = QPushButton(self.widget_5)
        self.pb_manage.setObjectName(u"pb_manage")
        self.pb_manage.setMinimumSize(QSize(0, 35))
        self.pb_manage.setFont(font3)
        self.pb_manage.setStyleSheet(u"background-color: #0055ff;")

        self.horizontalLayout_4.addWidget(self.pb_manage)


        self.verticalLayout_3.addWidget(self.widget_5)

        self.lw_walletView = QListWidget(self.stack_wallet)
        self.lw_walletView.setObjectName(u"lw_walletView")
        self.lw_walletView.setFont(font4)
        self.lw_walletView.setStyleSheet(u"background-color:#23334c;")

        self.verticalLayout_3.addWidget(self.lw_walletView)

        self.widget_6 = QWidget(self.stack_wallet)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, -1, 0, 0)
        self.horizontalSpacer = QSpacerItem(405, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.pb_wClose = QPushButton(self.widget_6)
        self.pb_wClose.setObjectName(u"pb_wClose")
        self.pb_wClose.setMinimumSize(QSize(150, 35))
        self.pb_wClose.setFont(font3)
        self.pb_wClose.setStyleSheet(u"background-color: rgb(255, 62, 65);")

        self.horizontalLayout_6.addWidget(self.pb_wClose)


        self.verticalLayout_3.addWidget(self.widget_6)

        self.stackedWidget.addWidget(self.stack_wallet)
        self.stack_purchaseHistory = QWidget()
        self.stack_purchaseHistory.setObjectName(u"stack_purchaseHistory")
        self.verticalLayout_4 = QVBoxLayout(self.stack_purchaseHistory)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lb_phTitle = QLabel(self.stack_purchaseHistory)
        self.lb_phTitle.setObjectName(u"lb_phTitle")
        self.lb_phTitle.setFont(font6)

        self.verticalLayout_4.addWidget(self.lb_phTitle)

        self.grp_search = QWidget(self.stack_purchaseHistory)
        self.grp_search.setObjectName(u"grp_search")
        self.grp_search.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.grp_search)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.le_phConsumer = QLineEdit(self.grp_search)
        self.le_phConsumer.setObjectName(u"le_phConsumer")
        self.le_phConsumer.setMinimumSize(QSize(0, 35))
        self.le_phConsumer.setFont(font4)

        self.horizontalLayout_5.addWidget(self.le_phConsumer)

        self.pb_phFilter = QPushButton(self.grp_search)
        self.pb_phFilter.setObjectName(u"pb_phFilter")
        self.pb_phFilter.setMinimumSize(QSize(120, 35))
        self.pb_phFilter.setFont(font3)
        self.pb_phFilter.setStyleSheet(u"background-color: rgb(0, 122, 33);")

        self.horizontalLayout_5.addWidget(self.pb_phFilter)


        self.verticalLayout_4.addWidget(self.grp_search)

        self.tbl_history = QTableWidget(self.stack_purchaseHistory)
        self.tbl_history.setObjectName(u"tbl_history")
        self.tbl_history.setStyleSheet(u"background-color: #23334c;")

        self.verticalLayout_4.addWidget(self.tbl_history)

        self.widget_7 = QWidget(self.stack_purchaseHistory)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, -1, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(405, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.pb_phClose = QPushButton(self.widget_7)
        self.pb_phClose.setObjectName(u"pb_phClose")
        self.pb_phClose.setMinimumSize(QSize(150, 35))
        self.pb_phClose.setFont(font3)
        self.pb_phClose.setStyleSheet(u"background-color: rgb(255, 62, 65);")

        self.horizontalLayout_7.addWidget(self.pb_phClose)


        self.verticalLayout_4.addWidget(self.widget_7)

        self.stackedWidget.addWidget(self.stack_purchaseHistory)

        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 33))
        self.menubar.setFont(font1)
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setFont(font5)
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionPurchase_History)
        self.menuFile.addAction(self.actionWallet)
        self.menuFile.addAction(self.actionConsumers)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Utility Token Payment Automator", None))
        self.actionPurchase_History.setText(QCoreApplication.translate("MainWindow", u"Purchase History", None))
        self.actionWallet.setText(QCoreApplication.translate("MainWindow", u"Wallet", None))
        self.actionConsumers.setText(QCoreApplication.translate("MainWindow", u"Consumers", None))
        self.pb_searchMeter.setText(QCoreApplication.translate("MainWindow", u"Search Meter", None))
        self.le_meterNo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter meter number", None))
        self.cb_payment.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select a payment method", None))
        self.le_amount.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter amount", None))
        self.pb_submit.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.pb_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.lb_token.setText(QCoreApplication.translate("MainWindow", u"abcdefghijklmnopqrstuvwxyz1234567890", None))
        self.lb_message.setText(QCoreApplication.translate("MainWindow", u"abcdefghijklmnopqrstuvwxyz1234567890", None))
        self.lb_cvTitle.setText(QCoreApplication.translate("MainWindow", u"Consumer Meter View", None))
        self.le_searchMeter.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filter by Name or Meter Number", None))
        self.pb_filter.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.pb_select.setText(QCoreApplication.translate("MainWindow", u"Select Meter", None))
        self.pb_cvClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.lb_cvMessage.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.lb_wTitle.setText(QCoreApplication.translate("MainWindow", u"Wallet", None))
        self.pb_newCard.setText(QCoreApplication.translate("MainWindow", u"New Card", None))
        self.pb_manage.setText(QCoreApplication.translate("MainWindow", u"Manage Cards", None))
        self.pb_wClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.lb_phTitle.setText(QCoreApplication.translate("MainWindow", u"Purchase History", None))
        self.le_phConsumer.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filter by Name or Meter Number", None))
        self.pb_phFilter.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.pb_phClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

