import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import numpy as np
import shutil
import subprocess
from pathlib import Path

from window.window_main import Ui_MainWindow
from window.window_vtd import Ui_Window_vtd
from window.window_carmaker import Ui_window_carmaker
from window import window_main, window_vtd

from shutil import copyfile
from carmaker_utils import CarMakerUtils


# 2023.09.13 接入了CarMaker 转换程序API

# windows
DEFAULT_CUR_DIR = os.path.abspath(os.path.dirname(os.getcwd()))
DEFAULT_INPUT_DATABASE = os.path.abspath(os.path.dirname(os.getcwd())) + "\\database"
DEFAULT_OUTPUT_DIR = os.path.abspath(os.path.dirname(os.getcwd())) + "\\output"
DEFAULT_CMAKER_VEHICLE_MODELS_DIR = os.path.abspath(os.path.dirname(os.getcwd())) + "\\Carmaker_Vehicle"
DEFAULT_VTD_VEHICLE_MODELS_DIR = os.path.abspath(os.path.dirname(os.getcwd())) + "\\VTD_Vehicle"
DEFAULT_CMAKER_SENSOR_DIR = os.path.abspath(os.path.dirname(os.getcwd())) + "\\Carmaker_Sensor"
DEFAULT_VTD_SENSOR_DIR = os.path.abspath(os.path.dirname(os.getcwd())) + "\\VTD_Sensor"
DEFAULT_ROADRUNNER_SOFT_DIR = os.path.abspath(os.path.dirname(os.getcwd())) + "\\database\\soft_path.txt"

'''
# linux
DEFAULT_INPUT_DATABASE = os.path.abspath(os.path.dirname(os.getcwd())) + "/database"
DEFAULT_OUTPUT_DIR = os.path.abspath(os.path.dirname(os.getcwd())) + "/output"
DEFAULT_CMAKER_VEHICLE_MODELS_DIR = os.path.abspath(os.path.dirname(os.getcwd())) + "/Carmaker_Vehicle"
DEFAULT_VTD_VEHICLE_MODELS_DIR = os.path.abspath(os.path.dirname(os.getcwd())) + "/VTD_Vehicle"
DEFAULT_CMAKER_SENSOR_DIR = os.path.abspath(os.path.dirname(os.getcwd())) + "/Carmaker_Sensor"
DEFAULT_VTD_SENSOR_DIR = os.path.abspath(os.path.dirname(os.getcwd())) + "/VTD_Sensor"
DEFAULT_ROADRUNNER_SOFT_DIR = os.path.abspath(os.path.dirname(os.getcwd())) + "/database/soft_path.txt"
'''


