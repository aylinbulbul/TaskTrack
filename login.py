# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(337, 584)
        MainWindow.setStyleSheet("background-color: rgb(255, 235, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.publicGL = QtWidgets.QGridLayout()
        self.publicGL.setObjectName("publicGL")
        self.passwordVL = QtWidgets.QVBoxLayout()
        self.passwordVL.setObjectName("passwordVL")
        self.passwordLE = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordLE.sizePolicy().hasHeightForWidth())
        self.passwordLE.setSizePolicy(sizePolicy)
        self.passwordLE.setStyleSheet("background-color: rgb(255, 235, 255);\n"
"border : 2px solid rgb(85, 0, 0);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.passwordLE.setText("")
        self.passwordLE.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLE.setObjectName("passwordLE")
        self.passwordVL.addWidget(self.passwordLE)
        self.publicGL.addLayout(self.passwordVL, 3, 0, 1, 1)
        self.loginVL = QtWidgets.QVBoxLayout()
        self.loginVL.setObjectName("loginVL")
        self.loginBut = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginBut.sizePolicy().hasHeightForWidth())
        self.loginBut.setSizePolicy(sizePolicy)
        self.loginBut.setStyleSheet("color : rgb(85, 0, 0);\n"
"font: 87 italic 12pt \"Segoe UI Black\";\n"
"background-color: rgb(255, 235, 255);\n"
"border : 2px solid rgb(85, 0, 0);")
        self.loginBut.setObjectName("loginBut")
        self.loginVL.addWidget(self.loginBut)
        self.publicGL.addLayout(self.loginVL, 4, 0, 1, 1)
        self.registerVL = QtWidgets.QVBoxLayout()
        self.registerVL.setObjectName("registerVL")
        self.registerBut = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerBut.sizePolicy().hasHeightForWidth())
        self.registerBut.setSizePolicy(sizePolicy)
        self.registerBut.setStyleSheet("color : rgb(85, 0, 0);\n"
"font: 87 italic 12pt \"Segoe UI Black\";\n"
"background-color: rgb(255, 235, 255);\n"
"border : 2px solid rgb(85, 0, 0);")
        self.registerBut.setObjectName("registerBut")
        self.registerVL.addWidget(self.registerBut)
        self.publicGL.addLayout(self.registerVL, 5, 0, 1, 1)
        self.welcomeVL = QtWidgets.QVBoxLayout()
        self.welcomeVL.setObjectName("welcomeVL")
        self.welcomelbl = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.welcomelbl.sizePolicy().hasHeightForWidth())
        self.welcomelbl.setSizePolicy(sizePolicy)
        self.welcomelbl.setStyleSheet("color : rgb(85, 0, 0);\n"
"font: 18pt \"Stencil\";\n"
"background-color: rgb(255, 235, 255);\n"
"border : 2px solid rgb(85, 0, 0);")
        self.welcomelbl.setAlignment(QtCore.Qt.AlignCenter)
        self.welcomelbl.setObjectName("welcomelbl")
        self.welcomeVL.addWidget(self.welcomelbl)
        self.publicGL.addLayout(self.welcomeVL, 1, 0, 1, 1)
        self.userNameVL = QtWidgets.QVBoxLayout()
        self.userNameVL.setObjectName("userNameVL")
        self.userNameLE = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userNameLE.sizePolicy().hasHeightForWidth())
        self.userNameLE.setSizePolicy(sizePolicy)
        self.userNameLE.setStyleSheet("background-color: rgb(255, 235, 255);\n"
"border : 2px solid rgb(85, 0, 0);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.userNameLE.setText("")
        self.userNameLE.setObjectName("userNameLE")
        self.userNameVL.addWidget(self.userNameLE)
        self.publicGL.addLayout(self.userNameVL, 2, 0, 1, 1)
        self.logoVL = QtWidgets.QVBoxLayout()
        self.logoVL.setObjectName("logoVL")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("background-color: rgb(255, 235, 255);\n"
"border : 2px solid rgb(85, 0, 0);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ok.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.logoVL.addWidget(self.label)
        self.publicGL.addLayout(self.logoVL, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.publicGL)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 337, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TASK TRACK"))
        self.passwordLE.setPlaceholderText(_translate("MainWindow", "Şifre : "))
        self.loginBut.setText(_translate("MainWindow", "Giriş Yap"))
        self.registerBut.setText(_translate("MainWindow", "Kayıt Ol"))
        self.welcomelbl.setText(_translate("MainWindow", "HOSGELDİNİZ.."))
        self.userNameLE.setPlaceholderText(_translate("MainWindow", "Kullanıcı Adı :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
