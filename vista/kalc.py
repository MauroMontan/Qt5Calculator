# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(421, 435)
        MainWindow.setStyleSheet(u"*{\n"
"background:rgb(170, 85, 255);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"*{\n"
"border-radius:16;\n"
"\n"
"background:white;\n"
"\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMaximumSize(QSize(7000, 80))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Inconsolata Semi Condensed Black")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"*{\n"
"color:rgb(170, 85, 255);\n"
"background:rgb(170, 170, 255);\n"
"}")
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lineEdit)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"*{\n"
"\n"
"color:rgb(170, 0, 255);\n"
"border-radius:17;\n"
"background:rgb(170, 170, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"background:rgb(170, 170, 255);\n"
"border:null;\n"
"	font: 25pt \"Inconsolata\";\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_8 = QPushButton(self.frame)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout.addWidget(self.pushButton_8, 3, 0, 1, 1)

        self.pushButton_18 = QPushButton(self.frame)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.gridLayout.addWidget(self.pushButton_18, 4, 1, 1, 1)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.frame)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout.addWidget(self.pushButton_9, 2, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)

        self.pushButton_12 = QPushButton(self.frame)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.gridLayout.addWidget(self.pushButton_12, 3, 2, 1, 1)

        self.pushButton_13 = QPushButton(self.frame)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.gridLayout.addWidget(self.pushButton_13, 0, 4, 1, 1)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_11 = QPushButton(self.frame)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout.addWidget(self.pushButton_11, 3, 1, 1, 1)

        self.pushButton_10 = QPushButton(self.frame)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout.addWidget(self.pushButton_10, 2, 2, 1, 1)

        self.pushButton_17 = QPushButton(self.frame)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.gridLayout.addWidget(self.pushButton_17, 4, 0, 1, 1)

        self.pushButton_14 = QPushButton(self.frame)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.gridLayout.addWidget(self.pushButton_14, 1, 4, 1, 1)

        self.pushButton_16 = QPushButton(self.frame)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.gridLayout.addWidget(self.pushButton_16, 3, 4, 1, 1)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 0, 0, 1, 1)

        self.pushButton_15 = QPushButton(self.frame)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.gridLayout.addWidget(self.pushButton_15, 2, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 3, 1, 1)

        self.pushButton_20 = QPushButton(self.frame)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setStyleSheet(u"*{\n"
"border-radius: 30px;\n"
"background-color:rgb(170, 0, 255);\n"
"color:rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 18px;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_20, 4, 4, 1, 1)

        self.pushButton_19 = QPushButton(self.frame)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.gridLayout.addWidget(self.pushButton_19, 4, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Kalc", None))
        self.lineEdit.setText("")
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u",", None))
    # retranslateUi

