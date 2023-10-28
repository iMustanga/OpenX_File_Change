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
        # 10.20增加选择文件夹功能
        self.carmaker_select_input_dir.clicked.connect(self.carmaker_input_dir_init)
        self.carmaker_select_output.clicked.connect(self.carmaker_output_init)
        self.to_carmaker.clicked.connect(self.carmaker_openx_change)
        self.carmaker_model_select.clicked.connect(self.model_update)

        self.carmaker_model_show.clear()
        carmaker_model = os.listdir(default_file.DEFAULT_CMAKER_MODEL_DIR)
        self.carmaker_model_show.addItems(carmaker_model)

        '''self.carmaker_vehicle_model_show.clear()
        self.carmaker_vehicle = os.listdir(default_file.DEFAULT_CMAKER_VEHICLE_MODELS_DIR)
        self.carmaker_vehicle_model_show.addItems(self.carmaker_vehicle)

        self.carmaker_sensor_show.clear()
        self.carmaker_sensor = os.listdir(default_file.DEFAULT_CMAKER_SENSOR_DIR)
        self.carmaker_sensor_show.addItems(self.carmaker_sensor)'''

    def carmaker_input_init(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileNames(None, "选取文件",
                                                                   default_file.DEFAULT_INPUT_DATABASE,
                                                                   "xosc Files(*.xosc)")
        self.carmaker_input_dir = fileName
        self.carmaker_show_input.setText(str(fileName))

    # 10.20增加选择文件夹功能
    def carmaker_input_dir_init(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(None, "请选择文件夹路径",
                                                               default_file.DEFAULT_INPUT_DATABASE)
        # 获取directory文件夹下所有xosc文件路径
        file_list = Path(directory).glob('**/*.xosc')
        # 将所有xosc文件路径转换为字符串
        file_list = [str(i) for i in file_list]
        self.carmaker_input_dir = file_list
        self.carmaker_show_input.setText(directory)

    def carmaker_output_init(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(None, "请选择文件夹路径",
                                                               default_file.DEFAULT_OUTPUT_DIR)
        self.carmaker_output_dir = directory

        self.carmaker_show_output.setText(directory)

    # 10.20修改多文件
    def carmaker_openx_change(self):
        # 软件路径
        cur_dir = default_file.DEFAULT_CUR_DIR
        # 输入路径，文件名，对列表进行遍历
        for i in range(len(self.carmaker_input_dir)):
            input_dir, file_name = os.path.split(self.carmaker_input_dir[i])
            file_name, _ = os.path.splitext(file_name)
            model_name = self.carmaker_model_show.currentText()
            cm_utils = CarMakerUtils(cur_dir=cur_dir,
                                     cmaker_dir=self.carmaker_output_dir,
                                     file_name=file_name,
                                     input_dir=input_dir)
            cm_utils.carmaker_process(model_name=model_name)

    def model_update(self):
        self.carmaker_model_show.clear()
        carmaker_model = os.listdir(default_file.DEFAULT_CMAKER_MODEL_DIR)
        self.carmaker_model_show.addItems(carmaker_model)


