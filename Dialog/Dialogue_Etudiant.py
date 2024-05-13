import Qt_PY.Page_Etudiant
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from Classes.Classe_Etudiant import Etudiant

class page_etudiant(QtWidgets.QDialog, Qt_PY.Page_Etudiant.Ui_Dialog):

    def __init__(self, parent=None):
        super(page_etudiant, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButtonAjouter_clicked(self):
        etudiant = Etudiant()
        numero_etudiant = self.lineEditNumEtud.text()
        nom_etudiant = self.lineEditNomEtud.text()
        programme = self.comboBoxProgramme.currentText()
        date_naissance = self.dateEditDateNaissance.date().toPyDate()
        etudiant.programme_etudiant = programme
        etudiant.date_naissance = date_naissance

        ajout = True

        try:
            etudiant.numero_etudiant = numero_etudiant
        except ValueError as error:
            self.labelErreurNumero.setText(f"{error}")
            ajout = False
        try:
            etudiant.nom_etudiant = nom_etudiant
        except ValueError as error:
            self.labelErreurNom.setText(f"{error}")
            ajout = False

        if ajout == False:
            self.lineEditNumEtud.clear()
            self.lineEditNomEtud.clear()
            return None

        if ajout == True:
            self.lineEditNumEtud.clear()
            self.lineEditNomEtud.clear()
            try:
                Etudiant.ajouter_etudiant(etudiant)
                self.textBrowserEtud.clear()
                for etudiant in Etudiant.liste_etudiants:
                    self.textBrowserEtud.append(etudiant.__str__())
            except ValueError as error:
                self.textBrowserEtud.setText(f"{error}")
                return None

    @pyqtSlot()
    def on_pushButtonSupprimer_clicked(self):
        numero_etudiant = self.lineEditNumEtud.text()
        for etudiant in Etudiant.liste_etudiants:
            if etudiant.numero_etudiant == numero_etudiant:
                Etudiant.liste_etudiants.remove(etudiant)
                self.labelErreurNumero.setText("L'étudiant a été enlevé !")
                break
        else:
            self.labelErreurNumero.setText("Cet étudiant n'existe pas !")
            return None
        self.textBrowserEtud.clear()
        for etudiant in Etudiant.liste_etudiants:
            self.textBrowserEtud.append(etudiant.__str__())

    @pyqtSlot()
    def on_pushButtonModifier_clicked(self):
        numero_etudiant = self.lineEditNumEtud.text()
        for etudiant in Etudiant.liste_etudiants:
            if etudiant.numero_etudiant == numero_etudiant:
                nom_etudiant = self.lineEditNomEtud.text()
                try:
                    etudiant.nom_etudiant = nom_etudiant
                except ValueError as error:
                    self.labelErreurNom.setText(f"{error}")
                programme = self.comboBoxProgramme.currentText()
                etudiant.programme = programme
                date_naissance = self.dateEditDateNaissance.date().toPyDate()
                etudiant.date_naissance = date_naissance
                break
        else:
            self.labelErreurNumero.setText("Cet étudiant n'existe pas !")
            return None
        self.textBrowserEtud.clear()
        for etudiant in Etudiant.liste_etudiants:
            self.textBrowserEtud.append(etudiant.__str__())

    @pyqtSlot()
    def on_pushButtonSauvegarder_clicked(self):
        liste_etudiants = []
        for etudiant in Etudiant.liste_etudiants:
            liste_informations = etudiant.__str__().splitlines()
            informations = ""
            for information in liste_informations:
                informations = informations + information + "\n"
            liste_etudiants.append(informations)
        with open("fichier_informations.txt", "w") as fichier:
            for etudiant in liste_etudiants:
                fichier.writelines(etudiant)








