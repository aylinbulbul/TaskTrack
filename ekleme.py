# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ekleme.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(415, 460)
        Dialog.setStyleSheet("background-color: rgb(255, 235, 255);\n"
"")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setStyleSheet("color : rgb(85, 0, 0);\n"
"font: 87 italic 12pt \"Segoe UI Black\";\n"
"background-color: rgb(255, 235, 255);\n"
"border : 2px solid rgb(85, 0, 0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setStyleSheet("color : rgb(85, 0, 0);\n"
"font: 87 italic 12pt \"Segoe UI Black\";\n"
"background-color: rgb(255, 235, 255);\n"
"border : 2px solid rgb(85, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 235, 255);\n"
"border : 2px solid rgb(85, 0, 0);\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setStyleSheet("color : rgb(85, 0, 0);\n"
"font: 87 italic 12pt \"Segoe UI Black\";\n"
"background-color: rgb(255, 235, 255);\n"
"border : 2px solid rgb(85, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 235, 255);\n"
"border : 2px solid rgb(85, 0, 0);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_5.addWidget(self.lineEdit_2)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setStyleSheet("color : rgb(85, 0, 0);\n"
"font: 87 italic 12pt \"Segoe UI Black\";\n"
"background-color: rgb(255, 235, 255);\n"
"border : 2px solid rgb(85, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.timeEdit = QtWidgets.QTimeEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeEdit.sizePolicy().hasHeightForWidth())
        self.timeEdit.setSizePolicy(sizePolicy)
        self.timeEdit.setStyleSheet("background-color: rgb(255, 235, 255);\n"
"border : 2px solid rgb(85, 0, 0);")
        self.timeEdit.setObjectName("timeEdit")
        self.verticalLayout_7.addWidget(self.timeEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet("background-color: rgb(226, 239, 220);\n"
"\n"
"color : rgb(85, 0, 0);\n"
"border : 2px solid rgb(85, 0, 0);\n"
"\n"
"font: 87 italic 12pt \"Segoe UI Black\";\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_8.addWidget(self.pushButton)
        self.verticalLayout_6.addLayout(self.verticalLayout_8)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "TASK TRACK"))
        self.label.setText(_translate("Dialog", " Bilgileri Doldurunuz"))
        self.label_2.setText(_translate("Dialog", "Başlık : "))
        self.label_3.setText(_translate("Dialog", "Açıklama :"))
        self.label_4.setText(_translate("Dialog", "Hatırlatma Saati : "))
        self.pushButton.setText(_translate("Dialog", "EKLE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
