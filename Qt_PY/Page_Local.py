# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Page_Local.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(837, 856)
        self.labelSuperficie = QtWidgets.QLabel(Dialog)
        self.labelSuperficie.setGeometry(QtCore.QRect(10, 130, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelSuperficie.setFont(font)
        self.labelSuperficie.setObjectName("labelSuperficie")
        self.labelNumero = QtWidgets.QLabel(Dialog)
        self.labelNumero.setGeometry(QtCore.QRect(10, 10, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelNumero.setFont(font)
        self.labelNumero.setObjectName("labelNumero")
        self.labelNombrePlaces = QtWidgets.QLabel(Dialog)
        self.labelNombrePlaces.setGeometry(QtCore.QRect(10, 260, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelNombrePlaces.setFont(font)
        self.labelNombrePlaces.setObjectName("labelNombrePlaces")
        self.labelType = QtWidgets.QLabel(Dialog)
        self.labelType.setGeometry(QtCore.QRect(10, 390, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelType.setFont(font)
        self.labelType.setObjectName("labelType")
        self.labelBloc = QtWidgets.QLabel(Dialog)
        self.labelBloc.setGeometry(QtCore.QRect(10, 510, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelBloc.setFont(font)
        self.labelBloc.setObjectName("labelBloc")
        self.lineEditNumero = QtWidgets.QLineEdit(Dialog)
        self.lineEditNumero.setGeometry(QtCore.QRect(10, 50, 271, 41))
        self.lineEditNumero.setObjectName("lineEditNumero")
        self.lineEditSuperficie = QtWidgets.QLineEdit(Dialog)
        self.lineEditSuperficie.setGeometry(QtCore.QRect(10, 180, 271, 41))
        self.lineEditSuperficie.setObjectName("lineEditSuperficie")
        self.lineEditNombrePlaces = QtWidgets.QLineEdit(Dialog)
        self.lineEditNombrePlaces.setGeometry(QtCore.QRect(10, 310, 271, 41))
        self.lineEditNombrePlaces.setObjectName("lineEditNombrePlaces")
        self.comboBoxType = QtWidgets.QComboBox(Dialog)
        self.comboBoxType.setGeometry(QtCore.QRect(10, 440, 151, 41))
        self.comboBoxType.setObjectName("comboBoxType")
        self.comboBoxType.addItem("")
        self.comboBoxType.addItem("")
        self.comboBoxBloc = QtWidgets.QComboBox(Dialog)
        self.comboBoxBloc.setGeometry(QtCore.QRect(10, 550, 151, 41))
        self.comboBoxBloc.setObjectName("comboBoxBloc")
        self.comboBoxBloc.addItem("")
        self.comboBoxBloc.addItem("")
        self.comboBoxBloc.addItem("")
        self.labelTechnique = QtWidgets.QLabel(Dialog)
        self.labelTechnique.setGeometry(QtCore.QRect(540, 0, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelTechnique.setFont(font)
        self.labelTechnique.setObjectName("labelTechnique")
        self.labelMarque = QtWidgets.QLabel(Dialog)
        self.labelMarque.setGeometry(QtCore.QRect(540, 50, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelMarque.setFont(font)
        self.labelMarque.setObjectName("labelMarque")
        self.lineEditMarque = QtWidgets.QLineEdit(Dialog)
        self.lineEditMarque.setGeometry(QtCore.QRect(540, 100, 271, 41))
        self.lineEditMarque.setObjectName("lineEditMarque")
        self.labelNombreOrdinateurs = QtWidgets.QLabel(Dialog)
        self.labelNombreOrdinateurs.setGeometry(QtCore.QRect(540, 180, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelNombreOrdinateurs.setFont(font)
        self.labelNombreOrdinateurs.setObjectName("labelNombreOrdinateurs")
        self.lineEditNombreOrdinateurs = QtWidgets.QLineEdit(Dialog)
        self.lineEditNombreOrdinateurs.setGeometry(QtCore.QRect(540, 220, 271, 41))
        self.lineEditNombreOrdinateurs.setObjectName("lineEditNombreOrdinateurs")
        self.labelProjecteur = QtWidgets.QLabel(Dialog)
        self.labelProjecteur.setGeometry(QtCore.QRect(540, 300, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelProjecteur.setFont(font)
        self.labelProjecteur.setObjectName("labelProjecteur")
        self.comboBoxProjecteur = QtWidgets.QComboBox(Dialog)
        self.comboBoxProjecteur.setGeometry(QtCore.QRect(540, 350, 151, 41))
        self.comboBoxProjecteur.setObjectName("comboBoxProjecteur")
        self.comboBoxProjecteur.addItem("")
        self.comboBoxProjecteur.addItem("")
        self.labelNormal = QtWidgets.QLabel(Dialog)
        self.labelNormal.setGeometry(QtCore.QRect(540, 450, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelNormal.setFont(font)
        self.labelNormal.setObjectName("labelNormal")
        self.textBrowserLocal = QtWidgets.QTextBrowser(Dialog)
        self.textBrowserLocal.setGeometry(QtCore.QRect(240, 640, 571, 211))
        self.textBrowserLocal.setObjectName("textBrowserLocal")
        self.pushButtonAjouter = QtWidgets.QPushButton(Dialog)
        self.pushButtonAjouter.setGeometry(QtCore.QRect(10, 640, 211, 61))
        self.pushButtonAjouter.setObjectName("pushButtonAjouter")
        self.labelNombrePlacesParTable = QtWidgets.QLabel(Dialog)
        self.labelNombrePlacesParTable.setGeometry(QtCore.QRect(540, 490, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelNombrePlacesParTable.setFont(font)
        self.labelNombrePlacesParTable.setObjectName("labelNombrePlacesParTable")
        self.lineEditNombrePlacesParTable = QtWidgets.QLineEdit(Dialog)
        self.lineEditNombrePlacesParTable.setGeometry(QtCore.QRect(540, 540, 271, 41))
        self.lineEditNombrePlacesParTable.setObjectName("lineEditNombrePlacesParTable")
        self.labelErreurNumero = QtWidgets.QLabel(Dialog)
        self.labelErreurNumero.setGeometry(QtCore.QRect(10, 100, 271, 16))
        self.labelErreurNumero.setText("")
        self.labelErreurNumero.setObjectName("labelErreurNumero")
        self.labelErreurSuperficie = QtWidgets.QLabel(Dialog)
        self.labelErreurSuperficie.setGeometry(QtCore.QRect(10, 230, 271, 16))
        self.labelErreurSuperficie.setText("")
        self.labelErreurSuperficie.setObjectName("labelErreurSuperficie")
        self.labelErreurNombrePlaces = QtWidgets.QLabel(Dialog)
        self.labelErreurNombrePlaces.setGeometry(QtCore.QRect(10, 360, 271, 16))
        self.labelErreurNombrePlaces.setText("")
        self.labelErreurNombrePlaces.setObjectName("labelErreurNombrePlaces")
        self.labelErreurMarque = QtWidgets.QLabel(Dialog)
        self.labelErreurMarque.setGeometry(QtCore.QRect(540, 150, 271, 16))
        self.labelErreurMarque.setText("")
        self.labelErreurMarque.setObjectName("labelErreurMarque")
        self.labelErreurNombreOrdinateurs = QtWidgets.QLabel(Dialog)
        self.labelErreurNombreOrdinateurs.setGeometry(QtCore.QRect(540, 270, 271, 16))
        self.labelErreurNombreOrdinateurs.setText("")
        self.labelErreurNombreOrdinateurs.setObjectName("labelErreurNombreOrdinateurs")
        self.labelNombrePlacesParTable_2 = QtWidgets.QLabel(Dialog)
        self.labelNombrePlacesParTable_2.setGeometry(QtCore.QRect(540, 590, 271, 16))
        self.labelNombrePlacesParTable_2.setText("")
        self.labelNombrePlacesParTable_2.setObjectName("labelNombrePlacesParTable_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelSuperficie.setText(_translate("Dialog", "Superficie du local"))
        self.labelNumero.setText(_translate("Dialog", "Numéro du local"))
        self.labelNombrePlaces.setText(_translate("Dialog", "Nombre de places"))
        self.labelType.setText(_translate("Dialog", "Type de local"))
        self.labelBloc.setText(_translate("Dialog", "Bloc du local"))
        self.comboBoxType.setItemText(0, _translate("Dialog", "Normal"))
        self.comboBoxType.setItemText(1, _translate("Dialog", "Technique"))
        self.comboBoxBloc.setItemText(0, _translate("Dialog", "A"))
        self.comboBoxBloc.setItemText(1, _translate("Dialog", "B"))
        self.comboBoxBloc.setItemText(2, _translate("Dialog", "C"))
        self.labelTechnique.setText(_translate("Dialog", "Local technique"))
        self.labelMarque.setText(_translate("Dialog", "Marque des ordinateurs"))
        self.labelNombreOrdinateurs.setText(_translate("Dialog", "Nombre d\'ordinateurs"))
        self.labelProjecteur.setText(_translate("Dialog", "Projecteur"))
        self.comboBoxProjecteur.setItemText(0, _translate("Dialog", "True"))
        self.comboBoxProjecteur.setItemText(1, _translate("Dialog", "False"))
        self.labelNormal.setText(_translate("Dialog", "Local normal"))
        self.pushButtonAjouter.setText(_translate("Dialog", "Ajouter local"))
        self.labelNombrePlacesParTable.setText(_translate("Dialog", "Nombre de places par table"))
