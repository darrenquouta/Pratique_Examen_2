# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Page_Principale.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(793, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelAccueil = QtWidgets.QLabel(self.centralwidget)
        self.labelAccueil.setGeometry(QtCore.QRect(90, 20, 621, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelAccueil.setFont(font)
        self.labelAccueil.setObjectName("labelAccueil")
        self.pushButtonGererEtudiants = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonGererEtudiants.setGeometry(QtCore.QRect(10, 190, 251, 81))
        self.pushButtonGererEtudiants.setObjectName("pushButtonGererEtudiants")
        self.pushButtonGererCours = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonGererCours.setGeometry(QtCore.QRect(530, 190, 251, 81))
        self.pushButtonGererCours.setObjectName("pushButtonGererCours")
        self.pushButtonGererLocaux = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonGererLocaux.setGeometry(QtCore.QRect(10, 450, 251, 81))
        self.pushButtonGererLocaux.setObjectName("pushButtonGererLocaux")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 793, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelAccueil.setText(_translate("MainWindow", "Bienvenue à l\'application de gestion scolaire !"))
        self.pushButtonGererEtudiants.setText(_translate("MainWindow", "Gérer les étudiants"))
        self.pushButtonGererCours.setText(_translate("MainWindow", "Gérer les cours"))
        self.pushButtonGererLocaux.setText(_translate("MainWindow", "Gérer les locaux"))
