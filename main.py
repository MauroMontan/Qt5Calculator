from PyQt5.QtWidgets import *
import sys
from vista.calc import Ui_MainWindow

class Registro(QMainWindow):
    def __init__(self,):
        super(Registro,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.resultado=False

        self.ui.pushButton_18.clicked.connect(lambda:self.ui.lineEdit.insert("0"))
        self.ui.pushButton.clicked.connect(lambda:self.ui.lineEdit.insert("("))
        self.ui.pushButton_9.clicked.connect(lambda:self.ui.lineEdit.insert("5"))
        self.ui.pushButton_5.clicked.connect(lambda:self.ui.lineEdit.insert("8"))
        self.ui.pushButton_8.clicked.connect(lambda:self.ui.lineEdit.insert("1"))
        self.ui.pushButton_7.clicked.connect(lambda:self.ui.lineEdit.insert("4"))
        self.ui.pushButton_6.clicked.connect(lambda:self.ui.lineEdit.insert("9"))
        self.ui.pushButton_2.clicked.connect(lambda:self.ui.lineEdit.insert(")"))
        self.ui.pushButton_12.clicked.connect(lambda:self.ui.lineEdit.insert("3"))
        self.ui.pushButton_13.clicked.connect(lambda:self.ui.lineEdit.insert("*"))
        self.ui.pushButton_4.clicked.connect(lambda:self.ui.lineEdit.insert("7"))
        self.ui.pushButton_11.clicked.connect(lambda:self.ui.lineEdit.insert("2"))
        self.ui.pushButton_10.clicked.connect(lambda:self.ui.lineEdit.insert("6"))
        self.ui.pushButton_17.clicked.connect(lambda:self.ui.lineEdit.insert("."))
        self.ui.pushButton_14.clicked.connect(lambda:self.ui.lineEdit.insert("%"))
        self.ui.pushButton_16.clicked.connect(lambda:self.ui.lineEdit.insert("+"))
        self.ui.pushButton_15.clicked.connect(lambda:self.ui.lineEdit.insert("-"))
        self.ui.pushButton_3.clicked.connect(lambda:self.ui.lineEdit.setText(""))
        self.ui.pushButton_19.clicked.connect(lambda:self.ui.lineEdit.setText(""))
        self.ui.pushButton_20.clicked.connect(self.calcular)
    def calcular(self):
        x=eval(self.ui.lineEdit.text())
        self.ui.lineEdit.setText("")
        self.ui.lineEdit.setText(str(x))



if __name__ == '__main__':
    app=QApplication(sys.argv)
    my_app=Registro()
    my_app.show()
    sys.exit(app.exec_())
