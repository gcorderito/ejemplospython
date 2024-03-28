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

from datetime import datetime

class FormEmpleado(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/empleadoeditar.ui",self)
        self.cargarcombodepartamento()
        self.hoy = datetime.now().date()
        self.datenacimiento.setDate(self.hoy)
        self.datenacimiento.dateChanged.connect(self.calcularedad)
        self.btnguardar.clicked.connect(self.guardar)
        self.btnlimpiar.clicked.connect(self.limpiar)
        self.btncerrar.clicked.connect(self.close)

    def cargarcombodepartamento(self):
        departamentos = ["Atencion al cliente", "Admistrativa", "Sistemas", "Recursos Humanos", "Financiero"]

        for x in range(len(departamentos)):
            self.cbxdepartamento.addItem(departamentos[x])

    def calcularedad(self):
        anioactual = datetime.now().date().year
        mesactual = datetime.now().date().month
        diaactual = datetime.now().date().day

        fecha = self.datenacimiento.date().toPyDate()
        anionacimiento = fecha.year
        mesnacimiento  = fecha.month
        dianacimiento  = fecha.day

        if mesactual >= mesnacimiento and diaactual >= dianacimiento:
            edad = anioactual - anionacimiento
        else:
            edad = anioactual - anionacimiento
            edad = edad - 1
        self.spbedad.setValue(edad)
        

    def guardar(self):
        empleado = {}
        empleado['cedula'] = self.txtcedula.text()
        empleado['nombre'] = self.txtnombre.text()
        empleado['telefono'] = self.txttelefono.text()
        empleado['correo'] = self.txtcorreo.text()
        empleado['fechanacimiento'] = self.datenacimiento.date().toString('yyyy-MM-dd')
        if self.rbmasculino.isChecked() == True:
            empleado['sexo'] = "M"
        elif self.rbfemenino.isChecked() == True:
            empleado['sexo'] = "F"
        else:
            empleado['sexo'] = "N/A"
        empleado['edad'] = self.spbedad.value()
        empleado['strdepartamento'] = self.cbxdepartamento.currentText()
        empleado['indexdepartamento'] = self.cbxdepartamento.currentIndex()
        empleado['sueldo'] = self.spbsueldo.value()
        empleado['estado'] = self.chkestado.isChecked()

        print(empleado)

    def limpiar(self):
        self.txtcedula.setText("")
        self.txtnombre.setText("")
        self.txttelefono.setText("")
        self.txtcorreo.setText("")
        self.datenacimiento.setDate(self.hoy)
        self.rbmasculino.setChecked(False)
        self.rbfemenino.setChecked(False)
        self.spbedad.setValue(0)
        self.cbxdepartamento.setCurrentIndex(0)
        self.spbsueldo.setValue(0)
        self.chkestado.setChecked(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = FormEmpleado()
    GUI.show()
    sys.exit(app.exec_())