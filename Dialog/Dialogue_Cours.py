from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
import Qt_PY.Page_Cours
from Classes.Classe_Cours import Cours
from Dialog.Dialogue_Association import page_association
class page_cours(QtWidgets.QDialog, Qt_PY.Page_Cours.Ui_Dialog):

    def __init__(self, parent=None):
        super(page_cours, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButtonAjouter_clicked(self):
        cours = Cours()
        sigle_cours = self.lineEditSigle.text()
        titre_cours = self.lineEditTitre.text()
        nombre_heures_cours = self.lineEditHeures.text()
        erreur = False
        try:
            cours.sigle_cours = sigle_cours
        except ValueError as error:
            self.labelErreurSigle.setText(f"{error}")
            erreur = True
        try:
            cours.titre_cours = titre_cours
        except ValueError as error:
            self.labelErreurTitre.setText(f"{error}")
            erreur = True
        try:
            cours.nombre_heures_cours = int(nombre_heures_cours)
        except ValueError as error:
            self.labelErreurHeures.setText(f"{error}")
            erreur = True

        if erreur == True:
            self.lineEditSigle.clear()
            self.lineEditTitre.clear()
            self.lineEditHeures.clear()
            return None

        if erreur == False:
            self.lineEditSigle.clear()
            self.lineEditTitre.clear()
            self.lineEditHeures.clear()
            reponse = Cours.ajouter_cours(cours)
            if reponse == True:
                self.textBrowserCours.clear()
                for cours in Cours.liste_cours:
                    self.textBrowserCours.append(cours.__str__())
            else:
                self.textBrowserCours.setText("Ce cours existe déjà, ajout échoué !")
                return None

    @pyqtSlot()
    def on_pushButtonAssocier_clicked(self):
        dialogue = page_association()
        dialogue.show()
        dialogue.exec_()




