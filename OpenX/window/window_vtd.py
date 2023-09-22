# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_vtd.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window_vtd(object):
    def setupUi(self, Window_vtd):
        Window_vtd.setObjectName("Window_vtd")
        Window_vtd.resize(1126, 937)
        Window_vtd.setAutoFillBackground(False)
        Window_vtd.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.gridLayout = QtWidgets.QGridLayout(Window_vtd)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 6, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 3, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem4 = QtWidgets.QSpacerItem(318, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.vtd_vehicle_model_select_2 = QtWidgets.QPushButton(Window_vtd)
        self.vtd_vehicle_model_select_2.setMinimumSize(QtCore.QSize(271, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.vtd_vehicle_model_select_2.setFont(font)
        self.vtd_vehicle_model_select_2.setStyleSheet("border:2px solid rgb(186,186,186);\n"
        "border-radius:10px")
        self.vtd_vehicle_model_select_2.setObjectName("vtd_vehicle_model_select_2")
        self.horizontalLayout_6.addWidget(self.vtd_vehicle_model_select_2)
        spacerItem5 = QtWidgets.QSpacerItem(368, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.blank_8 = QtWidgets.QPushButton(Window_vtd)
        self.blank_8.setMinimumSize(QtCore.QSize(330, 6))
        self.blank_8.setMaximumSize(QtCore.QSize(16777215, 6))
        self.blank_8.setStyleSheet("border:5px solid rgb(186,186,186);\n"
        "border-radius:25px")
        self.blank_8.setText("")
        self.blank_8.setObjectName("blank_8")
        self.horizontalLayout_8.addWidget(self.blank_8)
        self.vtd_vehicle_model_select_3 = QtWidgets.QPushButton(Window_vtd)
        self.vtd_vehicle_model_select_3.setMinimumSize(QtCore.QSize(271, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.vtd_vehicle_model_select_3.setFont(font)
        self.vtd_vehicle_model_select_3.setStyleSheet("border:2px solid rgb(186,186,186);\n"
        "border-radius:10px")
        self.vtd_vehicle_model_select_3.setObjectName("vtd_vehicle_model_select_3")
        self.horizontalLayout_8.addWidget(self.vtd_vehicle_model_select_3)
        self.blank_7 = QtWidgets.QPushButton(Window_vtd)
        self.blank_7.setMinimumSize(QtCore.QSize(330, 6))
        self.blank_7.setMaximumSize(QtCore.QSize(16777215, 6))
        self.blank_7.setStyleSheet("border:5px solid rgb(186,186,186);\n"
        "border-radius:25px")
        self.blank_7.setText("")
        self.blank_7.setObjectName("blank_7")
        self.horizontalLayout_8.addWidget(self.blank_7)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.vtd_input = QtWidgets.QPushButton(Window_vtd)
        self.vtd_input.setMinimumSize(QtCore.QSize(271, 41))
        self.vtd_input.setStyleSheet("QPushButton{\n"
        "border:2px solid rgb(85, 87, 83);\n"
        "background-color: rgb(186, 189, 182);\n"
        "border-radius:10px\n"
        "}\n"
        "QPushButton:pressed{\n"
        "border:2px solid rgb(85, 87, 83);\n"
        "background-color: rgb(92, 105, 107);\n"
        "border-radius:10px;\n"
        "}")
        self.vtd_input.setObjectName("vtd_input")
        self.horizontalLayout.addWidget(self.vtd_input)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem8)
        self.vtd_show_input = QtWidgets.QLineEdit(Window_vtd)
        self.vtd_show_input.setMinimumSize(QtCore.QSize(541, 41))
        self.vtd_show_input.setStyleSheet("border:2px solid rgb(186,186,186);\n"
        "border-radius:10px")
        self.vtd_show_input.setText("")
        self.vtd_show_input.setObjectName("vtd_show_input")
        self.horizontalLayout.addWidget(self.vtd_show_input)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem9)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.blank_14 = QtWidgets.QPushButton(Window_vtd)
        self.blank_14.setMinimumSize(QtCore.QSize(330, 6))
        self.blank_14.setMaximumSize(QtCore.QSize(16777215, 6))
        self.blank_14.setStyleSheet("border:5px solid rgb(186,186,186);\n"
        "border-radius:25px")
        self.blank_14.setText("")
        self.blank_14.setObjectName("blank_14")
        self.horizontalLayout_9.addWidget(self.blank_14)
        self.vtd_vehicle_model_select_4 = QtWidgets.QPushButton(Window_vtd)
        self.vtd_vehicle_model_select_4.setMinimumSize(QtCore.QSize(271, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.vtd_vehicle_model_select_4.setFont(font)
        self.vtd_vehicle_model_select_4.setStyleSheet("border:2px solid rgb(186,186,186);\n"
        "border-radius:10px")
        self.vtd_vehicle_model_select_4.setObjectName("vtd_vehicle_model_select_4")
        self.horizontalLayout_9.addWidget(self.vtd_vehicle_model_select_4)
        self.blank_13 = QtWidgets.QPushButton(Window_vtd)
        self.blank_13.setMinimumSize(QtCore.QSize(330, 6))
        self.blank_13.setMaximumSize(QtCore.QSize(16777215, 6))
        self.blank_13.setStyleSheet("border:5px solid rgb(186,186,186);\n"
        "border-radius:25px")
        self.blank_13.setText("")
        self.blank_13.setObjectName("blank_13")
        self.horizontalLayout_9.addWidget(self.blank_13)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.vtd_vehicle_model_select = QtWidgets.QPushButton(Window_vtd)
        self.vtd_vehicle_model_select.setMinimumSize(QtCore.QSize(271, 41))
        self.vtd_vehicle_model_select.setStyleSheet("QPushButton{\n"
        "border:2px solid rgb(186,186,186);\n"
        "background-color: rgb(250,250,250);\n"
        "border-radius:10px\n"
        "}\n"
        "QPushButton:pressed{\n"
        "border:2px solid rgb(85, 87, 83);\n"
        "background-color: rgb(211, 215, 207);\n"
        "border-radius:10px;\n"
        "}")
        self.vtd_vehicle_model_select.setObjectName("vtd_vehicle_model_select")
        self.horizontalLayout_2.addWidget(self.vtd_vehicle_model_select)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem11)
        self.vtd_vehicle_model_show = QtWidgets.QComboBox(Window_vtd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vtd_vehicle_model_show.sizePolicy().hasHeightForWidth())
        self.vtd_vehicle_model_show.setSizePolicy(sizePolicy)
        self.vtd_vehicle_model_show.setMinimumSize(QtCore.QSize(541, 41))
        self.vtd_vehicle_model_show.setStyleSheet("border:2px solid rgb(186,186,186);\n"
        "border-radius:10px")
        self.vtd_vehicle_model_show.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.vtd_vehicle_model_show.setObjectName("vtd_vehicle_model_show")
        self.horizontalLayout_2.addWidget(self.vtd_vehicle_model_show)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem12)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem13)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.blank_18 = QtWidgets.QPushButton(Window_vtd)
        self.blank_18.setMinimumSize(QtCore.QSize(330, 6))
        self.blank_18.setMaximumSize(QtCore.QSize(16777215, 6))
        self.blank_18.setStyleSheet("border:5px solid rgb(186,186,186);\n"
        "border-radius:25px")
        self.blank_18.setText("")
        self.blank_18.setObjectName("blank_18")
        self.horizontalLayout_10.addWidget(self.blank_18)
        self.vtd_vehicle_model_select_5 = QtWidgets.QPushButton(Window_vtd)
        self.vtd_vehicle_model_select_5.setMinimumSize(QtCore.QSize(271, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.vtd_vehicle_model_select_5.setFont(font)
        self.vtd_vehicle_model_select_5.setStyleSheet("border:2px solid rgb(186,186,186);\n"
        "border-radius:10px")
        self.vtd_vehicle_model_select_5.setObjectName("vtd_vehicle_model_select_5")
        self.horizontalLayout_10.addWidget(self.vtd_vehicle_model_select_5)
        self.blank_17 = QtWidgets.QPushButton(Window_vtd)
        self.blank_17.setMinimumSize(QtCore.QSize(330, 6))
        self.blank_17.setMaximumSize(QtCore.QSize(16777215, 6))
        self.blank_17.setStyleSheet("border:5px solid rgb(186,186,186);\n"
        "border-radius:25px")
        self.blank_17.setText("")
        self.blank_17.setObjectName("blank_17")
        self.horizontalLayout_10.addWidget(self.blank_17)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.vtd_sensor_select = QtWidgets.QPushButton(Window_vtd)
        self.vtd_sensor_select.setMinimumSize(QtCore.QSize(271, 41))
        self.vtd_sensor_select.setStyleSheet("QPushButton{\n"
        "border:2px solid rgb(186,186,186);\n"
        "background-color: rgb(250,250,250);\n"
        "border-radius:10px\n"
        "}\n"
        "QPushButton:pressed{\n"
        "border:2px solid rgb(85, 87, 83);\n"
        "background-color: rgb(211, 215, 207);\n"
        "border-radius:10px;\n"
        "}")
        self.vtd_sensor_select.setObjectName("vtd_sensor_select")
        self.horizontalLayout_3.addWidget(self.vtd_sensor_select)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem14)
        self.vtd_sensor_show = QtWidgets.QComboBox(Window_vtd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vtd_sensor_show.sizePolicy().hasHeightForWidth())
        self.vtd_sensor_show.setSizePolicy(sizePolicy)
        self.vtd_sensor_show.setMinimumSize(QtCore.QSize(541, 41))
        self.vtd_sensor_show.setStyleSheet("border:2px solid rgb(186,186,186);\n"
        "border-radius:10px")
        self.vtd_sensor_show.setObjectName("vtd_sensor_show")
        self.horizontalLayout_3.addWidget(self.vtd_sensor_show)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem15)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem16)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.blank_19 = QtWidgets.QPushButton(Window_vtd)
        self.blank_19.setMinimumSize(QtCore.QSize(330, 6))
        self.blank_19.setMaximumSize(QtCore.QSize(16777215, 6))
        self.blank_19.setStyleSheet("border:5px solid rgb(186,186,186);\n"
        "border-radius:25px")
        self.blank_19.setText("")
        self.blank_19.setObjectName("blank_19")
        self.horizontalLayout_11.addWidget(self.blank_19)
        self.vtd_vehicle_model_select_6 = QtWidgets.QPushButton(Window_vtd)
        self.vtd_vehicle_model_select_6.setMinimumSize(QtCore.QSize(271, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.vtd_vehicle_model_select_6.setFont(font)
        self.vtd_vehicle_model_select_6.setStyleSheet("border:2px solid rgb(186,186,186);\n"
        "border-radius:10px")
        self.vtd_vehicle_model_select_6.setObjectName("vtd_vehicle_model_select_6")
        self.horizontalLayout_11.addWidget(self.vtd_vehicle_model_select_6)
        self.blank_21 = QtWidgets.QPushButton(Window_vtd)
        self.blank_21.setMinimumSize(QtCore.QSize(330, 6))
        self.blank_21.setMaximumSize(QtCore.QSize(16777215, 6))
        self.blank_21.setStyleSheet("border:5px solid rgb(186,186,186);\n"
        "border-radius:25px")
        self.blank_21.setText("")
        self.blank_21.setObjectName("blank_21")
        self.horizontalLayout_11.addWidget(self.blank_21)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.vtd_select_output = QtWidgets.QPushButton(Window_vtd)
        self.vtd_select_output.setMinimumSize(QtCore.QSize(271, 41))
        self.vtd_select_output.setStyleSheet("QPushButton{\n"
        "border:2px solid rgb(85, 87, 83);\n"
        "background-color: rgb(186, 189, 182);\n"
        "border-radius:10px\n"
        "}\n"
        "QPushButton:pressed{\n"
        "border:2px solid rgb(85, 87, 83);\n"
        "background-color: rgb(92, 105, 107);\n"
        "border-radius:10px;\n"
        "}")
        self.vtd_select_output.setObjectName("vtd_select_output")
        self.horizontalLayout_4.addWidget(self.vtd_select_output)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem17)
        self.vtd_show_output = QtWidgets.QLineEdit(Window_vtd)
        self.vtd_show_output.setMinimumSize(QtCore.QSize(541, 41))
        self.vtd_show_output.setStyleSheet("border:2px solid rgb(186,186,186);\n"
        "border-radius:10px")
        self.vtd_show_output.setText("")
        self.vtd_show_output.setObjectName("vtd_show_output")
        self.horizontalLayout_4.addWidget(self.vtd_show_output)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem18)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem19)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem20 = QtWidgets.QSpacerItem(548, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem20)
        self.to_vtd = QtWidgets.QPushButton(Window_vtd)
        self.to_vtd.setMinimumSize(QtCore.QSize(291, 41))
        self.to_vtd.setStyleSheet("QPushButton{\n"
        "border:2px solid rgb(85, 87, 83);\n"
        "background-color: rgb(190, 221, 255);\n"
        "border-radius:10px\n"
        "}\n"
        "QPushButton:pressed{\n"
        "border:2px solid rgb(85, 87, 83);\n"
        "background-color: rgb(138, 164, 193);\n"
        "border-radius:10px;\n"
        "}")
        self.to_vtd.setObjectName("to_vtd")
        self.horizontalLayout_5.addWidget(self.to_vtd)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem21)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout, 1, 3, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem22, 3, 3, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem23, 1, 0, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem24, 2, 3, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem25, 1, 2, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem26, 1, 5, 1, 1)

        self.retranslateUi(Window_vtd)
        QtCore.QMetaObject.connectSlotsByName(Window_vtd)

    def retranslateUi(self, Window_vtd):
        _translate = QtCore.QCoreApplication.translate
        Window_vtd.setWindowTitle(_translate("Window_vtd", "VTD"))
        self.vtd_vehicle_model_select_2.setText(_translate("Window_vtd", "VTD"))
        self.vtd_vehicle_model_select_3.setText(_translate("Window_vtd", "1.选择输入文件"))
        self.vtd_input.setText(_translate("Window_vtd", "选择xosc文件"))
        self.vtd_vehicle_model_select_4.setText(_translate("Window_vtd", "2.选择车辆模型"))
        self.vtd_vehicle_model_select.setText(_translate("Window_vtd", "选择车辆模型"))
        self.vtd_vehicle_model_select_5.setText(_translate("Window_vtd", "3.选择传感器模型"))
        self.vtd_sensor_select.setText(_translate("Window_vtd", "选择传感器模型"))
        self.vtd_vehicle_model_select_6.setText(_translate("Window_vtd", "4.选择输出目录"))
        self.vtd_select_output.setText(_translate("Window_vtd", "选择打包后输出目录"))
        self.to_vtd.setText(_translate("Window_vtd", "转换为VTD格式（Linux）"))
from window import DSXW_rc
