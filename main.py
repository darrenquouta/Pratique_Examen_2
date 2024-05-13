import Qt_PY.Page_Principale
from Dialog.Dialogue_Etudiant import page_etudiant
from Dialog.Dialogue_Cours import page_cours

import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot

class pageAccueil(QtWidgets.QMainWindow, Qt_PY.Page_Principale.Ui_MainWindow):
    def __init__(self, parent=None):
        super(pageAccueil, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButtonGererEtudiants_clicked(self):
        page_dialogue = page_etudiant()
        page_dialogue.show()
        page_dialogue.exec_()

    @pyqtSlot()
    def on_pushButtonGererCours_clicked(self):
        page_dialogue = page_cours()
        page_dialogue.show()
        page_dialogue.exec_()

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = pageAccueil()
    form.show()
    app.exec()

if __name__ == "__main__":
    main()