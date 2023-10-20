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
        self.prescan_select_input_dir.clicked.connect(self.input_dir)
        self.prescan_select_output.clicked.connect(self.prescan_input)
        self.to_prescan.clicked.connect(self.prescan_change)
        print("---------------分割线----------------")
        print("验证鼠标点击选择路径、目标安装目录，键盘输入新文件名称：")

    def input_file(self):
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

    # 2023.10.18 添加选择文件夹功能
    def input_dir(self):
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

    def prescan_input(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(None, "请选择prescan文件夹路径",
                                                               "D:/PreScan/Experiment_place/import_actions/python_test")
        prescan_inputs.clear()
        prescan_inputs.append(directory)
        self.prescan_show_output.setText(directory)
        print("prescan_inputs: %s" % prescan_inputs)

    # 2023.10.11添加显示修改结果功能
    def show_result(self):
        msg_box = QMessageBox.information(QtWidgets.QWidget(), '提示',
                                          '修改成功')

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
            file_name = os.path.basename(str(inputs[0][0]))
            print("首文件文件名file_name: %s" % file_name)
            port = os.path.splitext(file_name)
            print("首文件拓展名port[1]: %s" % port[1])  # 为了得到首文件拓展名，用于判断输入的文件类型

            if 'xosc' in port[1]:  # 只要首文件是xosc文件，就进行修改
                not_xosc_list1 = []
                if not prescan_inputs or all(element == '' for element in prescan_inputs):
                    msg_box = QMessageBox.information(QtWidgets.QWidget(), '提示', '请先选择目标路径')
                else:
                    if self.size > 1:
                        print("多文件场景")
                        # 方法一：
                        # for i in range(self.size):
                        #     self.get_input_parameters_1(str(inputs[0][i]))
                        #     name_por = os.path.basename(str(inputs[0][i]))
                        #     portion = os.path.splitext(name_por)
                        #     if 'xosc' not in portion[1]:
                        #         msg_box = QMessageBox.information(QtWidgets.QWidget(), '警告',
                        #                                           '以下文件不是xosc文件： ' + str(
                        #                                               inputs[0][i]) + '.\n' + '点击ok继续')
                        #         continue
                        #     else:
                        #         roadRunner_to_prescan = xml_prescan_change.roadrunnner_to_prescan(self.input_file,
                        #                                                                           self.output_file)
                        #         roadRunner_to_prescan.prescan_tranform()
                        # print("No Bug!! Enjoy.")
                        # print("----------------------------------分割线-----------------------------------------")
                        # print("----------------------------------分割线-----------------------------------------")
                        # self.show_result()
                        # 方法二：
                        for i in range(self.size):
                            input_file_name3, expand_name2 = os.path.splitext(str(inputs[0][i]))
                            if expand_name2 != '.xosc':
                                input_file_name4 = input_file_name3 + expand_name2
                                not_xosc_list1.append(input_file_name4)  # 记录文件夹中所有的非xosc文件
                            else:
                                self.get_input_parameters_1(str(inputs[0][i]))
                                roadRunner_to_prescan = xml_prescan_change.roadrunnner_to_prescan(self.input_file,
                                                                                                  self.output_file)
                                roadRunner_to_prescan.prescan_tranform()
                        print("非xosc文件列表： %s" % not_xosc_list1)
                        self.show_result()

                        if not_xosc_list1:
                            file_string = '\n'.join(not_xosc_list1)
                            msg_box = QMessageBox.information(QtWidgets.QWidget(), '警告',
                                                              '以下文件不是xosc文件，无法修改：\n' + file_string)

                    else:
                        print("单文件场景")
                        self.get_input_parameters_1(str(inputs[0][0]))
                        roadRunner_to_prescan = xml_prescan_change.roadrunnner_to_prescan(self.input_file,
                                                                                          self.output_file)
                        roadRunner_to_prescan.prescan_tranform()
                        print("No Bug!! Enjoy.")
                        print("----------------------------------分割线-----------------------------------------")
                        print("----------------------------------分割线-----------------------------------------")
                        self.show_result()

            elif port[1] != '.xosc':
                msg_box = QMessageBox.information(QtWidgets.QWidget(), '警告',
                                                  '请谨慎选择需要修改的文件，暂不支持首文件不是xosc格式的多文件修改。以下文件不是xosc文件： ' + str(
                                                      inputs[0][0]))

        elif VALID[0] == 2: # 如果VALID列表元素值为2，则进行文件夹修改功能，会识别文件夹内的xosc文件并修改，与此同时弹窗提示所有非xosc文件
            print("选择了文件夹")
            not_xosc_list2 = []
            if not prescan_inputs or all(element == '' for element in prescan_inputs):
                msg_box = QMessageBox.information(QtWidgets.QWidget(), '提示', '请先选择目标路径')
            else:
                # self.get_input_parameters_2(self.dir_name)
                file_list = os.listdir(self.dir_name)
                new_file_name = os.path.basename(self.dir_name)     # 获得所选文件夹的文件夹名，作为新文件夹的文件夹名
                print("所选文件夹里的文件列表： %s" % file_list)
                print("新文件夹名： %s" % new_file_name)
                new_file = prescan_inputs[0] + '/' + new_file_name # 得到新文件夹路径
                print("新文件夹路径：%s" % new_file)
                os.mkdir(new_file) # 创建与所选文件夹同名的新文件夹

                for file_name in file_list: # 遍历所选文件夹
                    file_name1, expand_name = os.path.splitext(file_name)
                    if expand_name != '.xosc':
                        not_xosc_list2.append(file_name) # 记录文件夹中所有的非xosc文件

                    else:
                        self.input_file = self.dir_name + '/' + file_name1 + '.xosc'
                        self.output_file = new_file + '/' + file_name1 + '.xosc'
                        roadRunner_to_prescan = xml_prescan_change.roadrunnner_to_prescan(self.input_file,
                                                                                          self.output_file)
                        roadRunner_to_prescan.prescan_tranform()

                print("非xosc文件列表： %s" % not_xosc_list2)
                self.show_result()

                # 用窗口的方式显示所选文件夹中所有非xosc文件
                #方法一：
                # not_xosc_list_dir = []
                # num3 = len(not_xosc_list)
                # for i in range(num3):
                #     a = self.dir_name + '/' + not_xosc_list[i]
                #     not_xosc_list_dir.append(a)
                #
                # print("not_xosc_list_dir: %s" % not_xosc_list_dir)
                #
                # file_string = '\n'.join(not_xosc_list_dir)
                # msg_box = QMessageBox.information(QtWidgets.QWidget(), '警告',
                #                               '在所选文件夹中，以下文件不是xosc文件，无法进行修改：' + file_string)
                # 方法二：
                if not_xosc_list2:
                    file_string = '\n'.join(not_xosc_list2)
                    msg_box = QMessageBox.information(QtWidgets.QWidget(), '警告', '在所选文件夹' + self.dir_name + '中，以下文件不是xosc文件，无法修改：\n' + file_string)











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