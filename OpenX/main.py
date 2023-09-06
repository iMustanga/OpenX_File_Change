import pathlib
import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import numpy as np
import shutil
import subprocess
from FileSelect import Ui_MainWindow
import FileSelect
from shutil import copy, copyfile
import xml.etree.ElementTree as ET
import Xml_change_followtrajectory
import Xml_change_dur
import Xml_changetools
from carmaker_utils import CarMakerUtils

'''
# windows 
DEFAULT_INPUT_DATABASE = os.path.abspath(os.path.dirname(os.getcwd())) + "\\database"
DEFAULT_OUTPUT_DIR = os.path.abspath(os.path.dirname(os.getcwd())) + "\\output"
DEFAULT_CMAKER_VEHICLE_MODELS_DIR = os.path.abspath(os.path.dirname(os.getcwd())) + "\\Carmaker_Vehicle"
DEFAULT_ROADRUNNER_SOFT_DIR = os.path.abspath(os.path.dirname(os.getcwd())) + "\\database\\soft_path.txt"
'''

# linux
DEFAULT_INPUT_DATABASE = os.path.abspath(os.path.dirname(os.getcwd())) + "/database"
DEFAULT_OUTPUT_DIR = os.path.abspath(os.path.dirname(os.getcwd())) + "/output"
DEFAULT_CMAKER_VEHICLE_MODELS_DIR = os.path.abspath(os.path.dirname(os.getcwd())) + "/Carmaker_Vehicle"
DEFAULT_ROADRUNNER_SOFT_DIR = os.path.abspath(os.path.dirname(os.getcwd())) + "/database/soft_path.txt"


paths = []
inputs = []
outputs = []
select = []
soft_path = []
cmaker = []
name = []
# 2023.09.03
vehicle_model_name = []

str_1 = []
time_mid = []
time_action = []
time_count = 0


# 2023.09.02 所有路径初始化前都加了clear，避免重复选择导致的多行路径bug
def input_file(self):
    fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件",
                                                               DEFAULT_INPUT_DATABASE,
                                                               "All Files(*);;Text Files(*.txt)")
    paths.clear()
    inputs.clear()

    paths.append(fileName)
    inputs.append(fileName)
    ui.show_input.setText(fileName)


def output_file(self):
    directory = QtWidgets.QFileDialog.getExistingDirectory(None, "请选择文件夹路径",
                                                           DEFAULT_OUTPUT_DIR)
    paths.clear()
    outputs.clear()

    paths.append(directory)
    outputs.append(directory)
    ui.show_output.setText(directory)


def new_name(self):
    name_1 = ui.new_filename.text()
    name.clear()
    name.append(name_1)


def vehicle_models(self):
    # 2023.09.02 使用固定路径
    # directory = QtWidgets.QFileDialog.getExistingDirectory(None, "请选择文件夹路径",
    #                                                        DEFAULT_CMAKER_VEHICLE_MODELS_DIR)
    # vehicle_model_name.clear()
    #
    # select.append(directory)
    # str = '\n'
    # select_dir = str.join(select)

    ui.comboBox.clear()
    file_open = os.listdir(DEFAULT_CMAKER_VEHICLE_MODELS_DIR)
    ui.comboBox.addItems(file_open)


# 读取选择的vehicle_model的名字
def vehicle_models_change(self):
    vehicle_model_name_buf = ui.comboBox.currentText()
    vehicle_model_name.clear()

    vehicle_model_name.append(vehicle_model_name_buf)


def carmaker_input(self):
    # 2023.09.02
    directory = QtWidgets.QFileDialog.getExistingDirectory(None, "请选择文件夹路径",
                                                           "C:/CM_Projects")
    paths.clear()
    cmaker.clear()

    paths.append(directory)
    cmaker.append(directory)
    ui.show_carmaker.setText(directory)

