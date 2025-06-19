import sys
from interface import interface
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMainWindow

from interface.interface import Ui_MainWindow


class calcul(QMainWindow):
    def __init__(self):
        super().__init__()
        self.UI = Ui_MainWindow()
        self.UI.setupUi(self)
        self.UI.pushButton.clicked.connect(self.Addition)

    def Addition(self):
        a=int(self.UI.lineEdit.text())
        b=int(self.UI.lineEdit_2.text())
        r=a+b
        print(str(r))
        self.UI.resultat.setText(str(r))

app = QApplication(sys.argv)
window = calcul()
window.show()
app.exec_()

