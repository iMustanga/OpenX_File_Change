import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
# import selectfile
import xml_prescan_change
import default_file
from window.window_prescan import Ui_window_prescan

paths = []
inputs = []
prescan_inputs = []
name = []

# DEFAULT_INPUT_DATABASE = os.path.abspath(os.path.dirname(os.getcwd())) + "\\database"

class presc_change(QtWidgets.QWidget, Ui_window_prescan):

    def __init__(self):
        print("---------------分割线----------------")
        super(presc_change, self).__init__()
        self.setupUi(self)

        self.prescan_select_input.clicked.connect(self.input_file)
        self.prescan_select_output.clicked.connect(self.prescan_input)
        # self.new_file_name.textEdited.connect(new_name)
        self.to_prescan.clicked.connect(self.prescan_change)
        print("---------------分割线----------------")
        print("验证鼠标点击选择路径、目标安装目录，键盘输入新文件名称：")


    def input_file(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件",
                                                                   default_file.DEFAULT_INPUT_DATABASE,
                                                                   "All Files(*);;Text Files(*.txt)")
        paths.clear()
        inputs.clear()

        paths.append(fileName)
        inputs.append(fileName)
        self.prescan_show_input.setText(fileName)
        print("inputs: %s" % inputs)

    def prescan_input(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(None, "请选择prescan文件夹路径",
                                                               default_file.DEFAULT_OUTPUT_DIR)
        paths.clear()
        prescan_inputs.clear()
        paths.append(directory)
        prescan_inputs.append(directory)
        self.prescan_show_output.setText(directory)
        print("prescan_inputs: %s" % prescan_inputs)

    def new_name(self):
        new_file_name = ui.new_file_name.text()
        name.clear()
        name.append(new_file_name)
        print("name = %s" % name)
        print("name[0] = %s" % name[0])

    def prescan_change(self):
        str = '/'
        input_dir_and_file = inputs[0]
        input_dir, input_file1 = os.path.split(input_dir_and_file)# 将文件划分为路径和文件名
        print("---------------分割线----------------")
        print("验证文件名及文件路径：")
        print("input_dir_and_file = %s" % input_dir_and_file)
        print("input_dir = %s" % input_dir)
        print("input_file1 = %s" % input_file1)

        old_file_name, _ = os.path.splitext(input_file1)# 将文件名划分为文件名称和文件拓展名，拓展名用不到
        print("old_file_name = %s" % old_file_name)

        output_dir = prescan_inputs[0]
        print("output_dir = %s" % output_dir)

        input_file = input_dir + str + old_file_name + '.xosc'
        print("input_file = %s" % input_file)

        # output_file = output_dir + str + name[0] + '.xosc'
        output_file = output_dir + str + old_file_name + '.xosc'
        print("output_file = %s" % output_file)

        roadRunner_to_prescan = xml_prescan_change.roadrunnner_to_prescan(input_file, output_file)
        roadRunner_to_prescan.prescan_tranform()
        print("No Bug!! Enjoy.")
'''  
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        print("---------------分割线----------------")
        window = QMainWindow()
        ui = selectfile.Ui_MainWindow()
        ui.setupUi(window)
        window.show()
        ui.select_input.clicked.connect(input_file)
        ui.select_output.clicked.connect(prescan_input)
        ui.new_file_name.textEdited.connect(new_name)
        ui.Prescan.clicked.connect(prescan_change)
        print("---------------分割线----------------")
        print("验证鼠标点击选择路径、目标安装目录，键盘输入新文件名称：")
        sys.exit(app.exec_())
'''