import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Calculadora(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/calculadora.ui",self)
        self.cargarcombooperacion()
        self.btncalcular.clicked.connect(self.calcular)
        self.btnlimpiar.clicked.connect(self.limpiar)
        self.btnsalir.clicked.connect(self.close)

    def cargarcombooperacion(self):
        operaciones = ["Suma","Resta","Multiplicación","División"]

        for x in range(len(operaciones)):
            self.cbxoperacion.addItem(operaciones[x])

    def suma(self):
        a = float(self.txta.text())
        b = float(self.txtb.text())

        resultado = a + b

        return resultado
    
    def resta(self):
        a = float(self.txta.text())
        b = float(self.txtb.text())

        resultado = a - b

        return resultado
    
    def multiplicacion(self):
        a = float(self.txta.text())
        b = float(self.txtb.text())

        resultado = a * b

        return resultado
    
    def division(self):
        a = float(self.txta.text())
        b = float(self.txtb.text())

        try:
            resultado = a / b
        except:
            msgbox = QMessageBox()
            msgbox.setIcon(QMessageBox.Critical)
            msgbox.setWindowTitle("Error")
            msgbox.setText("No se puede dividir entre cero.")
            msgbox.exec()

            resultado = 0

        return resultado

    def calcular(self):

        indexoperacion = self.cbxoperacion.currentIndex()

        if indexoperacion == 0:#Suma
            resultado = self.suma()
        elif indexoperacion == 1:#Resta
            resultado = self.resta()
        elif indexoperacion == 2:#Multiplicacion
            resultado = self.multiplicacion()
        elif indexoperacion == 3: #División
            resultado = self.division()
        else:
            resultado = 0

        self.txtresultado.setText(str(resultado))

    def limpiar(self):
        self.txta.setText("")
        self.txtb.setText("")
        self.txtresultado.setText("")
        self.cbxoperacion.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = Calculadora()
    GUI.show()
    sys.exit(app.exec_())