class vtd_change(QtWidgets.QWidget, Ui_Window_vtd):
    vtd_inputs = []
    vtd_outputs = []
    def __init__(self):
        super(vtd_change, self).__init__()
        self.setupUi(self)
        self.setfun()



    def setfun(self):

        self.vtd_input.clicked.connect(self.vtd_input_file)
        self.vtd_select_output.clicked.connect(self.vtd_output_file)
        self.to_vtd.clicked.connect(self.vtd_openx_change)

        self.vtd_vehicle_model_show.clear()
        vtd_vehicle = os.listdir(DEFAULT_VTD_VEHICLE_MODELS_DIR)
        self.vtd_vehicle_model_show.addItems(vtd_vehicle)

        self.vtd_sensor_show.clear()
        vtd_sensor = os.listdir(DEFAULT_VTD_SENSOR_DIR)
        self.vtd_sensor_show.addItems(vtd_sensor)




    def vtd_input_file(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件",
                                                                   DEFAULT_INPUT_DATABASE,
                                                                   "All Files(*);;Text Files(*.txt)")
        vtd_change.vtd_inputs.clear()

        vtd_change.vtd_inputs.append(fileName)
        self.vtd_show_input.setText(fileName)

    def vtd_output_file(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(None, "请选择文件夹路径",
                                                               DEFAULT_OUTPUT_DIR)

        vtd_change.vtd_outputs.clear()
        vtd_change.vtd_outputs.append(directory)

        self.vtd_show_output.setText(directory)

    def vtd_openx_change(self):
        inputs = vtd_change.vtd_inputs
        outputs = vtd_change.vtd_outputs
        print(str(inputs))
        stri = '\n'
        s = []
        v = []
        line_s = []
        set_con = 0
        time_lis = []
        time_con = 0
        act_support_cont = 100
        time_arr = np.zeros((act_support_cont, act_support_cont))
        time_set = []
        veh_cont = 0
        act_cont = 0
        arr_con = 0
        act_set = 0

        m = 0
        n = 0

        set_in_m = 0
        set_in_n = 0
        set_out_m = 0
        set_out_n = 0

        out_m = 0
        out_n = 0

        name = Path(str(inputs)).stem
        # print(name)


        if not os.path.exists(stri.join(inputs)):
            # print("Please select input file!")
            msg_box = QMessageBox.information(QtWidgets.QWidget(), "Error", "Please select input file!")
        else:

            if not os.path.exists(stri.join(outputs)):
                # print("Please select output folder!")
                msg_box = QMessageBox.information(QtWidgets.QWidget(), "Error", "Please select output folder!")
            else:
                out_dirs = stri.join(outputs) + '/' + name + '_VTD'

                if not os.path.exists(out_dirs + '/OpenX'):
                    os.makedirs(out_dirs + '/OpenX')
                else:
                    shutil.rmtree(out_dirs + '/OpenX')
                    os.makedirs(out_dirs + '/OpenX')

                if not os.path.exists(out_dirs + '/VehicleModels'):
                    os.makedirs(out_dirs + '/VehicleModels')
                else:
                    shutil.rmtree(out_dirs + '/VehicleModels')
                    os.makedirs(out_dirs + '/VehicleModels')

                if not os.path.exists(out_dirs + '/Others'):
                    os.makedirs(out_dirs + '/Others')
                else:
                    shutil.rmtree(out_dirs + '/Others')
                    os.makedirs(out_dirs + '/Others')

                input_dir = stri.join(inputs)

                output_dir = out_dirs + '/OpenX' + '/' + name
                output_dir = output_dir + '.txt'

                output_list = out_dirs + '/OpenX' + '/'

                readme = open(out_dirs + '/' + 'readme.txt', mode='w')

                readme.write('一、roadrunner操作 \n')
                readme.write('1.需要在车辆设置界面将车辆主体名称命名为ego，车辆型号名称可以不作修改 \n \n')
                readme.write(
                    '2.加速场景的加速方式都可以选择，减速模式不可以选择加速度方式，其余时间或是长度方式都可以，但模式必须选择为线性“Liner”，其余模式VTD无法识别 \n \n')
                readme.write('3.roadrunner动作中目前只能够导入变道、变速两个动作 \n \n')
                readme.write('二、软件操作 \n')
                readme.write(
                    '1.软件使用：首先点击select file按钮，选取需要更改格式的xosc文件；随后点击select folder按钮，选择更改后xosc文件需要保存的位置；最后在new filename后的对话框输入新xosc的文件名；最终点击VTD按钮即可。 \n \n')
                readme.write(
                    '2.若需要导入车辆模型，需要在点击VTD按钮前点击vehicle Models选取车辆模型所在的文件夹，并在后面的下拉框内选择需要的车辆模型最终会将该文件写入到Vehicle Modles文件夹中 \n \n')
                readme.write(
                    '3.需要注意的是输入的新的xosc文件名必须与osgb以及xodr文件的文件名完全相同，否则会导致在读取osgb以及xodr文件时发生错误 \n \n')
                readme.write(
                    '4.需要在路径~/VIRES/VTD.2021.4/Data/Projects/Current/Databases下新建一个名为roadrunner的文件夹，并将osgb以及xodr文件存储在该路径下，否则会导致在读取osgb以及xodr文件时发生错误 \n \n')

                readme.close()

                file_input = open(input_dir, "r")

                for line in open(input_dir, "r"):

                    if 'SimulationTimeCondition' in line:
                        time_in = line.replace("<SimulationTimeCondition value=", "")
                        time_in = time_in.replace('\n', '')
                        time_in = time_in.replace(' ', '')
                        time_in = time_in.replace('rule="greaterThan"/>', "")
                        time_in = time_in.replace('"', '')
                        # print(time_in)


                        if "0.0000000000000000e+0" in time_in:
                            # print("time=0")
                            if arr_con == 1:
                                m = m + 1
                                set_in_m = m
                                arr_con = 0
                            # print(m)
                            n = 0

                        else:

                            time_arr[m][n] = time_in
                            n = n + 1
                            arr_con = 1
                        # print(time_arr)

                        # s.append(file_input.readline())
                        # print(time_lis)

                for line in open(input_dir, "r"):
                    if '<CatalogLocations/>' in line:
                        s.append('    <CatalogLocations>' + '\n')
                        s.append('        <VehicleCatalog>' + '\n')
                        s.append('            <Directory path="Distros/Current/Config/Players/Vehicles" />' + '\n')
                        s.append('        </VehicleCatalog>' + '\n')
                        s.append('        <ControllerCatalog>' + '\n')
                        s.append(
                            '            <Directory path="Distros/Current/Config/Players/driverCfg.xml" />' + '\n')
                        s.append('        </ControllerCatalog>' + '\n')
                        s.append('    </CatalogLocations>' + '\n')
                        line = next(file_input)

                    elif 'LogicFile' in line:
                        s.append('        <LogicFile filepath="Projects/Current/Databases/roadrunner/' + name + '.xodr"/>' + '\n')
                        line = next(file_input)

                    elif 'SceneGraphFile' in line:
                        s.append(
                            '        <SceneGraphFile filepath="Projects/Current/Databases/roadrunner/' + name + '.osgb"/>' + '\n')
                        line = next(file_input)

                    elif 'vehicleCategory' in line:
                        s.append('            <Vehicle name="Audi_A3_2009_black" vehicleCategory="car">' + '\n')
                        line = next(file_input)

                    elif '/Vehicle>' in line:
                        s.append('            </Vehicle>' + '\n')
                        s.append('            <ObjectController>' + '\n')
                        s.append('                <Controller name="DefaultDriver">' + '\n')
                        s.append('                    <Properties/>' + '\n')
                        s.append('                </Controller>' + '\n')
                        s.append('            </ObjectController>' + '\n')
                        line = next(file_input)

                    elif 'SimulationTimeCondition' in line:
                        time_mid = line.replace("<SimulationTimeCondition value=", "")
                        time_mid = time_mid.replace('\n', '')
                        time_mid = time_mid.replace(' ', '')
                        # global time_action
                        time_action = time_mid.replace('rule="greaterThan"/>', "")
                        s.append(file_input.readline())
                        # print(time_action)


                    elif 'GlobalGroup" maximumExecutionCount="1"' in line:
                        str_1 = line.replace("\n", "")
                        s.append('<!--' + str_1 + '\n')
                        set_con = 1
                        act_cont = act_cont + 1
                        line = next(file_input)

                    elif '         </StopTrigger>' in line:
                        str_1 = line.replace("\n", "")
                        s.append(str_1 + '-->' + '\n')
                        set_con = 0
                        line = next(file_input)

                    elif 'StoryboardElementStateCondition' in line:

                        if set_con == 0:
                            set_out_n = out_n
                            time_input = time_arr[out_m][out_n]
                            if time_input == 0:
                                out_m = out_m + 1
                                out_n = 0


                            if out_m > set_in_m:
                                out_m = 1
                                out_n = 1
                                act_set = act_set + 1
                                # print("act_set=1")

                            time_input = time_arr[out_m][out_n]
                            if time_input == -1:
                                out_n = out_n + 1
                            time_input = time_arr[out_m][out_n]

                            time_count = 0
                            time_arr[out_m][out_n] = -1
                            time_set = str(time_input)
                            print(time_set)
                            s.append(
                                "                                            <SimulationTimeCondition value=" + '"' + time_set + '"' + ' rule="greaterThan" />' + '\n')


                            out_n = out_n + 1
                            if out_m > 0 and out_n == 1:
                                out_m = out_m + 1
                                out_n = 0

                            line = next(file_input)
                        else:
                            s.append(file_input.readline())

                    else:
                        # line_s = file_input.readline()
                        s.append(file_input.readline())

                    # s.append(line_s)

                file_input.close()

                file_output = open(output_dir, "w")
                for line in s:
                    file_output.writelines(line)
                file_output.close()

                file_change_suffix = os.listdir(output_list)
                for filename in file_change_suffix:
                    portion = os.path.splitext(filename)
                    if portion[1] == '.txt':
                        newname = output_list + portion[0] + '.xosc'
                        filename = output_list + filename
                        os.rename(filename, newname)

                file_dir = self.vtd_vehicle_model_show.currentText()

                if len(file_dir) == 0:
                    # print("Please select vehicle model!")
                    msg_box = QMessageBox.information(QtWidgets.QWidget(), "Error",
                                                      "Please select vehicle model!")
                else:
                    cur_vehicle_model_name = DEFAULT_VTD_VEHICLE_MODELS_DIR + '/' + file_dir
                    out_vehicle_model_name = out_dirs + '/VehicleModels' + '/' + file_dir

                    copyfile(cur_vehicle_model_name, out_vehicle_model_name)

                sensor_model_name = self.vtd_sensor_show.currentText()

                if len(sensor_model_name) == 0:
                    msg_box = QMessageBox.information(QtWidgets.QWidget(), "Error",
                                                      "Please select sensor model!")
                else:
                    cur_sensor_model_name = DEFAULT_VTD_SENSOR_DIR + '/' + sensor_model_name
                    out_sensor_model_name = out_dirs + '/Others' + '/' + sensor_model_name

                    copyfile(cur_sensor_model_name, out_sensor_model_name)




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

        self.carmaker_vehicle_model_show.clear()
        self.carmaker_vehicle = os.listdir(DEFAULT_CMAKER_VEHICLE_MODELS_DIR)
        self.carmaker_vehicle_model_show.addItems(self.carmaker_vehicle)

        self.carmaker_sensor_show.clear()
        self.carmaker_sensor = os.listdir(DEFAULT_CMAKER_SENSOR_DIR)
        self.carmaker_sensor_show.addItems(self.carmaker_sensor)

    def carmaker_input_init(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件",
                                                                   DEFAULT_INPUT_DATABASE,
                                                                   "All Files(*);;Text Files(*.txt)")
        self.carmaker_input_dir = fileName

        self.carmaker_show_input.setText(fileName)

    def carmaker_output_init(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(None, "请选择文件夹路径",
                                                               DEFAULT_OUTPUT_DIR)
        self.carmaker_output_dir = directory

        self.carmaker_show_output.setText(directory)

    def carmaker_openx_change(self):
        # 软件路径
        cur_dir = DEFAULT_CUR_DIR
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


class window_main(QtWidgets.QWidget, Ui_MainWindow):
    soft_path = []
    def __init__(self):
        super(window_main, self).__init__()
        self.setupUi(self)
        self.openx_vtd_change.clicked.connect(self.show_vtd)
        self.openx_carmaker_change.clicked.connect(self.show_carmaker)
        self.select_software_dir.clicked.connect(self.get_soft_dir)
        self.open_software.clicked.connect(self.open_roadrunner)

        self.case_download_show.clear()
        openx_case = os.listdir(DEFAULT_INPUT_DATABASE)
        self.case_download_show.addItems(openx_case)

        self.report_show.clear()
        report = os.listdir(DEFAULT_CMAKER_VEHICLE_MODELS_DIR)
        self.report_show.addItems(report)

        self.range_show.clear()
        range = os.listdir(DEFAULT_OUTPUT_DIR)
        self.range_show.addItems(range)

    def show_vtd(self):
        self.vtd_window = vtd_change()
        self.vtd_window.show()

    def show_carmaker(self):
        self.carmaker_window = window_carmaker_change()
        self.carmaker_window.show()

    def get_soft_dir(self):
        stri = '\n'
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件",
                                                                   "")
        window_main.soft_path.clear()
        window_main.soft_path.append(fileName)
        # print(soft_path)
        file_softpath = open(DEFAULT_ROADRUNNER_SOFT_DIR, mode="w")
        file_softpath.truncate(0)
        file_softpath.writelines(window_main.soft_path)
        file_softpath.close()

    def open_roadrunner(self):
        stri = '\n'
        if not os.path.exists(DEFAULT_ROADRUNNER_SOFT_DIR):
            msg_box = QMessageBox.information(QtWidgets.QWidget(), "Error", "Please select RoadRunner software path!")
        else:
            soft_dir = []
            file_opensoft = open(DEFAULT_ROADRUNNER_SOFT_DIR, mode="r")
            soft_dir.append(file_opensoft.readline())
            file_opensoft.close()
            if not os.path.exists(stri.join(soft_dir)):
                msg_box = QMessageBox.information(QtWidgets.QWidget(), "Error",
                                                  "Please reload RoadRunner software path!")
            else:
                subprocess.Popen(soft_dir)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    Mainwindow = window_main()
    Mainwindow.show()
    sys.exit(app.exec_())

