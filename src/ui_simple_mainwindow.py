# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simple_mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)
import app_icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 400)
        MainWindow.setMinimumSize(QSize(500, 400))
        icon = QIcon()
        icon.addFile(u":/main/receipt-share.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 0, 12, 12)
        self.le_meterNo = QLineEdit(self.widget)
        self.le_meterNo.setObjectName(u"le_meterNo")
        self.le_meterNo.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamilies([u"JetBrains Mono"])
        font.setPointSize(14)
        self.le_meterNo.setFont(font)
        self.le_meterNo.setFrame(False)
        self.le_meterNo.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.le_meterNo)

        self.le_amount = QLineEdit(self.widget)
        self.le_amount.setObjectName(u"le_amount")
        self.le_amount.setMinimumSize(QSize(0, 30))
        self.le_amount.setFont(font)
        self.le_amount.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.le_amount.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.le_amount)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 12, 0, 12)
        self.pb_submit = QPushButton(self.widget_3)
        self.pb_submit.setObjectName(u"pb_submit")
        self.pb_submit.setMinimumSize(QSize(0, 35))
        self.pb_submit.setFont(font)
        self.pb_submit.setStyleSheet(u"background-color: rgb(11, 121, 255);")

        self.horizontalLayout.addWidget(self.pb_submit)

        self.pb_clear = QPushButton(self.widget_3)
        self.pb_clear.setObjectName(u"pb_clear")
        self.pb_clear.setMinimumSize(QSize(0, 35))
        self.pb_clear.setFont(font)
        self.pb_clear.setStyleSheet(u"background-color: rgb(255, 62, 65);")

        self.horizontalLayout.addWidget(self.pb_clear)


        self.verticalLayout.addWidget(self.widget_3)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(12, 5, 12, 12)
        self.frame = QFrame(self.widget_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lb_token = QLabel(self.frame)
        self.lb_token.setObjectName(u"lb_token")
        self.lb_token.setFont(font)
        self.lb_token.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.lb_token.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout.addWidget(self.lb_token, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame)

        self.lb_message = QLabel(self.widget_2)
        self.lb_message.setObjectName(u"lb_message")
        self.lb_message.setMinimumSize(QSize(0, 0))
        self.lb_message.setMaximumSize(QSize(16777215, 18))
        font1 = QFont()
        font1.setFamilies([u"JetBrains Mono"])
        font1.setPointSize(10)
        self.lb_message.setFont(font1)

        self.verticalLayout_2.addWidget(self.lb_message)


        self.gridLayout_2.addWidget(self.widget_2, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QRect(0, 0, 500, 33))
        self.menuExit = QMenu(self.menubar)
        self.menuExit.setObjectName(u"menuExit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setFont(font1)
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuExit.menuAction())
        self.menuExit.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Utility Token Automator", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.le_meterNo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Meter Number", None))
        self.le_amount.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Amount $", None))
        self.pb_submit.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.pb_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.lb_token.setText(QCoreApplication.translate("MainWindow", u"abcdefghijklmnopqrstuvwxyz 0123456789", None))
        self.lb_message.setText(QCoreApplication.translate("MainWindow", u"abcdefghijklmnopqrstuvwxyz 0123456789", None))
        self.menuExit.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