def select_soft():
    stri = '\n'
    fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件",
                                                               "All Files(*);;Text Files(*.txt)")
    soft_path.clear()
    soft_path.append(fileName)
    # print(soft_path)
    file_softpath = open(DEFAULT_ROADRUNNER_SOFT_DIR, mode="w")
    file_softpath.truncate(0)
    file_softpath.writelines(soft_path)
    file_softpath.close()


def open_soft():
    stri = '\n'
    if not os.path.exists(DEFAULT_ROADRUNNER_SOFT_DIR):
        msg_box = QMessageBox.information(QtWidgets.QWidget(), "Error", "Please select RoadRunner software path!")
    else:
        soft_dir = []
        file_opensoft = open(DEFAULT_ROADRUNNER_SOFT_DIR, mode="r")
        soft_dir.append(file_opensoft.readline())
        file_opensoft.close()
        if not os.path.exists(stri.join(soft_dir)):
            msg_box = QMessageBox.information(QtWidgets.QWidget(), "Error", "Please reload RoadRunner software path!")
        else:
            subprocess.Popen(soft_dir)


def done_py(self):
    if not os.path(inputs).isfile("outputs.txt"):
        # if not os.path.isfile("paths.txt"):
        f = open("paths.txt", mode="w")
    else:
        f = open("paths.txt", mode="w")
    stri = '\n'
    f.write(stri.join(paths))
    f.close
    # print(inputs)
    # print(outputs)


def write(self):
    stri = '\n'
    input_dir = stri.join(inputs)

    output_dir = stri.join(outputs) + '/' + stri.join(name)
    # output_dir=output_dir + '/'
    # output_dir =output_dir + stri.join(name)
    output_dir = output_dir + '.txt'

    file = open(input_dir, "r")
    oldfile = file.read()
    file.close()

    file = open(output_dir, "w")
    file.write(oldfile)
    file.write(input_dir)
    file.close()


