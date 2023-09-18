import os
import shutil
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from pathlib import Path
from window.window_carmaker import Ui_window_carmaker
from shutil import copyfile
import default_file
from carmaker_utils import CarMakerUtils

# 2023.09.18 封装到类 并独立为一个文件
# 2023.09.18 增加点击按钮更新车辆模型以及传感器模型的显示


class window_carmaker_change(QtWidgets.QWidget, Ui_window_carmaker):
    def __init__(self):
        super(window_carmaker_change, self).__init__()
        self.carmaker_input_dir = None
        self.carmaker_output_dir = None
        self.carmaker_vehicle = None
        self.carmaker_sensor = None
        self.setupUi(self)
        self.var_init()

    def var_init(self):
        self.carmaker_select_input.clicked.connect(self.carmaker_input_init)
        self.carmaker_select_output.clicked.connect(self.carmaker_output_init)
        self.to_carmaker.clicked.connect(self.carmaker_openx_change)
        self.carmaker_vehicle_model_select.clicked.connect(self.vehicle_update)
        self.carmaker_sensor_select.clicked.connect(self.sensor_update)

        self.carmaker_vehicle_model_show.clear()
        self.carmaker_vehicle = os.listdir(default_file.DEFAULT_CMAKER_VEHICLE_MODELS_DIR)
        self.carmaker_vehicle_model_show.addItems(self.carmaker_vehicle)

        self.carmaker_sensor_show.clear()
        self.carmaker_sensor = os.listdir(default_file.DEFAULT_CMAKER_SENSOR_DIR)
        self.carmaker_sensor_show.addItems(self.carmaker_sensor)

    def carmaker_input_init(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件",
                                                                   default_file.DEFAULT_INPUT_DATABASE,
                                                                   "All Files(*);;Text Files(*.txt)")
        self.carmaker_input_dir = fileName

        self.carmaker_show_input.setText(fileName)

    def carmaker_output_init(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(None, "请选择文件夹路径",
                                                               default_file.DEFAULT_OUTPUT_DIR)
        self.carmaker_output_dir = directory

        self.carmaker_show_output.setText(directory)

    def carmaker_openx_change(self):
        # 软件路径
        cur_dir = default_file.DEFAULT_CUR_DIR
        # 输入路径，文件名
        input_dir, file_name = os.path.split(self.carmaker_input_dir)
        file_name, _ = os.path.splitext(file_name)
        # 当前选择的vehicle_model
        vehicle_model_name = self.carmaker_vehicle_model_show.currentText()
        # 当前选择的sensor
        # sensor_model_name = self.carmaker_sensor_model_show_currentText()
        cm_utils = CarMakerUtils(cur_dir=cur_dir,
                                 cmaker_dir=self.carmaker_output_dir,
                                 file_name=file_name,
                                 input_dir=input_dir)

        cm_utils.carmaker_process(vehicle_model_name=vehicle_model_name)

    # 点击按钮更新车辆模型内容
    def vehicle_update(self):
        self.carmaker_vehicle_model_show.clear()
        carmaker_vehicle = os.listdir(default_file.DEFAULT_VTD_VEHICLE_MODELS_DIR)
        self.carmaker_vehicle_model_show.addItems(carmaker_vehicle)

    # 点击按钮更新传感器模型内容
    def sensor_update(self):
        self.carmaker_sensor_show.clear()
        carmaker_sensor = os.listdir(default_file.DEFAULT_VTD_SENSOR_DIR)
        self.carmaker_sensor_show.addItems(carmaker_sensor)


