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
files = []
dir_list = []

class SelectDir(QWidget):
    def __init__(self, files, directory, interact):
        super().__init__()
        self.directory = directory
        self.files = files

        self.interact = interact

        self.setWindowTitle('请勾选包含xosc文件的文件夹')
        self.setGeometry(200, 200, 500, 600)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        # 创建滚动区域
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)  # 允许滚动区域内的小部件调整大小

        scroll_widget = QWidget()
        scroll_area.setWidget(scroll_widget)

        selectbox = QGridLayout()
        scroll_widget.setLayout(selectbox)

        self.file_checkboxes = {}
        self.selected_files = ""

        for file in self.files:
            checkbox = QCheckBox(file)
            checkbox.stateChanged.connect(self.onCheckboxStateChanged)
            # 字体大小
            font = checkbox.font()
            font.setPointSize(10)
            checkbox.setFont(font)
            selectbox.addWidget(checkbox, self.files.index(file) // 2, self.files.index(file) % 2)
            self.file_checkboxes[file] = checkbox

        button_layout = QVBoxLayout()
        select_all_button = QPushButton('全选')
        select_all_button.clicked.connect(self.selectAll)
        button_layout.addWidget(select_all_button)
        select_none_button = QPushButton('取消全选')
        select_none_button.clicked.connect(self.selectNon)
        button_layout.addWidget(select_none_button)
        confirm_button = QPushButton('确认')
        confirm_button.clicked.connect(lambda: self.confirm(interact))
        button_layout.addWidget(confirm_button)

        # 创建一个搜索输入框
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.textChanged.connect(self.filterFiles)
        search_label = QLabel("请输入需要查找的文件夹名称：")
        search_label.setBuddy(self.search_input)
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_input)

        main_layout = QVBoxLayout()
        main_layout.addLayout(search_layout)
        main_layout.addWidget(scroll_area)
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

    def onCheckboxStateChanged(self, state):
        sender = self.sender()
        for file, checkbox in self.file_checkboxes.items():
            if checkbox == sender:
                if state == 2:  # 选中
                    # 将选中文件夹的路径存入列表dir_list
                    dir_list.append(self.directory + '/' + file)
                else:
                    # 将取消选中文件夹的路径从列表dir_list中删除
                    dir_list.remove(self.directory + '/' + file)

    def selectAll(self):
        for file, checkbox in self.file_checkboxes.items():
            checkbox.setChecked(True)

    def selectNon(self):
        for file, checkbox in self.file_checkboxes.items():
            checkbox.setChecked(False)

    def confirm(self, interact):
        file_fir1 = []
        num1 = len(dir_list)

        if num1 == 0:
            msg_box = QMessageBox.information(QtWidgets.QWidget(), '提示', '没有做任何勾选')
        else:
            for i in range(num1):
                dir1 = os.path.basename(dir_list[i])
                file_fir1.append(dir1)

            file_fir = interact.dir_name + '/' + file_fir1[0]

            for dir in file_fir1:
                if dir == file_fir1[0]:
                    continue
                else:
                    file_fir2 = file_fir + '+' + dir
                    file_fir = file_fir2

            interact.prescan_show_input.setText(str(file_fir))
            self.close()

            VALID.append(2)

    def closeEvent(self, event):
        super().closeEvent(event)
        if hasattr(self.interact, 'prescan_select_input_dir'):
            self.interact.prescan_select_input_dir.setEnabled(True)
        else:
            print("未找到 'prescan_select_input_dir' 按钮")

    def filterFiles(self):
        search_text = self.search_input.text().lower()
        for file, checkbox in self.file_checkboxes.items():
            if search_text in file.lower():
                checkbox.setVisible(True)
            else:
                checkbox.setVisible(False)

