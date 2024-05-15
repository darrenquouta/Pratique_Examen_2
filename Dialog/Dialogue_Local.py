from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
import Qt_PY.Page_Local
from Classes.Classe_Local import Local
class page_local(QtWidgets.QDialog, Qt_PY.Page_Local.Ui_Dialog):

    def __init__(self, parent=None):
        super(page_local, self).__init__(parent)
        self.setupUi(self)
        self.labelTechnique.setDisabled(True)
        self.labelMarque.setDisabled(True)
        self.lineEditMarque.setDisabled(True)
        self.labelNombreOrdinateurs.setDisabled(True)
        self.lineEditNombreOrdinateurs.setDisabled(True)
        self.labelProjecteur.setDisabled(True)
        self.comboBoxProjecteur.setDisabled(True)
        self.comboBoxType.currentIndexChanged.connect(self.type_local)

    def activation_local(self, technique):
        self.labelTechnique.setDisabled(not technique)
        self.labelMarque.setDisabled(not technique)
        self.lineEditMarque.setDisabled(not technique)
        self.labelNombreOrdinateurs.setDisabled(not technique)
        self.lineEditNombreOrdinateurs.setDisabled(not technique)
        self.labelProjecteur.setDisabled(not technique)
        self.comboBoxProjecteur.setDisabled(not technique)
        self.labelNormal.setDisabled(technique)
        self.labelNombrePlacesParTable.setDisabled(technique)
        self.lineEditNombrePlacesParTable.setDisabled(technique)

    def type_local(self):
        if "Technique" == self.comboBoxType.currentText():
            technique = True
        else:
            technique = False
        self.activation_local(technique)



