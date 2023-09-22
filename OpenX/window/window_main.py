# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1110, 822)
        MainWindow.setMaximumSize(QtCore.QSize(1666665, 166666))
        self.gridLayout_3 = QtWidgets.QGridLayout(MainWindow)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 7, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 5, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.case_download_show = QtWidgets.QListWidget(MainWindow)
        self.case_download_show.setMinimumSize(QtCore.QSize(0, 331))
        self.case_download_show.setObjectName("case_download_show")
        self.gridLayout_2.addWidget(self.case_download_show, 2, 0, 1, 1)
        self.case_down = QtWidgets.QPushButton(MainWindow)
        self.case_down.setMinimumSize(QtCore.QSize(281, 41))
        self.case_down.setStyleSheet("QPushButton{\n"
        "border:2px solid rgb(186,186,186);\n"
        "background-color: rgb(250,250,250);\n"
        "border-radius:10px\n"
        "}\n"
        "QPushButton:pressed{\n"
        "border:2px solid rgb(85, 87, 83);\n"
        "background-color: rgb(211, 215, 207);\n"
        "border-radius:10px;\n"
        "}")
        self.case_down.setObjectName("case_down")
        self.gridLayout_2.addWidget(self.case_down, 0, 0, 1, 1)
        self.report = QtWidgets.QPushButton(MainWindow)
        self.report.setMinimumSize(QtCore.QSize(281, 41))
        self.report.setStyleSheet("QPushButton{\n"
        "border:2px solid rgb(186,186,186);\n"
        "background-color: rgb(250,250,250);\n"
        "border-radius:10px\n"
        "}\n"
        "QPushButton:pressed{\n"
        "border:2px solid rgb(85, 87, 83);\n"
        "background-color: rgb(211, 215, 207);\n"
        "border-radius:10px;\n"
        "}")
        self.report.setObjectName("report")
        self.gridLayout_2.addWidget(self.report, 0, 2, 1, 1)
        self.range_show = QtWidgets.QListWidget(MainWindow)
        self.range_show.setObjectName("range_show")
        self.gridLayout_2.addWidget(self.range_show, 2, 4, 1, 1)
        self.report_show = QtWidgets.QListWidget(MainWindow)
        self.report_show.setObjectName("report_show")
        self.gridLayout_2.addWidget(self.report_show, 2, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 3, 1, 1)
        self.range = QtWidgets.QPushButton(MainWindow)
        self.range.setMinimumSize(QtCore.QSize(281, 41))
        self.range.setStyleSheet("QPushButton{\n"
        "border:2px solid rgb(186,186,186);\n"
        "background-color: rgb(250,250,250);\n"
        "border-radius:10px\n"
        "}\n"
        "QPushButton:pressed{\n"
        "border:2px solid rgb(85, 87, 83);\n"
        "background-color: rgb(211, 215, 207);\n"
        "border-radius:10px;\n"
        "}")
        self.range.setObjectName("range")
        self.gridLayout_2.addWidget(self.range, 0, 4, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 6, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem4, 4, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 5, 2, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.frame_3 = QtWidgets.QFrame(MainWindow)
        self.frame_3.setMinimumSize(QtCore.QSize(341, 211))
        self.frame_3.setMaximumSize(QtCore.QSize(341, 211))
        self.frame_3.setStyleSheet("border-image: url(:/DSXW/DSXW.png);\n"
        "border-image: url(:/DSXW/DSXW.png);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4.addWidget(self.frame_3)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.select_software_dir = QtWidgets.QPushButton(MainWindow)
        self.select_software_dir.setMinimumSize(QtCore.QSize(241, 41))
        self.select_software_dir.setMaximumSize(QtCore.QSize(16777215, 41))
        self.select_software_dir.setStyleSheet("QPushButton{\n"
        "border:2px solid rgb(85, 87, 83);\n"
        "background-color: rgb(255, 199, 125);\n"
        "border-radius:10px\n"
        "}\n"
        "QPushButton:pressed{\n"
        "border:2px solid rgb(85, 87, 83);\n"
        "background-color: rgb(193, 125, 17);\n"
        "border-radius:10px;\n"
        "}")
        self.select_software_dir.setObjectName("select_software_dir")
        self.verticalLayout_2.addWidget(self.select_software_dir)
        self.open_software = QtWidgets.QPushButton(MainWindow)
        self.open_software.setMinimumSize(QtCore.QSize(241, 41))
        self.open_software.setStyleSheet("QPushButton{\n"
        "border:2px solid rgb(85, 87, 83);\n"
        "background-color: rgb(255, 199, 125);\n"
        "border-radius:10px\n"
        "}\n"
        "QPushButton:pressed{\n"
        "border:2px solid rgb(85, 87, 83);\n"
        "background-color: rgb(193, 125, 17);\n"
        "border-radius:10px;\n"
        "}\n"
        "")
        self.open_software.setObjectName("open_software")
        self.verticalLayout_2.addWidget(self.open_software)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem8 = QtWidgets.QSpacerItem(318, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 1)
        self.horizontalLayout_4.setStretch(3, 1)
        self.horizontalLayout_4.setStretch(4, 1)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 4, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem9, 8, 2, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem10, 6, 4, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem11, 6, 3, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem12, 3, 2, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem13, 6, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem14)
        self.openx_vtd_change = QtWidgets.QPushButton(MainWindow)
        self.openx_vtd_change.setMinimumSize(QtCore.QSize(251, 41))
        self.openx_vtd_change.setStyleSheet("QPushButton{\n"
    "border:2px solid rgb(85, 87, 83);\n"
    "background-color: rgb(190, 221, 255);\n"
    "border-radius:10px\n"
    "}\n"
    "QPushButton:pressed{\n"
    "border:2px solid rgb(85, 87, 83);\n"
    "background-color: rgb(138, 164, 193);\n"
    "border-radius:10px;\n"
    "}")
        self.openx_vtd_change.setDefault(False)
        self.openx_vtd_change.setFlat(False)
        self.openx_vtd_change.setObjectName("openx_vtd_change")
        self.horizontalLayout_3.addWidget(self.openx_vtd_change)
        spacerItem15 = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem15)
        self.openx_carmaker_change = QtWidgets.QPushButton(MainWindow)
        self.openx_carmaker_change.setMinimumSize(QtCore.QSize(251, 41))
        self.openx_carmaker_change.setStyleSheet("QPushButton{\n"
    "border:2px solid rgb(85, 87, 83);\n"
    "background-color: rgb(190, 221, 255);\n"
    "border-radius:10px\n"
    "}\n"
    "QPushButton:pressed{\n"
    "border:2px solid rgb(85, 87, 83);\n"
    "background-color: rgb(138, 164, 193);\n"
    "border-radius:10px;\n"
    "}")
        self.openx_carmaker_change.setObjectName("openx_carmaker_change")
        self.horizontalLayout_3.addWidget(self.openx_carmaker_change)
        spacerItem16 = QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem16)
        self.openx_prescan_change = QtWidgets.QPushButton(MainWindow)
        self.openx_prescan_change.setMinimumSize(QtCore.QSize(251, 41))
        self.openx_prescan_change.setStyleSheet("QPushButton{\n"
    "border:2px solid rgb(85, 87, 83);\n"
    "background-color: rgb(190, 221, 255);\n"
    "border-radius:10px\n"
    "}\n"
    "QPushButton:pressed{\n"
    "border:2px solid rgb(85, 87, 83);\n"
    "background-color: rgb(138, 164, 193);\n"
    "border-radius:10px;\n"
    "}")
        self.openx_prescan_change.setObjectName("openx_prescan_change")
        self.horizontalLayout_3.addWidget(self.openx_prescan_change)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem17)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 2, 2, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem18, 6, 1, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem19, 1, 2, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem20, 0, 2, 1, 1)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OpenX"))
        self.case_down.setText(_translate("MainWindow", "案例下载次数统计"))
        self.report.setText(_translate("MainWindow", "测试报告获取"))
        self.range.setText(_translate("MainWindow", "测试里程"))
        self.select_software_dir.setText(_translate("MainWindow", "选择Roadrunner软件目录"))
        self.open_software.setText(_translate("MainWindow", "打开Roadrunner软件"))
        self.openx_vtd_change.setText(_translate("MainWindow", "OpenX-VTD格式转换"))
        self.openx_carmaker_change.setText(_translate("MainWindow", "OpenX-CarMaker格式转换"))
        self.openx_prescan_change.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.openx_prescan_change.setText(_translate("MainWindow", "OpenX-Prescan格式转换"))
from window import DSXW_rc
