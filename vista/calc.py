# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(421, 435)
        MainWindow.setStyleSheet("*{\n"
"background:rgb(170, 85, 255);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setStyleSheet("*{\n"
"border-radius:16;\n"
"\n"
"background:white;\n"
"\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMaximumSize(QtCore.QSize(7000, 80))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Inconsolata Semi Condensed Black")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("*{\n"
"color:rgb(170, 85, 255);\n"
"background:rgb(170, 170, 255);\n"
"}")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.frame_3)
        self.frame.setStyleSheet("*{\n"
"\n"
"color:rgb(170, 0, 255);\n"
"border-radius:17;\n"
"background:rgb(170, 170, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"background:rgb(170, 170, 255);\n"
"border:null;\n"
"    font: 25pt \"Inconsolata\";\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 3, 0, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.frame)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout.addWidget(self.pushButton_18, 4, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 2, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.frame)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 3, 2, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.frame)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 0, 4, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.frame)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 3, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 2, 2, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.frame)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout.addWidget(self.pushButton_17, 4, 0, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.frame)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 1, 4, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.frame)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_16, 3, 4, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 0, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.frame)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_15, 2, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 3, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.frame)
        self.pushButton_20.setStyleSheet("*{\n"
"border-radius: 30px;\n"
"background-color:rgb(170, 0, 255);\n"
"color:rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 18px;\n"
"}")
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout.addWidget(self.pushButton_20, 4, 4, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.frame)
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout.addWidget(self.pushButton_19, 4, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.frame)
        self.verticalLayout.addWidget(self.frame_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kalc"))
        self.pushButton_8.setText(_translate("MainWindow", "1"))
        self.pushButton_18.setText(_translate("MainWindow", "0"))
        self.pushButton.setText(_translate("MainWindow", "("))
        self.pushButton_9.setText(_translate("MainWindow", "5"))
        self.pushButton_5.setText(_translate("MainWindow", "8"))
        self.pushButton_7.setText(_translate("MainWindow", "4"))
        self.pushButton_6.setText(_translate("MainWindow", "9"))
        self.pushButton_2.setText(_translate("MainWindow", ")"))
        self.pushButton_12.setText(_translate("MainWindow", "3"))
        self.pushButton_13.setText(_translate("MainWindow", "*"))
        self.pushButton_4.setText(_translate("MainWindow", "7"))
        self.pushButton_11.setText(_translate("MainWindow", "2"))
        self.pushButton_10.setText(_translate("MainWindow", "6"))
        self.pushButton_17.setText(_translate("MainWindow", "."))
        self.pushButton_14.setText(_translate("MainWindow", "%"))
        self.pushButton_16.setText(_translate("MainWindow", "+"))
        self.pushButton_3.setText(_translate("MainWindow", "C"))
        self.pushButton_15.setText(_translate("MainWindow", "-"))
        self.pushButton_20.setText(_translate("MainWindow", "="))
        self.pushButton_19.setText(_translate("MainWindow", ","))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
