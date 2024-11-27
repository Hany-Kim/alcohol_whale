# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(430, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Questions = QLabel(self.centralwidget)
        self.Questions.setObjectName(u"Questions")
        self.Questions.setGeometry(QRect(0, 40, 431, 71))
        self.Questions.setTextFormat(Qt.AutoText)
        self.Questions.setAlignment(Qt.AlignCenter)
        self.Next = QPushButton(self.centralwidget)
        self.Next.setObjectName(u"Next")
        self.Next.setGeometry(QRect(330, 510, 75, 24))
        self.Back = QPushButton(self.centralwidget)
        self.Back.setObjectName(u"Back")
        self.Back.setGeometry(QRect(20, 510, 75, 24))
        self.BTN1 = QCheckBox(self.centralwidget)
        self.BTN1.setObjectName(u"BTN1")
        self.BTN1.setGeometry(QRect(50, 150, 271, 20))
        self.BTN2 = QCheckBox(self.centralwidget)
        self.BTN2.setObjectName(u"BTN2")
        self.BTN2.setGeometry(QRect(230, 150, 181, 20))
        self.BTN3 = QCheckBox(self.centralwidget)
        self.BTN3.setObjectName(u"BTN3")
        self.BTN3.setGeometry(QRect(50, 230, 361, 20))
        self.BTN4 = QCheckBox(self.centralwidget)
        self.BTN4.setObjectName(u"BTN4")
        self.BTN4.setGeometry(QRect(230, 230, 161, 20))
        self.BTN5 = QCheckBox(self.centralwidget)
        self.BTN5.setObjectName(u"BTN5")
        self.BTN5.setGeometry(QRect(50, 300, 341, 20))
        self.BTN6 = QCheckBox(self.centralwidget)
        self.BTN6.setObjectName(u"BTN6")
        self.BTN6.setGeometry(QRect(230, 300, 181, 20))
        self.BTN7 = QCheckBox(self.centralwidget)
        self.BTN7.setObjectName(u"BTN7")
        self.BTN7.setGeometry(QRect(50, 380, 511, 20))
        self.BTN8 = QCheckBox(self.centralwidget)
        self.BTN8.setObjectName(u"BTN8")
        self.BTN8.setGeometry(QRect(230, 380, 171, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Back.clicked.connect(MainWindow.goBack)
        self.Next.clicked.connect(MainWindow.goNext)
        self.Questions.linkActivated.connect(MainWindow.showQs)
        self.BTN1.clicked.connect(MainWindow.addAns1)
        self.BTN5.clicked.connect(MainWindow.addAns5)
        self.BTN7.clicked.connect(MainWindow.addAns7)
        self.BTN2.clicked.connect(MainWindow.addAns2)
        self.BTN4.clicked.connect(MainWindow.addAns4)
        self.BTN6.clicked.connect(MainWindow.addAns6)
        self.BTN8.clicked.connect(MainWindow.addAns8)
        self.BTN3.clicked.connect(MainWindow.addAns3)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Questions.setText(QCoreApplication.translate("MainWindow", u"\uc9c8\ubb38", None))
        self.Next.setText(QCoreApplication.translate("MainWindow", u"\ub2e4\uc74c", None))
        self.Back.setText(QCoreApplication.translate("MainWindow", u"\uc774\uc804", None))
        self.BTN1.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.BTN2.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.BTN3.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.BTN4.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.BTN5.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.BTN6.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.BTN7.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.BTN8.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
    # retranslateUi

