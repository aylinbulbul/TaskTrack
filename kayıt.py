# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kayıt.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(373, 501)
        MainWindow.setStyleSheet("background-color: rgb(255, 235, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.userRegFormVL = QtWidgets.QVBoxLayout()
        self.userRegFormVL.setObjectName("userRegFormVL")
        self.userRegFormlbl = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userRegFormlbl.sizePolicy().hasHeightForWidth())
        self.userRegFormlbl.setSizePolicy(sizePolicy)
        self.userRegFormlbl.setStyleSheet("color : rgb(85, 0, 0);\n"
"font: 87 italic 14pt \"Segoe UI Black\";\n"
"background-color: rgb(255, 235, 255);\n"
"border : 2px solid rgb(85, 0, 0);")
        self.userRegFormlbl.setAlignment(QtCore.Qt.AlignCenter)
        self.userRegFormlbl.setObjectName("userRegFormlbl")
        self.userRegFormVL.addWidget(self.userRegFormlbl)
        self.gridLayout_2.addLayout(self.userRegFormVL, 0, 0, 1, 1)
        self.userNameVL = QtWidgets.QVBoxLayout()
        self.userNameVL.setObjectName("userNameVL")
        self.userNamelbl = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userNamelbl.sizePolicy().hasHeightForWidth())
        self.userNamelbl.setSizePolicy(sizePolicy)
        self.userNamelbl.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"background-color: rgb(255, 235, 255);\n"
"border : 2px solid rgb(85, 0, 0);\n"
"color : rgb(85, 0, 0)\n"
"")
        self.userNamelbl.setObjectName("userNamelbl")
        self.userNameVL.addWidget(self.userNamelbl)
        self.gridLayout_2.addLayout(self.userNameVL, 1, 0, 1, 1)
        self.userNameVL_2 = QtWidgets.QVBoxLayout()
        self.userNameVL_2.setObjectName("userNameVL_2")
        self.userNamelbl_2 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userNamelbl_2.sizePolicy().hasHeightForWidth())
        self.userNamelbl_2.setSizePolicy(sizePolicy)
        self.userNamelbl_2.setStyleSheet("background-color: rgb(255, 235, 255);\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"border : 2px solid rgb(85, 0, 0);\n"
"\n"
"")
        self.userNamelbl_2.setText("")
        self.userNamelbl_2.setObjectName("userNamelbl_2")
        self.userNameVL_2.addWidget(self.userNamelbl_2)
        self.gridLayout_2.addLayout(self.userNameVL_2, 2, 0, 1, 1)
        self.mailVL = QtWidgets.QVBoxLayout()
        self.mailVL.setObjectName("mailVL")
        self.maillbl = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maillbl.sizePolicy().hasHeightForWidth())
        self.maillbl.setSizePolicy(sizePolicy)
        self.maillbl.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"background-color: rgb(255, 235, 255);\n"
"border : 2px solid rgb(85, 0, 0);\n"
"color : rgb(85, 0, 0)\n"
"")
        self.maillbl.setObjectName("maillbl")
        self.mailVL.addWidget(self.maillbl)
        self.gridLayout_2.addLayout(self.mailVL, 3, 0, 1, 1)
        self.mailVL_2 = QtWidgets.QVBoxLayout()
        self.mailVL_2.setObjectName("mailVL_2")
        self.maillbl_2 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maillbl_2.sizePolicy().hasHeightForWidth())
        self.maillbl_2.setSizePolicy(sizePolicy)
        self.maillbl_2.setStyleSheet("background-color: rgb(255, 235, 255);\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"border : 2px solid rgb(85, 0, 0);\n"
"\n"
"")
        self.maillbl_2.setObjectName("maillbl_2")
        self.mailVL_2.addWidget(self.maillbl_2)
        self.gridLayout_2.addLayout(self.mailVL_2, 4, 0, 1, 1)
        self.passwordVL = QtWidgets.QVBoxLayout()
        self.passwordVL.setObjectName("passwordVL")
        self.passwordlbl = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordlbl.sizePolicy().hasHeightForWidth())
        self.passwordlbl.setSizePolicy(sizePolicy)
        self.passwordlbl.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"background-color: rgb(255, 235, 255);\n"
"border : 2px solid rgb(85, 0, 0);\n"
"color : rgb(85, 0, 0)\n"
"")
        self.passwordlbl.setObjectName("passwordlbl")
        self.passwordVL.addWidget(self.passwordlbl)
        self.gridLayout_2.addLayout(self.passwordVL, 5, 0, 1, 1)
        self.passwordVL_2 = QtWidgets.QVBoxLayout()
        self.passwordVL_2.setObjectName("passwordVL_2")
        self.passwordlbl_2 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordlbl_2.sizePolicy().hasHeightForWidth())
        self.passwordlbl_2.setSizePolicy(sizePolicy)
        self.passwordlbl_2.setStyleSheet("background-color: rgb(255, 235, 255);\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"border : 2px solid rgb(85, 0, 0);\n"
"\n"
"")
        self.passwordlbl_2.setObjectName("passwordlbl_2")
        self.passwordVL_2.addWidget(self.passwordlbl_2)
        self.gridLayout_2.addLayout(self.passwordVL_2, 6, 0, 1, 1)
        self.registerVL = QtWidgets.QVBoxLayout()
        self.registerVL.setObjectName("registerVL")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet("color : rgb(85, 0, 0);\n"
"font: 87 10pt \"Arial Black\";\n"
"background-color : rgb(203, 213, 214)")
        self.pushButton.setObjectName("pushButton")
        self.registerVL.addWidget(self.pushButton)
        self.gridLayout_2.addLayout(self.registerVL, 7, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 373, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TASK TRACK KAYIT"))
        self.userRegFormlbl.setText(_translate("MainWindow", "Kullanıcı Kayıt Formu"))
        self.userNamelbl.setText(_translate("MainWindow", "Kullanıcı Adı :"))
        self.maillbl.setText(_translate("MainWindow", "E-Posta Adresi :"))
        self.passwordlbl.setText(_translate("MainWindow", "Şifre :"))
        self.pushButton.setText(_translate("MainWindow", "Kayıt Ol"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
