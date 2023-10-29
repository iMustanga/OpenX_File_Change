import numpy as np
import os
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import xml_prescan_change
import default_file
from window.window_prescan import Ui_window_prescan

inputs = []
prescan_inputs = []
VALID = []

class presc_change(QtWidgets.QWidget, Ui_window_prescan):

    def __init__(self):
        print("---------------分割线----------------")
        super(presc_change, self).__init__()
        self.setupUi(self)

        self.prescan_select_input.clicked.connect(self.input_file)
        self.prescan_select_output.clicked.connect(self.prescan_input)
        self.prescan_select_input_dir.clicked.connect(self.input_dir)
        # self.new_file_name.textEdited.connect(new_name)
        self.to_prescan.clicked.connect(self.prescan_change)
        print("---------------分割线----------------")
        print("验证鼠标点击选择路径、目标安装目录，键盘输入新文件名称：")

    def input_file(self):
        self.prescan_select_input.setEnabled(False)

        fileName, fileType = QtWidgets.QFileDialog.getOpenFileNames(None, "选取文件",
                                                                   default_file.DEFAULT_INPUT_DATABASE,
                                                                   "All Files(*);;Text Files(*.txt)")
        inputs.clear()
        VALID.clear()
        inputs.append(fileName)
        print("filename: %s" % fileName)
        print("inputs: %s" % inputs)

        # 2023.10.17 添加文件多选功能
        # 判断选取的文件数量
        self.num = np.size(inputs)
        print("选择的文件个数为：%s" % self.num)
        if self.num > 1:
            out_name = []
            out_name = fileName[0]
            for i in range(self.num-1):
                out_name = out_name + ' + ' + os.path.basename(fileName[i+1])
            self.prescan_show_input.setText(out_name)
        elif self.num == 1:
            self.prescan_show_input.setText(fileName[0])
        elif self.num == 0:
            fileName.append('')
        # 2023.10.19 使用os.path.isfile功能识别多选文件功能
        if os.path.isfile(fileName[0]):
            VALID.append(1)
        print("VALID: %s" % VALID)

        self.prescan_select_input.setEnabled(True)

    # 2023.10.18 添加选择文件夹功能
    def input_dir(self):
        self.prescan_select_input_dir.setEnabled(False)

        self.dir_name = QtWidgets.QFileDialog.getExistingDirectory(None, "请选择文件夹路径",
                                                              default_file.DEFAULT_INPUT_DATABASE)
        inputs.clear()
        VALID.clear()
        inputs.append(self.dir_name)
        self.prescan_show_input.setText(self.dir_name)
        print("dirname: %s" % self.dir_name)
        print("inputs: %s" % inputs)
        # 2023.10.19 使用os.path.isdir识别文件夹选择功能
        if os.path.isdir(self.dir_name):
            VALID.append(2)
        print("VALID: %s" % VALID)

        self.prescan_select_input_dir.setEnabled(True)

    def prescan_input(self):
        self.prescan_select_output.setEnabled(False)

        directory = QtWidgets.QFileDialog.getExistingDirectory(None, "请选择prescan文件夹路径",
                                                               "D:/PreScan/Experiment_place/import_actions/python_test")
        prescan_inputs.clear()
        prescan_inputs.append(directory)
        self.prescan_show_output.setText(directory)
        print("prescan_inputs: %s" % prescan_inputs)

        self.prescan_select_output.setEnabled(True)

    # 2023.10.11添加显示修改结果功能
    def show_result(self):
        msg_box = QMessageBox.information(QtWidgets.QWidget(), '提示',
                                          '修改成功')

    def prescan_readme(self):
        with open(prescan_inputs[0] + '/' + 'Prescan_Readme.txt', mode='w') as prescan_readme_file:
            prescan_readme_file.write('一、请按操作文档的要求在RoadRunner中构建OpenScenario场景并导出。\n \n')
            prescan_readme_file.write('二、运行RoadRunner-Prescan场景转换软件完成指定xosc文件的转换后，需要使用MATLAB脚本导入Prescan。导入方法如下：\n \n')
            prescan_readme_file.write('1.首先确保本机中含有Simcenter Prescan 2206软件；\n')
            prescan_readme_file.write('2.在软件Experiment目录下新建文件路径，自定义命名，命名规则与其他文件夹相同。\n')
            prescan_readme_file.write('3.使用Prescan Process Manager 2206控制台打开MATLAB，新建脚本文件，自定义文件名称并保存脚本文件至步骤2中创建的文件夹中。\n')
            prescan_readme_file.write('4.在脚本文件中键入一下命令：\n \n')
            prescan_readme_file.write('\t' + 'experiment = prescan.api.experiment.createExperiment(); % 创建实验\n \n')
            prescan_readme_file.write('\t' + 'prescan.api.openscenario.importOpenScenarioFile(experiment, ''); % 导入OpenScenario文件，''内填入修改后的xosc文件路径 \n \n')
            prescan_readme_file.write('\t' + 'experiment.scheduler.simulationSpeed = prescan.api.types.SimulationSpeed.WallClockSpeed; '
                                      '% 让项目以墙上时钟速度运行\n \n')
            prescan_readme_file.write('\t' + 'myViewer = prescan.api.viewer.createViewer(experiment); % 添加Prescan Viewer \n '
                                      '\t' + 'myViewer.windowSettings.windowDecoration = true; \n \n')
            prescan_readme_file.write('\t' + 'experiment.saveToFile(''); % 保存，''内填入pb文件名，格式为XX.pb\n \n')
            prescan_readme_file.write('\t' + 'prescan.api.simulink.generate(); % 创建cs\n \n')
            prescan_readme_file.write('三、若有添加传感器的需要，可以在脚本文件中添加一下命令： \n \n')
            prescan_readme_file.write('\t' + 'for i = 1:numel(experiment.objects) \n ')
            prescan_readme_file.write('\t' + '\t' + 'prescan.api.pcs.createPcsSensor(experiment.objects(i)); % 以导入Point Cloud Sensor为例\n \n')
            prescan_readme_file.write('四、若需要配置传感器参数，如配置Point Cloud Sensor的分辨率，可以进行如下操作：\n \n')
            prescan_readme_file.write('1.首先创建一个对象，如pcsensor：\n')
            prescan_readme_file.write('\t' + 'pcsensor = prescan.api.pcs.createPcsSensor(experiment.objects(i));\n \n')
            prescan_readme_file.write('2.然后赋值修改分辨率：\n')
            prescan_readme_file.write('\t' + 'pcsensor.resolutionX = 630;\n')
            prescan_readme_file.write('\t' + 'pcsensor.resolutionY = 125;\n')

    # 2023.10.17 封装获取主修改程序输入路径的代码
    def get_input_parameters_1(self, inputs):# 2023.10.17 给成员方法一个输入
        self.str1 = '/'
        self.input_dir_and_file = inputs
        self.input_dir, self.input_file1 = os.path.split(self.input_dir_and_file)  # 将文件划分为路径和文件名
        print("input_dir_and_file = %s" % self.input_dir_and_file)
        print("input_dir = %s" % self.input_dir)
        print("input_file1 = %s" % self.input_file1)

        self.old_file_name, _ = os.path.splitext(self.input_file1)  # 将文件名划分为文件名称和文件拓展名，拓展名用不到
        print("old_file_name = %s" % self.old_file_name)

        self.output_dir = prescan_inputs[0]
        print("output_dir = %s" % self.output_dir)

        self.input_file = self.input_dir + self.str1 + self.old_file_name + '.xosc'
        print("input_file = %s" % self.input_file)

        self.output_file = self.output_dir + self.str1 + self.old_file_name + '.xosc' # 2023.10.17 取消新文件名功能，用旧文件名替代
        print("output_file = %s" % self.output_file)

    def prescan_change(self):
        if not VALID: # 没有点击选择文件或文件夹按钮，或者点了按钮但又点了取消，这两种情况下VALID列表均为空，都会提示如下内容
            if not prescan_inputs or all(element == '' for element in prescan_inputs):
                msg_box = QMessageBox.information(QtWidgets.QWidget(), '提示', '请先选择文件和目标路径')
            else:
                msg_box = QMessageBox.information(QtWidgets.QWidget(), '提示', '请先选择文件或文件夹')

        elif VALID[0] == 1: # 如果VALID列表含有元素1，则进入文件多选对应的修改程序
            print("进行了文件的多选")
            self.size = np.size(inputs)  # 2023.10.17 改成使用首文件的拓展名作为判断依据
            print("size: %s" % self.size)

            if not prescan_inputs or all(element == '' for element in prescan_inputs):
                msg_box = QMessageBox.information(QtWidgets.QWidget(), '提示', '请先选择目标路径')
            else:
                if self.size > 1:
                    print("多文件场景")
                    for i in range(self.size):
                        self.get_input_parameters_1(str(inputs[0][i]))
                        roadRunner_to_prescan = xml_prescan_change.roadrunnner_to_prescan(self.input_file,
                                                                                              self.output_file)
                        roadRunner_to_prescan.prescan_tranform()
                    print("No Bug!! Enjoy.")
                    self.prescan_readme()
                    self.show_result()
                else:
                    print("单文件场景")
                    self.get_input_parameters_1(str(inputs[0][0]))
                    roadRunner_to_prescan = xml_prescan_change.roadrunnner_to_prescan(self.input_file,
                                                                                      self.output_file)
                    roadRunner_to_prescan.prescan_tranform()
                    print("No Bug!! Enjoy.")
                    self.prescan_readme()
                    self.show_result()

        elif VALID[0] == 2: # 如果VALID列表元素值为2，则进行文件夹修改功能，会识别文件夹内的xosc文件并修改，与此同时弹窗提示所有非xosc文件
            print("选择了文件夹")
            not_xosc_list2 = []
            if not prescan_inputs or all(element == '' for element in prescan_inputs):
                msg_box = QMessageBox.information(QtWidgets.QWidget(), '提示', '请先选择目标路径')
            else:
                file_list = os.listdir(self.dir_name)
                new_file_name = os.path.basename(self.dir_name)  # 获得所选文件夹的文件夹名，作为新文件夹的文件夹名
                print("所选文件夹里的文件列表： %s" % file_list)
                print("新文件夹名： %s" % new_file_name)
                new_file = prescan_inputs[0] + '/' + new_file_name  # 得到新文件夹路径
                print("新文件夹路径：%s" % new_file)

                # 2023.10.25 添加功能：先判断目标路径是否有同名文件夹，是则弹窗警告，否则创建文件夹
                if new_file_name in os.listdir(prescan_inputs[0]):
                    msg_box = QMessageBox.warning(QtWidgets.QWidget(), '警告',
                                                  '想要创建的文件夹已存在于该目标路径，请先删除该文件夹。')
                else:
                    os.mkdir(new_file)  # 创建与所选文件夹同名的新文件夹
                    for file_name in file_list:  # 遍历所选文件夹
                        file_name1, expand_name = os.path.splitext(file_name)
                        if expand_name != '.xosc':
                            not_xosc_list2.append(file_name)  # 记录文件夹中所有的非xosc文件

                        else:
                            self.input_file = self.dir_name + '/' + file_name1 + '.xosc'
                            self.output_file = new_file + '/' + file_name1 + '.xosc'
                            roadRunner_to_prescan = xml_prescan_change.roadrunnner_to_prescan(self.input_file,
                                                                                              self.output_file)
                            roadRunner_to_prescan.prescan_tranform()

                    print("非xosc文件列表： %s" % not_xosc_list2)
                    self.show_result()
                    self.prescan_readme()

                    num_list = len(file_list)
                    print("文件夹中含有的文件数量：%s" % num_list)
                    num_not_xosc_list2 = len(not_xosc_list2)
                    print("文件夹中含有的非xosc文件数量：%s" % num_not_xosc_list2)

                    if not_xosc_list2:
                        self.file_string2 = '\n'.join(not_xosc_list2)
                        with open(new_file + '/' + '备注.txt', mode='w') as f:
                            f.write('以下文件不是xosc文件，无法修改：\n' + self.file_string2)
                    else:
                        with open(new_file + '/' + '备注.txt', mode='w') as f:
                            f.write('在所选文件夹' + self.dir_name + '中，总共包含' + str(num_list) + '个文件，全部文件均以修改为Prescan可用的格式。')











    # def input_file(self):
    #     fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件",
    #                                                                default_file.DEFAULT_INPUT_DATABASE,
    #                                                                "All Files(*);;Text Files(*.txt)")
    #     inputs.clear()
    #
    #     inputs.append(fileName)
    #     self.prescan_show_input.setText(fileName)
    #     print("inputs: %s" % inputs)
    #
    # def prescan_input(self):
    #     directory = QtWidgets.QFileDialog.getExistingDirectory(None, "请选择prescan文件夹路径",
    #                                                            default_file.DEFAULT_OUTPUT_DIR)
    #     prescan_inputs.clear()
    #     prescan_inputs.append(directory)
    #     self.prescan_show_output.setText(directory)
    #     print("prescan_inputs: %s" % prescan_inputs)
    #
    # # def new_name(self):
    # #     new_file_name = ui.new_file_name.text()
    # #     name.clear()
    # #     name.append(new_file_name)
    # #     print("name = %s" % name)
    # #     print("name[0] = %s" % name[0])
    #
    # # 2023.10.11添加修改成功反馈
    # def show_result(self):
    #     msg_box = QMessageBox.information(QtWidgets.QWidget(), '提示',
    #                                       '修改成功')
    # def prescan_change(self):
    #     # 2023.10.12添加选择文件和路径相关提示
    #     if not inputs or all(element == '' for element in inputs):
    #         if not prescan_inputs or all(element == '' for element in prescan_inputs):
    #             msg_box = QMessageBox.information(QtWidgets.QWidget(), '提示',
    #                                               '请先选择文件和目标路径')
    #         else:
    #             msg_box = QMessageBox.information(QtWidgets.QWidget(), '提示',
    #                                               '请先选择文件')
    #     elif not prescan_inputs or all(element == '' for element in prescan_inputs):
    #         msg_box = QMessageBox.information(QtWidgets.QWidget(), '提示',
    #                                           '请先选择目标路径')
    #     else:
    #         str1 = '/'
    #         input_dir_and_file = inputs[0]
    #         input_dir, input_file1 = os.path.split(input_dir_and_file)# 将文件划分为路径和文件名
    #         print("---------------分割线----------------")
    #         print("验证文件名及文件路径：")
    #         print("input_dir_and_file = %s" % input_dir_and_file)
    #         print("input_dir = %s" % input_dir)
    #         print("input_file1 = %s" % input_file1)
    #
    #         old_file_name, _ = os.path.splitext(input_file1)# 将文件名划分为文件名称和文件拓展名，拓展名用不到
    #         print("old_file_name = %s" % old_file_name)
    #
    #         output_dir = prescan_inputs[0]
    #         print("output_dir = %s" % output_dir)
    #
    #         input_file = input_dir + str1 + old_file_name + '.xosc'
    #         print("input_file = %s" % input_file)
    #
    #         # output_file = output_dir + str + name[0] + '.xosc'
    #         output_file = output_dir + str1 + old_file_name + '.xosc'
    #         print("output_file = %s" % output_file)
    #
    #         roadRunner_to_prescan = xml_prescan_change.roadrunnner_to_prescan(input_file, output_file)
    #         roadRunner_to_prescan.prescan_tranform()
    #         print("No Bug!! Enjoy.")
    #         self.show_result()