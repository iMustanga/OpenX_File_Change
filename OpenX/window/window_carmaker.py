# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_carmaker.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_window_carmaker(object):
    def setupUi(self, window_carmaker):
        window_carmaker.setObjectName("window_carmaker")
        window_carmaker.resize(1133, 980)
        self.gridLayout = QtWidgets.QGridLayout(window_carmaker)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 19, 3, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.blank_7 = QtWidgets.QPushButton(window_carmaker)
        self.blank_7.setMinimumSize(QtCore.QSize(330, 6))
        self.blank_7.setMaximumSize(QtCore.QSize(16777215, 6))
        self.blank_7.setStyleSheet("border:5px solid rgb(186,186,186);\n"
        "border-radius:25px")
        self.blank_7.setText("")
        self.blank_7.setObjectName("blank_7")
        self.horizontalLayout_6.addWidget(self.blank_7)
        self.vtd_vehicle_model_select_3 = QtWidgets.QPushButton(window_carmaker)
        self.vtd_vehicle_model_select_3.setMinimumSize(QtCore.QSize(271, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.vtd_vehicle_model_select_3.setFont(font)
        self.vtd_vehicle_model_select_3.setStyleSheet("border:2px solid rgb(186,186,186);\n"
        "border-radius:10px")
        self.vtd_vehicle_model_select_3.setObjectName("vtd_vehicle_model_select_3")
        self.horizontalLayout_6.addWidget(self.vtd_vehicle_model_select_3)
        self.blank_8 = QtWidgets.QPushButton(window_carmaker)
        self.blank_8.setMinimumSize(QtCore.QSize(330, 6))
        self.blank_8.setMaximumSize(QtCore.QSize(16777215, 6))
        self.blank_8.setStyleSheet("border:5px solid rgb(186,186,186);\n"
        "border-radius:25px")
        self.blank_8.setText("")
        self.blank_8.setObjectName("blank_8")
        self.horizontalLayout_6.addWidget(self.blank_8)
        self.gridLayout.addLayout(self.horizontalLayout_6, 4, 3, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.blank_9 = QtWidgets.QPushButton(window_carmaker)
        self.blank_9.setMinimumSize(QtCore.QSize(330, 6))
        self.blank_9.setMaximumSize(QtCore.QSize(16777215, 6))
        self.blank_9.setStyleSheet("border:5px solid rgb(186,186,186);\n"
        "border-radius:25px")
        self.blank_9.setText("")
        self.blank_9.setObjectName("blank_9")
        self.horizontalLayout_7.addWidget(self.blank_9)
        self.vtd_vehicle_model_select_4 = QtWidgets.QPushButton(window_carmaker)
        self.vtd_vehicle_model_select_4.setMinimumSize(QtCore.QSize(271, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.vtd_vehicle_model_select_4.setFont(font)
        self.vtd_vehicle_model_select_4.setStyleSheet("border:2px solid rgb(186,186,186);\n"
        "border-radius:10px")
        self.vtd_vehicle_model_select_4.setObjectName("vtd_vehicle_model_select_4")
        self.horizontalLayout_7.addWidget(self.vtd_vehicle_model_select_4)
        self.blank_10 = QtWidgets.QPushButton(window_carmaker)
        self.blank_10.setMinimumSize(QtCore.QSize(330, 6))
        self.blank_10.setMaximumSize(QtCore.QSize(16777215, 6))
        self.blank_10.setStyleSheet("border:5px solid rgb(186,186,186);\n"
        "border-radius:25px")
        self.blank_10.setText("")
        self.blank_10.setObjectName("blank_10")
        self.horizontalLayout_7.addWidget(self.blank_10)
        self.gridLayout.addLayout(self.horizontalLayout_7, 8, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 10, 3, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.carmaker_vehicle_model_select = QtWidgets.QPushButton(window_carmaker)
        self.carmaker_vehicle_model_select.setMinimumSize(QtCore.QSize(271, 41))
        self.carmaker_vehicle_model_select.setStyleSheet("QPushButton{\n"
        "border:2px solid rgb(186,186,186);\n"
        "background-color: rgb(250,250,250);\n"
        "border-radius:10px\n"
        "}\n"
        "QPushButton:hover{\n"
        "border:2px solid rgb(186,186,186);\n"
        "background-color: rgb(240, 240, 240);\n"
        "border-radius:10px;}\n"
        "QPushButton:pressed{\n"
        "border:2px solid rgb(186,186,186);\n"
        "background-color: rgb(211, 215, 207);\n"
        "border-radius:10px;\n"
        "}")
        self.carmaker_vehicle_model_select.setObjectName("carmaker_vehicle_model_select")
        self.horizontalLayout_2.addWidget(self.carmaker_vehicle_model_select)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.carmaker_vehicle_model_show = QtWidgets.QComboBox(window_carmaker)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.carmaker_vehicle_model_show.sizePolicy().hasHeightForWidth())
        self.carmaker_vehicle_model_show.setSizePolicy(sizePolicy)
        self.carmaker_vehicle_model_show.setMinimumSize(QtCore.QSize(541, 41))
        self.carmaker_vehicle_model_show.setStyleSheet("border:2px solid rgb(186,186,186);\n"
        "background-color: rgb(255, 255, 255);\n"
        "border-radius:10px")
        self.carmaker_vehicle_model_show.setObjectName("carmaker_vehicle_model_show")
        self.horizontalLayout_2.addWidget(self.carmaker_vehicle_model_show)
        self.gridLayout.addLayout(self.horizontalLayout_2, 9, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 5, 6, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 5, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 14, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 6, 3, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 2, 3, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 5, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem9 = QtWidgets.QSpacerItem(318, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.vtd_vehicle_model_select_2 = QtWidgets.QPushButton(window_carmaker)
        self.vtd_vehicle_model_select_2.setMinimumSize(QtCore.QSize(271, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.vtd_vehicle_model_select_2.setFont(font)
        self.vtd_vehicle_model_select_2.setStyleSheet("border:2px solid rgb(186,186,186);\n"
        "border-radius:10px")
        self.vtd_vehicle_model_select_2.setObjectName("vtd_vehicle_model_select_2")
        self.horizontalLayout_5.addWidget(self.vtd_vehicle_model_select_2)
        spacerItem10 = QtWidgets.QSpacerItem(358, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)
        self.horizontalLayout_5.setStretch(2, 1)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 3, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.blank_12 = QtWidgets.QPushButton(window_carmaker)
        self.blank_12.setMinimumSize(QtCore.QSize(330, 6))
        self.blank_12.setMaximumSize(QtCore.QSize(16777215, 6))
        self.blank_12.setStyleSheet("border:5px solid rgb(186,186,186);\n"
        "border-radius:25px")
        self.blank_12.setText("")
        self.blank_12.setObjectName("blank_12")
        self.horizontalLayout_8.addWidget(self.blank_12)
        self.vtd_vehicle_model_select_5 = QtWidgets.QPushButton(window_carmaker)
        self.vtd_vehicle_model_select_5.setMinimumSize(QtCore.QSize(271, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.vtd_vehicle_model_select_5.setFont(font)
        self.vtd_vehicle_model_select_5.setStyleSheet("border:2px solid rgb(186,186,186);\n"
        "border-radius:10px")
        self.vtd_vehicle_model_select_5.setObjectName("vtd_vehicle_model_select_5")
        self.horizontalLayout_8.addWidget(self.vtd_vehicle_model_select_5)
        self.blank_11 = QtWidgets.QPushButton(window_carmaker)
        self.blank_11.setMinimumSize(QtCore.QSize(330, 6))
        self.blank_11.setMaximumSize(QtCore.QSize(16777215, 6))
        self.blank_11.setStyleSheet("border:5px solid rgb(186,186,186);\n"
        "border-radius:25px")
        self.blank_11.setText("")
        self.blank_11.setObjectName("blank_11")
        self.horizontalLayout_8.addWidget(self.blank_11)
        self.gridLayout.addLayout(self.horizontalLayout_8, 12, 3, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 11, 3, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 0, 3, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem13, 18, 3, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem14, 5, 2, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem15, 15, 3, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem16, 22, 3, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.carmaker_select_output = QtWidgets.QPushButton(window_carmaker)
        self.carmaker_select_output.setMinimumSize(QtCore.QSize(271, 41))
        self.carmaker_select_output.setStyleSheet("QPushButton{\n"
        "border:2px solid rgb(85, 87, 83);\n"
        "background-color: rgb(186, 189, 182);\n"
        "border-radius:10px\n"
        "}\n"
        "QPushButton:hover{\n"
        "border:2px solid rgb(85, 87, 83);\n"
        "background-color: rgb(175, 175, 175);\n"
        "border-radius:10px;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "border:2px solid rgb(85, 87, 83);\n"
        "background-color: rgb(92, 105, 107);\n"
        "border-radius:10px;\n"
        "}")
        self.carmaker_select_output.setObjectName("carmaker_select_output")
        self.horizontalLayout_4.addWidget(self.carmaker_select_output)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem17)
        self.carmaker_show_output = QtWidgets.QLineEdit(window_carmaker)
        self.carmaker_show_output.setMinimumSize(QtCore.QSize(541, 41))
        self.carmaker_show_output.setStyleSheet("border:2px solid rgb(186,186,186);\n"
        "background-color: rgb(255, 255, 255);\n"
        "border-radius:10px")
        self.carmaker_show_output.setText("")
        self.carmaker_show_output.setObjectName("carmaker_show_output")
        self.horizontalLayout_4.addWidget(self.carmaker_show_output)
        self.gridLayout.addLayout(self.horizontalLayout_4, 17, 3, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem18, 5, 5, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem19, 7, 3, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.carmaker_sensor_select = QtWidgets.QPushButton(window_carmaker)
        self.carmaker_sensor_select.setMinimumSize(QtCore.QSize(271, 41))
        self.carmaker_sensor_select.setStyleSheet("QPushButton{\n"
        "border:2px solid rgb(186,186,186);\n"
        "background-color: rgb(250,250,250);\n"
        "border-radius:10px\n"
        "}\n"
        "QPushButton:hover{\n"
        "border:2px solid rgb(186,186,186);\n"
        "background-color: rgb(240, 240, 240);\n"
        "border-radius:10px;}\n"
        "QPushButton:pressed{\n"
        "border:2px solid rgb(186,186,186);\n"
        "background-color: rgb(211, 215, 207);\n"
        "border-radius:10px;\n"
        "}")
        self.carmaker_sensor_select.setObjectName("carmaker_sensor_select")
        self.horizontalLayout_3.addWidget(self.carmaker_sensor_select)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem20)
        self.carmaker_sensor_show = QtWidgets.QComboBox(window_carmaker)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.carmaker_sensor_show.sizePolicy().hasHeightForWidth())
        self.carmaker_sensor_show.setSizePolicy(sizePolicy)
        self.carmaker_sensor_show.setMinimumSize(QtCore.QSize(541, 41))
        self.carmaker_sensor_show.setStyleSheet("border:2px solid rgb(186,186,186);\n"
        "background-color: rgb(255, 255, 255);\n"
        "border-radius:10px")
        self.carmaker_sensor_show.setObjectName("carmaker_sensor_show")
        self.horizontalLayout_3.addWidget(self.carmaker_sensor_show)
        self.gridLayout.addLayout(self.horizontalLayout_3, 13, 3, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.blank_13 = QtWidgets.QPushButton(window_carmaker)
        self.blank_13.setMinimumSize(QtCore.QSize(330, 6))
        self.blank_13.setMaximumSize(QtCore.QSize(16777215, 6))
        self.blank_13.setStyleSheet("border:5px solid rgb(186,186,186);\n"
        "border-radius:25px")
        self.blank_13.setText("")
        self.blank_13.setObjectName("blank_13")
        self.horizontalLayout_9.addWidget(self.blank_13)
        self.vtd_vehicle_model_select_6 = QtWidgets.QPushButton(window_carmaker)
        self.vtd_vehicle_model_select_6.setMinimumSize(QtCore.QSize(271, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.vtd_vehicle_model_select_6.setFont(font)
        self.vtd_vehicle_model_select_6.setStyleSheet("border:2px solid rgb(186,186,186);\n"
        "border-radius:10px")
        self.vtd_vehicle_model_select_6.setObjectName("vtd_vehicle_model_select_6")
        self.horizontalLayout_9.addWidget(self.vtd_vehicle_model_select_6)
        self.blank_14 = QtWidgets.QPushButton(window_carmaker)
        self.blank_14.setMinimumSize(QtCore.QSize(330, 6))
        self.blank_14.setMaximumSize(QtCore.QSize(16777215, 6))
        self.blank_14.setStyleSheet("border:5px solid rgb(186,186,186);\n"
        "border-radius:25px")
        self.blank_14.setText("")
        self.blank_14.setObjectName("blank_14")
        self.horizontalLayout_9.addWidget(self.blank_14)
        self.gridLayout.addLayout(self.horizontalLayout_9, 16, 3, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem21, 3, 3, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem22, 5, 1, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem23 = QtWidgets.QSpacerItem(548, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem23)
        self.to_carmaker = QtWidgets.QPushButton(window_carmaker)
        self.to_carmaker.setMinimumSize(QtCore.QSize(291, 41))
        self.to_carmaker.setStyleSheet("QPushButton{\n"
        "border:2px solid rgb(85, 87, 83);\n"
        "background-color: rgb(190, 221, 255);\n"
        "border-radius:10px\n"
        "}\n"
        "QPushButton:hover{\n"
        "border:2px solid rgb(85, 87, 83);\n"
        "background-color: rgb(170, 200, 230);\n"
        "border-radius:10px;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "border:2px solid rgb(85, 87, 83);\n"
        "background-color: rgb(138, 164, 193);\n"
        "border-radius:10px;\n"
        "}")
        self.to_carmaker.setObjectName("to_carmaker")
        self.horizontalLayout_10.addWidget(self.to_carmaker)
        spacerItem24 = QtWidgets.QSpacerItem(68, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem24)
        self.gridLayout.addLayout(self.horizontalLayout_10, 20, 3, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.carmaker_select_input = QtWidgets.QPushButton(window_carmaker)
        self.carmaker_select_input.setMinimumSize(QtCore.QSize(271, 41))
        self.carmaker_select_input.setStyleSheet("QPushButton{\n"
        "border:2px solid rgb(85, 87, 83);\n"
        "background-color: rgb(186, 189, 182);\n"
        "border-radius:10px\n"
        "}\n"
        "QPushButton:hover{\n"
        "border:2px solid rgb(85, 87, 83);\n"
        "background-color: rgb(175, 175, 175);\n"
        "border-radius:10px;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "border:2px solid rgb(85, 87, 83);\n"
        "background-color: rgb(92, 105, 107);\n"
        "border-radius:10px;\n"
        "}")
        self.carmaker_select_input.setObjectName("carmaker_select_input")
        self.horizontalLayout.addWidget(self.carmaker_select_input)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem25)
        self.carmaker_show_input = QtWidgets.QLineEdit(window_carmaker)
        self.carmaker_show_input.setMinimumSize(QtCore.QSize(541, 41))
        self.carmaker_show_input.setStyleSheet("border:2px solid rgb(186,186,186);\n"
        "background-color: rgb(255, 255, 255);\n"
        "border-radius:10px")
        self.carmaker_show_input.setText("")
        self.carmaker_show_input.setObjectName("carmaker_show_input")
        self.horizontalLayout.addWidget(self.carmaker_show_input)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 3, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem26, 21, 3, 1, 1)

        self.retranslateUi(window_carmaker)
        QtCore.QMetaObject.connectSlotsByName(window_carmaker)

    def retranslateUi(self, window_carmaker):
        _translate = QtCore.QCoreApplication.translate
        window_carmaker.setWindowTitle(_translate("window_carmaker", "CarMaker"))
        self.vtd_vehicle_model_select_3.setText(_translate("window_carmaker", "1.选择输入文件"))
        self.vtd_vehicle_model_select_4.setText(_translate("window_carmaker", "2.选择车辆模型"))
        self.carmaker_vehicle_model_select.setText(_translate("window_carmaker", "选择车辆模型"))
        self.vtd_vehicle_model_select_2.setText(_translate("window_carmaker", "CarMaker"))
        self.vtd_vehicle_model_select_5.setText(_translate("window_carmaker", "3.选择传感器模型"))
        self.carmaker_select_output.setText(_translate("window_carmaker", "输出到Carmaker工程目录"))
        self.carmaker_sensor_select.setText(_translate("window_carmaker", "选择传感器模型"))
        self.vtd_vehicle_model_select_6.setText(_translate("window_carmaker", "4.选择输出目录"))
        self.to_carmaker.setText(_translate("window_carmaker", "转换为Carmaker格式（Windows）"))
        self.carmaker_select_input.setText(_translate("window_carmaker", "选择xosc文件"))
