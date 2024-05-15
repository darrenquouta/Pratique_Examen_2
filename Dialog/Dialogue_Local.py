from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
import Qt_PY.Page_Local
from Classes.Classe_Local_Normal import Local_Normal
from Classes.Classe_Local_Technique import Local_Technique
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

    @pyqtSlot()
    def on_pushButtonAjouter_clicked(self):
        numero_local = self.lineEditNumero.text()
        superficie_local = self.lineEditSuperficie.text()
        nombre_places = self.lineEditNombrePlaces.text()
        if self.comboBoxType.currentText() == "Technique":
            local_technique = Local_Technique()
            erreur = False
            marque_ordinateurs = self.lineEditMarque.text()
            nombre_ordinateurs = self.lineEditNombreOrdinateurs.text()
            try:
                local_technique.numero_local = numero_local
            except ValueError as error:
                self.labelErreurNumero.setText(f"{error}")
                erreur = True
            try:
                local_technique.superficie_local = float(superficie_local)
            except ValueError as error:
                self.labelErreurSuperficie.setText(f"{error}")
                erreur = True
            try:
                local_technique.nombre_places = int(nombre_places)
            except ValueError as error:
                self.labelErreurNombrePlaces.setText(f"{error}")
                erreur = True
            local_technique.type_local = self.comboBoxType.currentText()
            local_technique.lieu_local = self.comboBoxBloc.currentText()
            try:
                local_technique.marque_ordinateurs = marque_ordinateurs
            except ValueError as error:
                self.labelErreurMarque.setText(f"{error}")
                erreur = True
            try:
                local_technique.nombre_ordinateurs = int(nombre_ordinateurs)
            except ValueError as error:
                self.labelErreurNombreOrdinateurs.setText(f"{error}")
                erreur = True
            local_technique.projecteur = self.comboBoxProjecteur.currentText()
            if erreur == True:
                self.lineEditNumero.clear()
                self.lineEditSuperficie.clear()
                self.lineEditNombrePlaces.clear()
                self.lineEditMarque.clear()
                self.lineEditNombreOrdinateurs.clear()
                return None
            else:
                try:
                    Local_Technique.ajouter_local(local_technique)
                    self.textBrowserLocal.clear()
                    for local in Local.liste_locaux:
                        self.textBrowserLocal.append(local.__str__())
                except ValueError as error:
                    self.textBrowserLocal.setText(f"{error}")
                    return None
        else:
            local_normal = Local_Normal()
            erreur = False
            nombre_places_par_table = self.lineEditNombrePlacesParTable.text()
            try:
                local_normal.numero_local = numero_local
            except ValueError as error:
                self.labelErreurNumero.setText(f"{error}")
                erreur = True
            try:
                local_normal.superficie_local = float(superficie_local)
            except ValueError as error:
                self.labelErreurSuperficie.setText(f"{error}")
                erreur = True
            try:
                local_normal.nombre_places = int(nombre_places)
            except ValueError as error:
                self.labelErreurNombrePlaces.setText(f"{error}")
                erreur = True
            local_normal.type_local = self.comboBoxType.currentText()
            local_normal.lieu_local = self.comboBoxBloc.currentText()
            try:
                local_normal.nombre_places_par_table = int(nombre_places_par_table)
            except ValueError as error:
                self.labelErreurNombrePlaces.setText(f"{error}")
                erreur = True
            if erreur == True:
                self.lineEditNumero.clear()
                self.lineEditSuperficie.clear()
                self.lineEditNombrePlaces.clear()
                self.lineEditMarque.clear()
                self.lineEditNombreOrdinateurs.clear()
                return None
            else:
                try:
                    Local_Normal.ajouter_local(local_normal)
                    self.textBrowserLocal.clear()
                    for local in Local.liste_locaux:
                        self.textBrowserLocal.append(local.__str__())
                except ValueError as error:
                    self.textBrowserLocal.setText(f"{error}")
                    return None




