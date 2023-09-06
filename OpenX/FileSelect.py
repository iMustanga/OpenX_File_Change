# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FileSelect.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1374, 781)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.select_input = QtWidgets.QPushButton(MainWindow)
        self.select_input.setGeometry(QtCore.QRect(60, 90, 271, 41))
        self.select_input.setStyleSheet("border:2px solid rgb(85, 87, 83);\n"
"background-color: rgb(186, 189, 182);\n"
"border-radius:10px")
        self.select_input.setObjectName("select_input")
        self.show_input = QtWidgets.QLineEdit(MainWindow)
        self.show_input.setGeometry(QtCore.QRect(360, 90, 541, 41))
        self.show_input.setStyleSheet("border:2px solid rgb(186,186,186);\n"
"border-radius:10px")
        self.show_input.setText("")
        self.show_input.setObjectName("show_input")
        self.select_output = QtWidgets.QPushButton(MainWindow)
        self.select_output.setGeometry(QtCore.QRect(60, 260, 271, 41))
        self.select_output.setStyleSheet("border:2px solid rgb(85, 87, 83);\n"
"background-color: rgb(186, 189, 182);\n"
"border-radius:10px")
        self.select_output.setObjectName("select_output")
        self.textEdit_2 = QtWidgets.QTextEdit(MainWindow)
        self.textEdit_2.setGeometry(QtCore.QRect(350, 180, 221, 41))
        self.textEdit_2.setStyleSheet("border:0px solid rgb(186,186,186);\n"
"background-color: rgb(243, 243, 243);\n"
"border-radius:10px")
        self.textEdit_2.setObjectName("textEdit_2")
        self.show_output = QtWidgets.QLineEdit(MainWindow)
        self.show_output.setGeometry(QtCore.QRect(350, 260, 541, 41))
        self.show_output.setStyleSheet("border:2px solid rgb(186,186,186);\n"
"border-radius:10px")
        self.show_output.setText("")
        self.show_output.setObjectName("show_output")
        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(1000, 580, 291, 41))
        self.pushButton.setStyleSheet("border:2px solid rgb(85, 87, 83);\n"
"background-color: rgb(190, 221, 255);\n"
"border-radius:10px\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.new_filename = QtWidgets.QLineEdit(MainWindow)
        self.new_filename.setGeometry(QtCore.QRect(350, 420, 541, 41))
        self.new_filename.setStyleSheet("border:2px solid rgb(186,186,186);\n"
"border-radius:10px")
        self.new_filename.setText("")
        self.new_filename.setObjectName("new_filename")
        self.select_folder = QtWidgets.QPushButton(MainWindow)
        self.select_folder.setGeometry(QtCore.QRect(50, 600, 271, 41))
        self.select_folder.setStyleSheet("border:2px solid rgb(85, 87, 83);\n"
"background-color: rgb(186, 189, 182);\n"
"border-radius:10px")
        self.select_folder.setObjectName("select_folder")
        self.comboBox = QtWidgets.QComboBox(MainWindow)
        self.comboBox.setGeometry(QtCore.QRect(340, 600, 541, 41))
        self.comboBox.setStyleSheet("border:2px solid rgb(186,186,186);\n"
"border-radius:10px")
        self.comboBox.setObjectName("comboBox")
        self.open_soft = QtWidgets.QPushButton(MainWindow)
        self.open_soft.setGeometry(QtCore.QRect(1000, 410, 291, 41))
        self.open_soft.setStyleSheet("border:2px solid rgb(85, 87, 83);\n"
"background-color: rgb(190, 221, 255);\n"
"border-radius:10px\n"
"")
        self.open_soft.setObjectName("open_soft")
        self.carmaker = QtWidgets.QPushButton(MainWindow)
        self.carmaker.setGeometry(QtCore.QRect(1000, 660, 291, 41))
        self.carmaker.setStyleSheet("border:2px solid rgb(85, 87, 83);\n"
"background-color: rgb(190, 221, 255);\n"
"border-radius:10px\n"
"")
        self.carmaker.setObjectName("carmaker")
        self.show_carmaker = QtWidgets.QLineEdit(MainWindow)
        self.show_carmaker.setGeometry(QtCore.QRect(340, 670, 541, 41))
        self.show_carmaker.setStyleSheet("border:2px solid rgb(186,186,186);\n"
"border-radius:10px")
        self.show_carmaker.setText("")
        self.show_carmaker.setObjectName("show_carmaker")
        self.carmaker_input = QtWidgets.QPushButton(MainWindow)
        self.carmaker_input.setGeometry(QtCore.QRect(50, 670, 271, 41))
        self.carmaker_input.setStyleSheet("border:2px solid rgb(85, 87, 83);\n"
"background-color: rgb(186, 189, 182);\n"
"border-radius:10px")
        self.carmaker_input.setObjectName("carmaker_input")
        self.frame = QtWidgets.QFrame(MainWindow)
        self.frame.setGeometry(QtCore.QRect(990, 30, 311, 211))
        self.frame.setStyleSheet("border-image: url(:/DSXW/DSXW.png);\n"
"border-image: url(:/DSXW/DSXW.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.blank = QtWidgets.QPushButton(MainWindow)
        self.blank.setGeometry(QtCore.QRect(20, 30, 901, 131))
        self.blank.setStyleSheet("border:5px solid rgb(186,186,186);\n"
"background-color: rgb(243, 243, 243);\n"
"border-radius:25px")
        self.blank.setText("")
        self.blank.setObjectName("blank")
        self.blank_3 = QtWidgets.QPushButton(MainWindow)
        self.blank_3.setGeometry(QtCore.QRect(20, 550, 901, 191))
        self.blank_3.setStyleSheet("border:5px solid rgb(186,186,186);\n"
"border-radius:25px")
        self.blank_3.setText("")
        self.blank_3.setObjectName("blank_3")
        self.blank_4 = QtWidgets.QPushButton(MainWindow)
        self.blank_4.setGeometry(QtCore.QRect(20, 370, 901, 131))
        self.blank_4.setStyleSheet("border:5px solid rgb(186,186,186);\n"
"border-radius:25px")
        self.blank_4.setText("")
        self.blank_4.setObjectName("blank_4")
        self.blank_2 = QtWidgets.QPushButton(MainWindow)
        self.blank_2.setGeometry(QtCore.QRect(20, 200, 901, 131))
        self.blank_2.setStyleSheet("border:5px solid rgb(186,186,186);\n"
"border-radius:25px")
        self.blank_2.setText("")
        self.blank_2.setObjectName("blank_2")
        self.select_folder_2 = QtWidgets.QPushButton(MainWindow)
        self.select_folder_2.setGeometry(QtCore.QRect(60, 420, 271, 41))
        self.select_folder_2.setStyleSheet("border:2px solid rgb(186,186,186);\n"
"border-radius:10px")
        self.select_folder_2.setObjectName("select_folder_2")
        self.textEdit_3 = QtWidgets.QTextEdit(MainWindow)
        self.textEdit_3.setGeometry(QtCore.QRect(350, 350, 221, 41))
        self.textEdit_3.setStyleSheet("border:0px solid rgb(186,186,186);\n"
"background-color: rgb(243, 243, 243);\n"
"border-radius:10px")
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(MainWindow)
        self.textEdit_4.setGeometry(QtCore.QRect(350, 530, 221, 41))
        self.textEdit_4.setStyleSheet("border:0px solid rgb(186,186,186);\n"
"background-color: rgb(243, 243, 243);\n"
"border-radius:10px")
        self.textEdit_4.setObjectName("textEdit_4")
        self.blank_5 = QtWidgets.QPushButton(MainWindow)
        self.blank_5.setGeometry(QtCore.QRect(970, 530, 351, 211))
        self.blank_5.setStyleSheet("border:5px solid rgb(186,186,186);\n"
"border-radius:25px")
        self.blank_5.setText("")
        self.blank_5.setObjectName("blank_5")
        self.textEdit_5 = QtWidgets.QTextEdit(MainWindow)
        self.textEdit_5.setGeometry(QtCore.QRect(1040, 510, 191, 41))
        self.textEdit_5.setStyleSheet("border:0px solid rgb(186,186,186);\n"
"background-color: rgb(243, 243, 243);\n"
"border-radius:10px")
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_6 = QtWidgets.QTextEdit(MainWindow)
        self.textEdit_6.setGeometry(QtCore.QRect(350, 10, 221, 41))
        self.textEdit_6.setStyleSheet("border:0px solid rgb(186,186,186);\n"
"background-color: rgb(243, 243, 243);\n"
"border-radius:10px")
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_7 = QtWidgets.QTextEdit(MainWindow)
        self.textEdit_7.setGeometry(QtCore.QRect(1050, 260, 191, 41))
        self.textEdit_7.setStyleSheet("border:0px solid rgb(186,186,186);\n"
"background-color: rgb(243, 243, 243);\n"
"border-radius:10px")
        self.textEdit_7.setObjectName("textEdit_7")
        self.blank_6 = QtWidgets.QPushButton(MainWindow)
        self.blank_6.setGeometry(QtCore.QRect(970, 280, 351, 211))
        self.blank_6.setStyleSheet("border:5px solid rgb(186,186,186);\n"
"border-radius:25px")
        self.blank_6.setText("")
        self.blank_6.setObjectName("blank_6")
        self.select_soft = QtWidgets.QPushButton(MainWindow)
        self.select_soft.setGeometry(QtCore.QRect(1000, 330, 291, 41))
        self.select_soft.setStyleSheet("border:2px solid rgb(85, 87, 83);\n"
"background-color: rgb(190, 221, 255);\n"
"border-radius:10px\n"
"")
        self.select_soft.setObjectName("select_soft")
        self.blank_6.raise_()
        self.blank_5.raise_()
        self.blank_3.raise_()
        self.blank_4.raise_()
        self.blank_2.raise_()
        self.blank.raise_()
        self.select_input.raise_()
        self.show_input.raise_()
        self.select_output.raise_()
        self.textEdit_2.raise_()
        self.show_output.raise_()
        self.pushButton.raise_()
        self.new_filename.raise_()
        self.select_folder.raise_()
        self.comboBox.raise_()
        self.open_soft.raise_()
        self.carmaker.raise_()
        self.show_carmaker.raise_()
        self.carmaker_input.raise_()
        self.frame.raise_()
        self.select_folder_2.raise_()
        self.textEdit_3.raise_()
        self.textEdit_4.raise_()
        self.textEdit_5.raise_()
        self.textEdit_6.raise_()
        self.textEdit_7.raise_()
        self.select_soft.raise_()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OpenX"))
        self.select_input.setText(_translate("MainWindow", "选择xosc文件"))
        self.select_output.setText(_translate("MainWindow", "选择打包后输出目录"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#2e3436;\">2.输出目录</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "转换为VTD格式（Linux）"))
        self.select_folder.setText(_translate("MainWindow", "选择车辆模型"))
        self.open_soft.setText(_translate("MainWindow", "打开Roadrunner软件"))
        self.carmaker.setText(_translate("MainWindow", "转换为Carmaker格式（Windows）"))
        self.carmaker_input.setText(_translate("MainWindow", "选择CarMaker工程目录"))
        self.select_folder_2.setText(_translate("MainWindow", "输入新文件名"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#2e3436;\">3.输出文件名</span></p></body></html>"))
        self.textEdit_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#2e3436;\">4.CarMaker</span></p></body></html>"))
        self.textEdit_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#2e3436;\">5.输出</span></p></body></html>"))
        self.textEdit_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#2e3436;\">1.输入文件</span></p></body></html>"))
        self.textEdit_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#2e3436;\">RoadRunner</span></p></body></html>"))
        self.select_soft.setText(_translate("MainWindow", "选择Roadrunner软件目录"))
import DSXW_rc
