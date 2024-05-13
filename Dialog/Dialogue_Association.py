from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
import Qt_PY.Page_Association
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from Classes.Classe_Cours import Cours
from Classes.Classe_Etudiant import Etudiant

class page_association(QtWidgets.QDialog, Qt_PY.Page_Association.Ui_Dialog):

    def __init__(self, parent=None):
        super(page_association, self).__init__(parent)
        self.setupUi(self)
        # Préparation des comboBox
        for cours in Cours.liste_cours:
            self.comboBoxCours.addItem(cours.sigle_cours)
        for etudiant in Etudiant.liste_etudiants:
            self.comboBoxEtudiant.addItem(etudiant.numero_etudiant)
        # Préparation du modèle
        self.model = QStandardItemModel()
        self.listViewCours.setModel(self.model)

    @pyqtSlot()
    def on_pushButtonAjouter_clicked(self):
        sigle = self.comboBoxCours.currentText()
        for cours in Cours.liste_cours:
            if cours.sigle_cours == sigle:
                cours_selectionne = cours
                break
        item = QStandardItem(f"Sigle : {cours_selectionne.sigle_cours} / Titre : {cours_selectionne.titre_cours}")
        self.model.appendRow(item)

    @pyqtSlot()
    def on_pushButtonAssocier_clicked(self):
        self.labelErreur.clear()
        numero_etudiant = self.comboBoxEtudiant.currentText()
        sigle_cours = self.comboBoxCours.currentText()
        for etudiant in Etudiant.liste_etudiants:
            if etudiant.numero_etudiant == numero_etudiant:
                etudiant_selectionne = etudiant
                break
        for cours in Cours.liste_cours:
            if cours.sigle_cours == sigle_cours:
                cours_selectionne = cours
                break
        for cours in etudiant_selectionne.liste_cours_inscrit:
            if cours.sigle_cours == cours_selectionne.sigle_cours:
                self.labelErreur.setText("Cette association existe déja !")
                return None
        else:
            etudiant_selectionne.liste_cours_inscrit.append(cours_selectionne)
            self.labelErreur.setText("L'association est fait !")
        for etudiant in cours_selectionne.liste_etudiants_inscrits:
            if etudiant.numero_etudiant == etudiant_selectionne.numero_etudiant:
                self.labelErreur.setText("Cette association existe déjà !")
                return None
        else:
            cours_selectionne.liste_etudiants_inscrits.append(etudiant_selectionne)
            self.labelErreur.setText("L'association est fait !")

