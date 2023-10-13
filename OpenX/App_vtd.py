import os
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import numpy as np
import shutil
from pathlib import Path
from window.window_vtd import Ui_Window_vtd
from shutil import copyfile
import default_file
from threading import Thread

# 2023.09.18 封装到类 并独立为一个文件
# 2023.09.18 增加点击按钮更新车辆模型以及传感器模型的显示

class vtd_change(QtWidgets.QWidget, Ui_Window_vtd):

    vtd_inputs = []
    vtd_input = []
    vtd_outputs = []
    vtd_input_dir = []
    vtd_name = []
    vtd_outdir = []
    vtd_outdir_openx = []
    vtd_outdir_vehicle = []
    vtd_outdir_others = []
    veh_model_name = []
    sensor_model_name = []
    vtd_input_con = 0
    # 程序所支持的车辆/动作数量
    vtd_act_support = 100
    vtd_time_arr = np.zeros((vtd_act_support, vtd_act_support))

    def __init__(self):
        super(vtd_change, self).__init__()
        self.setupUi(self)
        self.setfun_vtd()

    # 设置各个按钮功能以及显示框初始功能
    def setfun_vtd(self):

        # 设置各个按钮功能
        self.vtd_input.clicked.connect(self.vtd_input_file)
        self.vtd_input_4.clicked.connect(self.vtd_select_input_dir)
        self.vtd_select_output.clicked.connect(self.vtd_output_file)
        # self.to_vtd.clicked.connect(self.vtd_openx_change)
        self.to_vtd.clicked.connect(self.vtd_ergodic)
        self.vtd_vehicle_model_select.clicked.connect(self.vehicle_update)
        self.vtd_sensor_select.clicked.connect(self.sensor_update)

        # 设置打开页面即进行车辆模型显示
        self.vtd_vehicle_model_show.clear()
        vtd_vehicle = os.listdir(default_file.DEFAULT_VTD_VEHICLE_MODELS_DIR)
        self.vtd_vehicle_model_show.addItems(vtd_vehicle)

        # 设置打开页面即进行传感器模型显示
        self.vtd_sensor_show.clear()
        vtd_sensor = os.listdir(default_file.DEFAULT_VTD_SENSOR_DIR)
        self.vtd_sensor_show.addItems(vtd_sensor)

    def vtd_ergodic(self):
        self.to_vtd.setEnabled(False)
        stri = '\n'

        size_input = np.size(vtd_change.vtd_inputs)
        print(size_input)


        if size_input > 1:
            file_name = os.path.basename(str(vtd_change.vtd_inputs[0][0]))
        else:
            file_name = os.path.basename(str(vtd_change.vtd_inputs))
        port = os.path.splitext(file_name)
        # print(port[1])


        # print(vtd_change.vtd_inputs)
        if 'xosc' in port[1]:

            if size_input > 1:
                print("size_mult")
                for i in range(size_input):
                    # print(i)
                    self.clear_vtd_dir()
                    vtd_change.vtd_name = Path(str(vtd_change.vtd_inputs[0][i])).stem
                    vtd_change.vtd_input.append(vtd_change.vtd_inputs[0][i])
                    vtd_change.vtd_input_dir = vtd_change.vtd_inputs[0][i]
                    name_por = os.path.basename(str(vtd_change.vtd_inputs[0][i]))
                    portion = os.path.splitext(name_por)
                    if 'xosc' in portion[1]:
                        self.vtd_openx_change()
                    else:
                        # print("error")
                        msg_box = QMessageBox.information(QtWidgets.QWidget(), default_file.DISPLAY_WARN,
                                                          default_file.DISPLAY_WARN_INPUT_FORMAT + str(vtd_change.vtd_inputs[0][i]))
                    # print(i)
            else:
                print("one_mult")
                self.clear_vtd_dir()
                vtd_change.vtd_name = Path(str(vtd_change.vtd_inputs[0][0])).stem
                vtd_change.vtd_input.append(vtd_change.vtd_inputs[0][0])
                vtd_change.vtd_input_dir = vtd_change.vtd_inputs[0][0]
                name_por = os.path.basename(str(vtd_change.vtd_inputs[0][0]))
                portion = os.path.splitext(name_por)
                if 'xosc' in portion[1]:
                    self.vtd_openx_change()
                else:
                    # print("error")
                    msg_box = QMessageBox.information(QtWidgets.QWidget(), default_file.DISPLAY_WARN,
                                                      default_file.DISPLAY_WARN_INPUT_FORMAT + str(
                                                          vtd_change.vtd_inputs[0][0]))

        elif port[1] == '':
            print("size_one")
            vtd_dir = os.listdir(stri.join(vtd_change.vtd_inputs) + '/')
            for name in vtd_dir:
                self.clear_vtd_dir()
                vtd_change.vtd_input_dir = stri.join(vtd_change.vtd_inputs) + '/' + name

                portion = os.path.splitext(name)
                vtd_change.vtd_name = portion[0]

                vtd_change.vtd_input = vtd_change.vtd_inputs

                if 'xosc' in portion[1]:
                    # print(vtd_change.vtd_name)
                    # new_thread = Thread(target=self.vtd_openx_change)
                    # new_thread.start()
                    self.vtd_openx_change()
                else:
                    # print("error")
                    msg_box = QMessageBox.information(QtWidgets.QWidget(), default_file.DISPLAY_WARN,
                                                      default_file.DISPLAY_WARN_INPUT_FORMAT + vtd_change.vtd_input_dir)
        else:
            msg_box = QMessageBox.information(QtWidgets.QWidget(), default_file.DISPLAY_WARN,
                                              default_file.DISPLAY_WARN_INPUT_FORMAT + str(
                                                  vtd_change.vtd_inputs[0][0]))
        self.clear_vtd_dir()
        self.to_vtd.setEnabled(True)


    # xosc文件修改主函数
    def vtd_openx_change(self):
        # print(vtd_change.vtd_name)
        # 获取所需要的各种路径及文件名
        self.get_vtd_dir()
        stri = '\n'

        # 判断输入以及输出文件是否正确输入
        # print(vtd_change.vtd_input)
        if not os.path.exists(stri.join(vtd_change.vtd_input)):
            msg_box = QMessageBox.information(QtWidgets.QWidget(), default_file.DISPLAY_WARN, default_file.DISPLAY_WARN_INPUT)
        else:

            if not os.path.exists(stri.join(vtd_change.vtd_outputs)):
                msg_box = QMessageBox.information(QtWidgets.QWidget(), default_file.DISPLAY_WARN, default_file.DISPLAY_WARN_OUTPUT)
            else:
                # print("start")
                # 新建对应文件夹
                self.vtd_make_new_dirs()
                # 编写readme文件
                self.vtd_readme()
                # 输出新xosc文件
                self.write_vtd_output_xosc()
                # 将车辆模型复制到对应文件夹内
                self.copy_vehicle_model()
                # 将传感器模型复制到对应文件夹内
                self.copy_sensor_model()
                # 检查输出文件是否齐全
                self.out_check()

        # 清空处理过程中写入的数据
        self.clear_vtd_dir()

        # print(vtd_change.vtd_name)

    # 获取输入文件路径
    def vtd_input_file(self):
        self.vtd_input.setEnabled(False)
        self.vtd_input_4.setEnabled(False)
        stri = '\n'

        # fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件",default_file.DEFAULT_INPUT_DATABASE,"All Files(*);;Text Files(*.txt)")
        # fileName = QtWidgets.QFileDialog.getExistingDirectory(None, "请选择文件夹路径", default_file.DEFAULT_INPUT_DATABASE)
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileNames(None, "选取文件", default_file.DEFAULT_INPUT_DATABASE,"All Files(*);;Text Files(*.txt)")
        vtd_change.vtd_inputs.clear()
        vtd_change.vtd_inputs.append(fileName)
        scu = np.size(vtd_change.vtd_inputs)
        if scu > 1:
            out_name = []
            out_name = fileName[0]
            for i in range(scu-1):
                out_name = out_name + ' + ' + os.path.basename(fileName[i+1])
            # print(out_name)
            # self.vtd_show_input.setText(str(fileName[0]))
            self.vtd_show_input.setText(out_name)
        else:
            # print(vtd_change.vtd_inputs)
            # print(fileName)
            self.vtd_show_input.setText(fileName[0])

        self.vtd_input.setEnabled(True)
        self.vtd_input_4.setEnabled(True)

    def vtd_select_input_dir(self):
        self.vtd_input.setEnabled(False)
        self.vtd_input_4.setEnabled(False)


        dir_name = QtWidgets.QFileDialog.getExistingDirectory(None, "请选择文件夹路径", default_file.DEFAULT_INPUT_DATABASE)
        vtd_change.vtd_inputs.clear()
        vtd_change.vtd_inputs.append(dir_name)
        self.vtd_show_input.setText(dir_name)

        self.vtd_input.setEnabled(True)
        self.vtd_input_4.setEnabled(True)


    # 获取输出文件夹路径
    def vtd_output_file(self):
        self.vtd_select_output.setEnabled(False)
        directory = QtWidgets.QFileDialog.getExistingDirectory(None, "请选择文件夹路径",
                                                               default_file.DEFAULT_OUTPUT_DIR)

        vtd_change.vtd_outputs.clear()
        vtd_change.vtd_outputs.append(directory)
        self.vtd_show_output.setText(directory)
        self.vtd_select_output.setEnabled(True)


    # 获取所需要的各种路径及文件名
    def get_vtd_dir(self):
        stri = '\n'
        # vtd_change.vtd_name = Path(str(vtd_change.vtd_inputs)).stem
        vtd_change.vtd_outdir = stri.join(vtd_change.vtd_outputs) + '/' + vtd_change.vtd_name + '_VTD'
        # print(vtd_change.vtd_outdir)
        vtd_change.vtd_outdir_openx = vtd_change.vtd_outdir + "/OpenX"
        vtd_change.vtd_outdir_vehicle = vtd_change.vtd_outdir + "/VehicleModels"
        vtd_change.vtd_outdir_others = vtd_change.vtd_outdir + "/Others"
        vtd_change.veh_model_name = self.vtd_vehicle_model_show.currentText()
        vtd_change.sensor_model_name = self.vtd_sensor_show.currentText()

    def clear_vtd_dir(self):
        vtd_change.vtd_name = []
        vtd_change.vtd_outdir = []
        vtd_change.vtd_outdir_openx = []
        vtd_change.vtd_outdir_vehicle = []
        vtd_change.vtd_outdir_others = []
        vtd_change.veh_model_name = []
        vtd_change.sensor_model_name = []
        vtd_change.vtd_input = []


    # 新建对应文件夹
    def vtd_make_new_dirs(self):
        if not os.path.exists(vtd_change.vtd_outdir_openx):
            os.makedirs(vtd_change.vtd_outdir_openx)
            # print(vtd_change.vtd_outdir)
        else:
            shutil.rmtree(vtd_change.vtd_outdir_openx)
            os.makedirs(vtd_change.vtd_outdir_openx)
            # print(vtd_change.vtd_outdir)

        if not os.path.exists(vtd_change.vtd_outdir_vehicle):
            os.makedirs(vtd_change.vtd_outdir_vehicle)
        else:
            shutil.rmtree(vtd_change.vtd_outdir_vehicle)
            os.makedirs(vtd_change.vtd_outdir_vehicle)

        if not os.path.exists(vtd_change.vtd_outdir_others):
            os.makedirs(vtd_change.vtd_outdir_others)
        else:
            shutil.rmtree(vtd_change.vtd_outdir_others)
            os.makedirs(vtd_change.vtd_outdir_others)

    # 将车辆模型复制到对应文件夹内
    def copy_vehicle_model(self):
        #veh_model_name = self.vtd_vehicle_model_show.currentText()

        if len(vtd_change.veh_model_name) == 0:
            # print("Please select vehicle model!")
            msg_box = QMessageBox.information(QtWidgets.QWidget(), default_file.DISPLAY_WARN,
                                              default_file.DISPLAY_WARN_VEHICLE)
        else:
            cur_vehicle_model_name = default_file.DEFAULT_VTD_VEHICLE_MODELS_DIR+ '/' + vtd_change.veh_model_name
            out_vehicle_model_name = vtd_change.vtd_outdir_vehicle + '/' + vtd_change.veh_model_name

            copyfile(cur_vehicle_model_name, out_vehicle_model_name)

    # 将传感器模型复制到对应文件夹内
    def copy_sensor_model(self):
        # sensor_model_name = self.vtd_sensor_show.currentText()

        if len(vtd_change.sensor_model_name) == 0:
            msg_box = QMessageBox.information(QtWidgets.QWidget(), default_file.DISPLAY_WARN,
                                              default_file.DISPLAY_WARN_SENSOR)
        else:
            cur_sensor_model_name = default_file.DEFAULT_VTD_SENSOR_DIR + '/' + vtd_change.sensor_model_name
            out_sensor_model_name = vtd_change.vtd_outdir_others + '/' + vtd_change.sensor_model_name

            copyfile(cur_sensor_model_name, out_sensor_model_name)

    # 点击按钮更新车辆模型内容
    def vehicle_update(self):
        self.vtd_vehicle_model_show.clear()
        vtd_vehicle = os.listdir(default_file.DEFAULT_VTD_VEHICLE_MODELS_DIR)
        self.vtd_vehicle_model_show.addItems(vtd_vehicle)

    # 点击按钮更新传感器模型内容
    def sensor_update(self):
        self.vtd_sensor_show.clear()
        vtd_sensor = os.listdir(default_file.DEFAULT_VTD_SENSOR_DIR)
        self.vtd_sensor_show.addItems(vtd_sensor)

    # 编写readme文件
    def vtd_readme(self):
        vtd_readme_file = open(vtd_change.vtd_outdir + '/' + 'VTD_README.txt', mode='w')

        vtd_readme_file.write('一、roadrunner操作 \n')
        vtd_readme_file.write('1.需要在车辆设置界面将车辆主体名称命名为ego，车辆型号名称可以不作修改 \n \n')
        vtd_readme_file.write(
            '2.加速场景的加速方式都可以选择，减速模式不可以选择加速度方式，其余时间或是长度方式都可以，但模式必须选择为线性“Liner”，其余模式VTD无法识别 \n \n')
        vtd_readme_file.write('3.roadrunner动作中目前只能够导入变道、变速两个动作 \n \n')
        vtd_readme_file.write('二、软件操作 \n')
        vtd_readme_file.write(
            "1.软件使用：首先点击‘选择xosc文件’按钮，选取需要更改格式的xosc文件；随后点击‘选择打包后输出目录’按钮，选择更改后xosc文件需要保存的位置；最后点击'转换为VTD格式'按钮即可。 \n \n")
        vtd_readme_file.write(
            "2.导入车辆模型时，软件默认选择默认文件夹下的第一个模型，若需要更改车辆模型时，需要将所需文件放入默认路径下，点击左侧‘选择车辆模型’按钮更新下拉框的内容，并在后面的下拉框内选择需要的车辆模型，传感器模型同理。 \n \n")
        vtd_readme_file.write(
            "3.需要注意的是输入的新的xosc文件名必须与osgb以及xodr文件的文件名完全相同，否则会导致在读取osgb以及xodr文件时发生错误 \n \n")
        vtd_readme_file.write(
            "4.需要在路径~/VIRES/VTD.2021.4/Data/Projects/Current/Databases下新建一个名为roadrunner的文件夹，并将osgb以及xodr文件存储在该路径下，否则会导致在读取osgb以及xodr文件时发生错误 \n \n")

        vtd_readme_file.close()

    # 输出检查
    def out_check(self):
        stri = '\n'
        if os.path.exists(vtd_change.vtd_outdir_openx + '/' + vtd_change.vtd_name + '.xosc'):
            if os.path.exists(vtd_change.vtd_outdir_vehicle + '/' + vtd_change.veh_model_name):
                if os.path.exists(vtd_change.vtd_outdir_others + '/' + vtd_change.sensor_model_name):
                    print("sucess")
                    # msg_box = QMessageBox.information(QtWidgets.QWidget(), default_file.DISPLAY_SUCESS,
                    #                                   default_file.DiSPLAY_SUCESS_XOSC + vtd_change.vtd_outdir)
                else:
                    msg_box = QMessageBox.information(QtWidgets.QWidget(), default_file.DISPLAY_WARN,
                                                      default_file.DISPLAY_WARN_OUT_SEN)
            else:
                msg_box = QMessageBox.information(QtWidgets.QWidget(), default_file.DISPLAY_WARN,
                                                 default_file.DISPLAY_WARN_OUT_VEH)
        else:
            msg_box = QMessageBox.information(QtWidgets.QWidget(), default_file.DISPLAY_WARN,
                                              default_file.DISPLAY_WARN_OUT_FILE)

    # 编写新的xosc文件
    def write_vtd_output_xosc(self):
        stri = '\n'

        new_xosc_content = []
        time_change_set = 0
        act_cont = 0
        arr_cond = 0
        act_set = 0
        in_m = 0
        in_n = 0
        in_m_cont = 0
        out_m = 0
        out_n = 0

        # vtd_change.vtd_input_dir = stri.join(vtd_change.vtd_inputs)
        output_dir = vtd_change.vtd_outdir_openx + '/' + vtd_change.vtd_name
        output_dir = output_dir + '.txt'
        output_list = vtd_change.vtd_outdir_openx + '/'

        # print(output_dir)

        # 读取输入xosc文件并修改内容
        file_input = open(vtd_change.vtd_input_dir, "r")

        # 读取文件内包含的动作时间信息
        for line in open(vtd_change.vtd_input_dir, "r"):

            if 'SimulationTimeCondition' in line:
                time_in = line.replace("<SimulationTimeCondition value=", "")
                time_in = time_in.replace('\n', '')
                time_in = time_in.replace(' ', '')
                time_in = time_in.replace('rule="greaterThan"/>', "")
                time_in = time_in.replace('"', '')
                # print(time_in)

                if "0.0000000000000000e+0" in time_in:

                    if arr_cond == 1:
                        in_m = in_m + 1
                        in_m_cont = in_m
                        arr_cond = 0

                    in_n = 0

                else:

                    vtd_change.vtd_time_arr[in_m][in_n] = time_in
                    in_n = in_n + 1
                    arr_cond = 1

        # 对就文件内内容进行逐行遍历，并对内容进行修改
        for line in open(vtd_change.vtd_input_dir, "r"):
            # 添加车辆模型以及驾驶员模型的数据库（数据库为VTD内自带）
            if '<CatalogLocations/>' in line:
                new_xosc_content.append('    <CatalogLocations>' + '\n')
                new_xosc_content.append('        <VehicleCatalog>' + '\n')
                new_xosc_content.append(
                    '            <Directory path="Distros/Current/Config/Players/Vehicles" />' + '\n')
                new_xosc_content.append('        </VehicleCatalog>' + '\n')
                new_xosc_content.append('        <ControllerCatalog>' + '\n')
                new_xosc_content.append(
                    '            <Directory path="Distros/Current/Config/Players/driverCfg.xml" />' + '\n')
                new_xosc_content.append('        </ControllerCatalog>' + '\n')
                new_xosc_content.append('    </CatalogLocations>' + '\n')
                line = next(file_input)

            # 设置xodr以及osgb文件的关联
            elif 'LogicFile' in line:
                new_xosc_content.append(
                    '        <LogicFile filepath="Projects/Current/Databases/roadrunner/' + vtd_change.vtd_name + '.xodr"/>' + '\n')
                line = next(file_input)
            elif 'SceneGraphFile' in line:
                new_xosc_content.append(
                    '        <SceneGraphFile filepath="Projects/Current/Databases/roadrunner/' + vtd_change.vtd_name + '.osgb"/>' + '\n')
                line = next(file_input)

            # 添加车辆显示模型
            elif 'vehicleCategory' in line:
                new_xosc_content.append(
                    '            <Vehicle name="Audi_A3_2009_black" vehicleCategory="car">' + '\n')
                line = next(file_input)

            # 添加驾驶员模型
            elif '/Vehicle>' in line:
                new_xosc_content.append('            </Vehicle>' + '\n')
                new_xosc_content.append('            <ObjectController>' + '\n')
                new_xosc_content.append('                <Controller name="DefaultDriver">' + '\n')
                new_xosc_content.append('                    <Properties/>' + '\n')
                new_xosc_content.append('                </Controller>' + '\n')
                new_xosc_content.append('            </ObjectController>' + '\n')
                line = next(file_input)

            # 注释掉GlobalGroup的内容（roadrunner添加动作时间后会导出的内容)
            elif 'GlobalGroup" maximumExecutionCount="1"' in line:
                str_1 = line.replace("\n", "")
                new_xosc_content.append('<!--' + str_1 + '\n')
                time_change_set = 1
                act_cont = act_cont + 1
                line = next(file_input)
            elif '         </StopTrigger>' in line:
                str_1 = line.replace("\n", "")
                new_xosc_content.append(str_1 + '-->' + '\n')
                time_change_set = 0
                line = next(file_input)

            # 将正确的动作触发时间添加到对应的start trigger中
            elif 'StoryboardElementStateCondition' in line:

                if time_change_set == 0:
                    set_out_n = out_n
                    time_input = vtd_change.vtd_time_arr[out_m][out_n]
                    if time_input == 0:
                        out_m = out_m + 1
                        out_n = 0

                    if out_m > in_m_cont:
                        out_m = 1
                        out_n = 1
                        act_set = act_set + 1

                    time_input = vtd_change.vtd_time_arr[out_m][out_n]
                    if time_input == -1:
                        out_n = out_n + 1
                    time_input = vtd_change.vtd_time_arr[out_m][out_n]

                    vtd_change.vtd_time_arr[out_m][out_n] = -1
                    time_set = str(time_input)

                    # print(time_set)
                    new_xosc_content.append(
                        "                                            <SimulationTimeCondition value=" + '"' + time_set + '"' + ' rule="greaterThan" />' + '\n')

                    out_n = out_n + 1
                    if out_m > 0 and out_n == 1:
                        out_m = out_m + 1
                        out_n = 0

                    line = next(file_input)
                else:
                    new_xosc_content.append(file_input.readline())

            # 将无需修改的内容复制到新文件中
            else:
                # line_s = file_input.readline()
                new_xosc_content.append(file_input.readline())

        file_input.close()

        # 将修改后的文件内容写入到新文件中
        file_output = open(output_dir, "w")
        for line in new_xosc_content:
            file_output.writelines(line)
        file_output.close()

        # 将文件后缀更改为.xosc
        file_change_suffix = os.listdir(output_list)
        for filename in file_change_suffix:
            portion = os.path.splitext(filename)
            if portion[1] == '.txt':
                newname = output_list + portion[0] + '.xosc'
                filename = output_list + filename
                os.rename(filename, newname)