def vtd_change(self):
    stri = '\n'
    s = []
    v = []
    line_s = []
    set_con = 0
    time_lis = []
    time_con = 0
    act_support_cont = 5
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

    if not os.path.exists(stri.join(inputs)):
        # print("Please select input file!")
        msg_box = QMessageBox.information(QtWidgets.QWidget(), "Error", "Please select input file!")
    else:

        if not os.path.exists(stri.join(outputs)):
            # print("Please select output folder!")
            msg_box = QMessageBox.information(QtWidgets.QWidget(), "Error", "Please select output folder!")
        else:

            if len(name) == 0:
                # print("Please enter output file name!")
                msg_box = QMessageBox.information(QtWidgets.QWidget(), "Error", "Please enter output file name!")
            else:
                out_dirs = stri.join(outputs) + '/' + stri.join(name) + '_VTD'

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

                output_dir = out_dirs + '/OpenX' + '/' + stri.join(name)
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

                        if time_in == 0.0000000000000000e+0:
                            s = []
                        else:
                            time_lis.append(time_in)

                        if "0.0000000000000000e+0" in time_in:
                            # print("time=0")
                            if arr_con == 1:
                                m = m + 1
                                set_in_m = m
                                arr_con = 0
                            # print(m)
                            n = 0
                            # veh_cont = veh_cont + 1
                            # time_arr[m][n]=time_in
                        else:
                            # time_in = int(time_in)
                            # print(m)
                            # print(n)
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
                        s.append('            <Directory path="Distros/Current/Config/Players/driverCfg.xml" />' + '\n')
                        s.append('        </ControllerCatalog>' + '\n')
                        s.append('    </CatalogLocations>' + '\n')
                        line = next(file_input)

                    elif 'LogicFile' in line:
                        s.append('        <LogicFile filepath="Projects/Current/Databases/roadrunner/' + stri.join(
                            name) + '.xodr"/>' + '\n')
                        line = next(file_input)

                    elif 'SceneGraphFile' in line:
                        s.append('        <SceneGraphFile filepath="Projects/Current/Databases/roadrunner/' + stri.join(
                            name) + '.osgb"/>' + '\n')
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
                        # global time_count
                        # time_count = time_count + 1
                        # if time_count == 3:

                        # time_set = time_lis[time_con]
                        if set_con == 0:
                            set_out_n = out_n
                            time_input = time_arr[out_m][out_n]
                            if time_input == 0:
                                out_m = out_m + 1
                                out_n = 0
                            '''
                            if act_set == 1:
                                out_n = 0
                                out_m = out_m + 1
                            '''




                            if out_m > set_in_m:
                                out_m = 1
                                out_n = 1
                                act_set = act_set + 1
                                # print("act_set=1")


                            time_input = time_arr[out_m][out_n]
                            if time_input == -1:
                                out_n = out_n + 1
                            time_input = time_arr[out_m][out_n]
                            # print(out_m)
                            # print(out_n)
                            time_count = 0
                            time_arr[out_m][out_n]=-1
                            time_set = str(time_input)
                            # print(time_set)
                            s.append(
                                "                                            <SimulationTimeCondition value=" + '"' + time_set + '"' + ' rule="greaterThan" />' + '\n')
                            time_con = time_con + 1
                            veh_cont = veh_cont + 1

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

                file_dir = ui.comboBox.currentText()

                if len(file_dir) == 0:
                    # print("Please select vehicle model!")
                    msg_box = QMessageBox.information(QtWidgets.QWidget(), "Error",
                                                      "Please select vehicle model!")
                else:
                    cur_vehicle_model_name = DEFAULT_CMAKER_VEHICLE_MODELS_DIR + '/' + file_dir
                    # out_slect_dir = out_dirs + '/VehicleModels' + '/' + file_dir + '.txt'
                    out_vehicle_model_name = out_dirs + '/VehicleModels' + '/' + file_dir
                    output_list = out_dirs + '/VehicleModels' + '/'

                    copyfile(cur_vehicle_model_name, out_vehicle_model_name)

                    # print(select_dir)
                    # print(out_slect_dir)
                    '''

                    file_car_input = open(select_dir, "r")

                    for line in open(select_dir, "r"):
                        line_v = file_car_input.readline()
                        v.append(line_v)
                    file_car_input.close()

                    file_car_output = open(out_slect_dir, "w")
                    for line in v:
                        file_car_output.writelines(line)
                    file_car_output.close()

                    file_car_change_suffix = os.listdir(output_list)
                    for filename in file_car_change_suffix:
                        portion = os.path.splitext(filename)
                        if portion[1] == '.txt':
                            newname = output_list + portion[0] + ''
                            filename = output_list + filename
                            os.rename(filename, newname)
                    '''


def carmaker_change():
    input_dir_and_file = inputs[0]
    # 输入路径，旧文件名
    input_dir, old_file_name = os.path.split(input_dir_and_file)
    old_file_name, _ = os.path.splitext(old_file_name)
    # 输出路径
    output_dir = DEFAULT_OUTPUT_DIR
    # 当前选择的车辆模型名字
    cur_vehicle_model_name = vehicle_model_name[0]

    cm_utils = CarMakerUtils(cmaker_dir=cmaker[0],
                             new_file_name=name[0],
                             old_file_name=old_file_name,
                             input_dir=input_dir,
                             output_dir=output_dir)
    # 处理
    cm_utils.carmaker_process(vehicle_model_name=cur_vehicle_model_name)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Mainwindow = QMainWindow()
    ui = FileSelect.Ui_MainWindow()
    ui.setupUi(Mainwindow)
    Mainwindow.show()
    ui.select_input.clicked.connect(input_file)
    ui.select_output.clicked.connect(output_file)
    ui.select_folder.clicked.connect(vehicle_models)
    ui.new_filename.textEdited.connect(new_name)
    ui.carmaker_input.clicked.connect(carmaker_input)
    ui.pushButton.clicked.connect(vtd_change)
    ui.carmaker.clicked.connect(carmaker_change)
    ui.select_soft.clicked.connect(select_soft)
    ui.open_soft.clicked.connect(open_soft)
    # 2023.09.03
    ui.comboBox.currentIndexChanged.connect(vehicle_models_change)
    sys.exit(app.exec_())