class presc_change(QtWidgets.QWidget, Ui_window_prescan):

    def __init__(self):
        super(presc_change, self).__init__()
        self.setupUi(self)

        self.prescan_select_input.clicked.connect(self.input_file)
        self.prescan_select_output.clicked.connect(self.prescan_input)
        self.prescan_select_input_dir.clicked.connect(self.input_dir)
        self.to_prescan.clicked.connect(self.prescan_change)

        # 2023.11.6 每次打开Prescan的窗口都会清除掉跟转换有关的列表
        dir_list.clear()
        files.clear()
        prescan_inputs.clear()
        VALID.clear()
        inputs.clear()

    def input_file(self):
        self.prescan_select_input.setEnabled(False)

        fileName, fileType = QtWidgets.QFileDialog.getOpenFileNames(None, "选取文件",
                                                                   default_file.DEFAULT_INPUT_DATABASE,
                                                                   "Text Files(*.xosc)")
        inputs.clear()
        VALID.clear()

        self.prescan_show_input.clear()

        inputs.append(fileName)

        # 2023.10.17 添加文件多选功能
        # 判断选取的文件数量
        self.num = np.size(inputs)
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

        self.prescan_select_input.setEnabled(True)

    # 2023.10.18 添加选择文件夹功能
    def input_dir(self):
        self.prescan_select_input_dir.setEnabled(False)

        self.dir_name = QtWidgets.QFileDialog.getExistingDirectory(None, "请选择文件夹",
                                                              default_file.DEFAULT_INPUT_DATABASE)

        VALID.clear()
        dir_list.clear()

        self.prescan_show_input.clear()

        if self.dir_name:
            # 2023.11.1 实现勾选文件夹功能，使用二级弹窗
            self.files = [f for f in os.listdir(self.dir_name) if os.path.isdir(os.path.join(self.dir_name, f))]
            self.select_dir = SelectDir(self.files, self.dir_name, self)
            self.select_dir.show()

        elif not self.dir_name:
            self.prescan_select_input_dir.setEnabled(True)

    def prescan_input(self):
        self.prescan_select_output.setEnabled(False)

        directory = QtWidgets.QFileDialog.getExistingDirectory(None, "请选择prescan文件夹路径",
                                                               "D:/PreScan/Experiment_place/import_actions/python_test")

        self.prescan_show_output.clear()

        prescan_inputs.clear()
        prescan_inputs.append(directory)
        self.prescan_show_output.setText(directory)

        self.prescan_select_output.setEnabled(True)

    # 2023.10.11添加显示修改结果功能
    def show_result(self):
        msg_box = QMessageBox.information(QtWidgets.QWidget(), '提示',
                                          '修改成功')

    # 2023.10.17 封装获取主修改程序输入路径的代码
    def get_input_parameters_1(self, inputs):# 2023.10.17 给成员方法一个输入
        self.str1 = '/'
        self.input_dir_and_file = inputs
        self.input_dir, self.input_file1 = os.path.split(self.input_dir_and_file)  # 将文件划分为路径和文件名

        self.old_file_name, _ = os.path.splitext(self.input_file1)  # 将文件名划分为文件名称和文件拓展名，拓展名用不到

        self.output_dir = prescan_inputs[0]

        self.input_file = self.input_dir + self.str1 + self.old_file_name + '.xosc'

        self.output_file = self.output_dir + self.str1 + self.old_file_name + '.xosc' # 2023.10.17 取消新文件名功能，用旧文件名替代

    def prescan_change(self):
        if not VALID: # 没有点击选择文件或文件夹按钮，或者点了按钮但又点了取消，这两种情况下VALID列表均为空，都会提示如下内容
            if not prescan_inputs or all(element == '' for element in prescan_inputs):
                msg_box = QMessageBox.information(QtWidgets.QWidget(), '提示', '请先选择文件和目标路径')
            else:
                msg_box = QMessageBox.information(QtWidgets.QWidget(), '提示', '请先选择文件或文件夹')

        elif VALID[0] == 1: # 如果VALID列表含有元素1，则进入文件多选对应的修改程序
            self.size = np.size(inputs)  # 2023.10.17 改成使用首文件的拓展名作为判断依据

            if not prescan_inputs or all(element == '' for element in prescan_inputs):
                msg_box = QMessageBox.information(QtWidgets.QWidget(), '提示', '请先选择目标路径')
            else:
                if self.size > 1:

                    self.c = 0
                    error_file_list1 = []

                    for i in range(self.size):
                        self.get_input_parameters_1(str(inputs[0][i]))
                        roadRunner_to_prescan = xml_prescan_change.roadrunnner_to_prescan(self.input_file,
                                                                                              self.output_file)
                        self.result = roadRunner_to_prescan.prescan_tranform()
                        if self.result == 1:
                            self.c += 1
                            error_file_list1.append(self.input_file1)
                    if self.c != 0:
                        if len(error_file_list1) == 1:
                            with open(prescan_inputs[0] + '/' + '文件本身存在错误.txt', mode='w') as f:
                                f.write('以下文件存在错误，修改不成功：\n' + error_file_list1[0])
                        else:
                            self.error_file_string = '\n'.join(error_file_list1)
                            with open(prescan_inputs[0] + '/' + '文件本身存在错误.txt', mode='w') as f:
                                f.write('以下文件存在错误，修改不成功：\n' + self.error_file_string)
                        msg_box = QMessageBox.warning(QtWidgets.QWidget(), '警告', '修改出错')
                    else:

                        self.show_result()
                else:
                    self.get_input_parameters_1(str(inputs[0][0]))
                    roadRunner_to_prescan = xml_prescan_change.roadrunnner_to_prescan(self.input_file,
                                                                                      self.output_file)
                    self.result = roadRunner_to_prescan.prescan_tranform()
                    if self.result == 1:
                        msg_box = QMessageBox.warning(QtWidgets.QWidget(), '警告', '修改错误！因为所选择的文件' + self.input_file1 + '本身存在错误。')
                    else:
                        self.show_result()

        elif VALID[0] == 2: # 如果VALID列表元素值为2，则进行文件夹修改功能，会识别文件夹内的xosc文件并修改，与此同时弹窗提示所有非xosc文件

            not_xosc_list2 = []
            new_file_name_exist_list = []

            if not prescan_inputs or all(element == '' for element in prescan_inputs):
                msg_box = QMessageBox.information(QtWidgets.QWidget(), '提示', '请先选择目标路径')
            else:
                len1 = len(dir_list)

                self.e = len1

                for i in range(len1):
                    file_list = os.listdir(dir_list[i])
                    new_file_name = os.path.basename(dir_list[i])  # 获得所选文件夹的文件夹名，作为新文件夹的文件夹名
                    new_file = prescan_inputs[0] + '/' + new_file_name  # 得到新文件夹路径

                    # 2023.10.25 添加功能：先判断目标路径是否有同名文件夹，是则弹窗警告，否则创建文件夹
                    # 2023.11.3 完善在多选文件夹时识别到有同名文件夹时的提示功能
                    if new_file_name in os.listdir(prescan_inputs[0]):
                        new_file_name_exist_list.append(new_file_name)
                        continue
                    else:
                        os.mkdir(new_file)  # 创建与所选文件夹同名的新文件夹

                        self.d = 0
                        error_file_list2 = []

                        for file_name in file_list:  # 遍历所选文件夹
                            file_name1, expand_name = os.path.splitext(file_name)
                            if expand_name != '.xosc':
                                not_xosc_list2.append(file_name)  # 记录文件夹中所有的非xosc文件

                            else:
                                self.input_file = dir_list[i] + '/' + file_name1 + '.xosc'
                                self.output_file = new_file + '/' + file_name1 + '.xosc'
                                roadRunner_to_prescan = xml_prescan_change.roadrunnner_to_prescan(self.input_file,
                                                                                                  self.output_file)
                                self.result = roadRunner_to_prescan.prescan_tranform()
                                if self.result == 1:
                                    self.d += 1
                                    error_file_list2.append(file_name)

                        if self.d != 0:
                            if len(error_file_list2) == 1:
                                with open(new_file + '/' + '文件本身存在错误.txt', mode='w') as f:
                                    f.write('以下文件存在错误，修改不成功：\n' + error_file_list2[0])
                            else:
                                self.error_file_string2 = '\n'.join(error_file_list2)
                                with open(new_file + '/' + '文件本身存在错误.txt', mode='w') as f:
                                    f.write('以下文件存在错误，修改不成功：\n' + self.error_file_string2)
                            self.e -= 1

                        num_list = len(file_list)
                        num_not_xosc_list2 = len(not_xosc_list2)

                        if not_xosc_list2:
                            self.file_string2 = '\n'.join(not_xosc_list2)
                            # 2023.10.25 创建文本文件，将弹窗信息写入其中，看与否决定权交回给用户
                            with open(new_file + '/' + '存在非xosc导致的错误.txt', mode='w') as f:
                                f.write('以下文件不是xosc文件，无法修改：\n' + self.file_string2)
                        else:
                            if not os.path.isdir(new_file + '/' + '文件本身存在错误.txt'):
                                pass
                            else:
                                with open(new_file + '/' + '存在非xosc文件导致的错误.txt', mode='w') as f:
                                    f.write('在所选文件夹' + self.dir_name + '中，总共包含' + str(num_list) + '个文件，全部文件均以修改为Prescan可用的格式。')

                # 2023.11.3 完善在多选文件夹时识别到有同名文件夹时的提示功能
                len2 = len(new_file_name_exist_list)
                if len2 == 0:
                    if self.e == len1:
                        self.show_result()
                    else:
                        msg_box = QMessageBox.warning(QtWidgets.QWidget(), '警告', '修改出错')
                elif len2 == 1:
                    msg_box = QMessageBox.warning(QtWidgets.QWidget(), '警告',
                                                  '想要创建的名为' + new_file_name_exist_list[
                                                      0] + '的文件夹已存在于该目标路径，请先删除路径中的同名文件夹。')
                else:
                    new_file_name_exist_list_string = ', '.join(new_file_name_exist_list)
                    msg_box = QMessageBox.warning(QtWidgets.QWidget(), '警告',
                                                  '想要创建的名为' + new_file_name_exist_list_string + '的文件夹已存在于该目标路径，请先删除路径中的同名文件夹。')


















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