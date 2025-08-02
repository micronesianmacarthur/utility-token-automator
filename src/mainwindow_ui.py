# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)
import app_icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(500, 500))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        font.setBold(True)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/main/receipt-share.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout = QVBoxLayout(self.widget_5)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.lb_meterNo = QLabel(self.widget_5)
        self.lb_meterNo.setObjectName(u"lb_meterNo")

        self.verticalLayout.addWidget(self.lb_meterNo)

        self.lb_amount = QLabel(self.widget_5)
        self.lb_amount.setObjectName(u"lb_amount")

        self.verticalLayout.addWidget(self.lb_amount)


        self.horizontalLayout.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_2 = QVBoxLayout(self.widget_6)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.le_meterNo = QLineEdit(self.widget_6)
        self.le_meterNo.setObjectName(u"le_meterNo")
        self.le_meterNo.setMinimumSize(QSize(0, 35))

        self.verticalLayout_2.addWidget(self.le_meterNo)

        self.le_amount = QLineEdit(self.widget_6)
        self.le_amount.setObjectName(u"le_amount")
        self.le_amount.setMinimumSize(QSize(0, 35))

        self.verticalLayout_2.addWidget(self.le_amount)


        self.horizontalLayout.addWidget(self.widget_6)


        self.verticalLayout_3.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.pb_submit = QPushButton(self.widget_4)
        self.pb_submit.setObjectName(u"pb_submit")
        self.pb_submit.setMinimumSize(QSize(0, 35))
        self.pb_submit.setStyleSheet(u"background-color: rgb(0, 170, 255);")

        self.horizontalLayout_2.addWidget(self.pb_submit)

        self.pb_clear = QPushButton(self.widget_4)
        self.pb_clear.setObjectName(u"pb_clear")
        self.pb_clear.setMinimumSize(QSize(0, 35))
        self.pb_clear.setFont(font)
        self.pb_clear.setStyleSheet(u"background-color: rgb(255, 62, 65);")

        self.horizontalLayout_2.addWidget(self.pb_clear)


        self.verticalLayout_3.addWidget(self.widget_4)


        self.verticalLayout_5.addWidget(self.widget)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.frame = QFrame(self.widget_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(2, 2, -1, 2)
        self.lb_token = QLabel(self.frame)
        self.lb_token.setObjectName(u"lb_token")
        font1 = QFont()
        font1.setFamilies([u"IBM Plex Mono"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.lb_token.setFont(font1)
        self.lb_token.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.lb_token.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout.addWidget(self.lb_token, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.frame)

        self.widget_7 = QWidget(self.widget_2)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMaximumSize(QSize(16777215, 35))
        self.gridLayout_2 = QGridLayout(self.widget_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(1)
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.lb_message = QLabel(self.widget_7)
        self.lb_message.setObjectName(u"lb_message")
        self.lb_message.setMaximumSize(QSize(16777215, 35))
        font2 = QFont()
        font2.setFamilies([u"JetBrains Mono"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.lb_message.setFont(font2)
        self.lb_message.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_message, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.widget_7)


        self.verticalLayout_5.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setEnabled(False)
        self.menubar.setGeometry(QRect(0, 0, 500, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(9)
        font3.setBold(False)
        self.statusbar.setFont(font3)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Utility Token Automator", None))
        self.lb_meterNo.setText(QCoreApplication.translate("MainWindow", u"Meter No.:", None))
        self.lb_amount.setText(QCoreApplication.translate("MainWindow", u"Amount $:", None))
        self.pb_submit.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.pb_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.lb_token.setText(QCoreApplication.translate("MainWindow", u"token", None))
        self.lb_message.setText(QCoreApplication.translate("MainWindow", u"message", None))
    # retranslateUi

