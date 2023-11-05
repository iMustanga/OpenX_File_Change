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

# 10.27增加勾选多文件夹
class SelectDir(QWidget):
    def __init__(self, files, directory, interact):
        super().__init__()
        self.directory = directory
        self.files = files
        self.dir_list = []

        self.setWindowTitle('请选择包含xosc文件的文件夹')
        self.setGeometry(100, 100, 500, 550)
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
        # 创建一个搜索标签
        search_label = QLabel('搜索指定文件夹')
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
                    self.dir_list.append(os.path.join(self.directory, file))
                else:
                    # 将取消选中文件夹的路径从列表dir_list中删除
                    self.dir_list.remove(os.path.join(self.directory, file))

    def selectAll(self):
        for file, checkbox in self.file_checkboxes.items():
            checkbox.setChecked(True)

    def selectNon(self):
        for file, checkbox in self.file_checkboxes.items():
            checkbox.setChecked(False)

    def confirm(self, interact):
        interact.carmaker_input_dir = []
        for dir in self.dir_list:
            file_list = Path(dir).glob('**/*.xosc')
            # 将所有xosc文件路径转换为字符串
            file_list = [str(i) for i in file_list]
            file_lists = interact.carmaker_input_dir + file_list
            interact.carmaker_input_dir = file_lists
        interact.carmaker_show_input.setText(str(self.dir_list))
        self.close()

    def filterFiles(self):
        search_text = self.search_input.text().lower()
        for file, checkbox in self.file_checkboxes.items():
            if search_text in file.lower():
                checkbox.setVisible(True)
            else:
                checkbox.setVisible(False)


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

    # # 10.20增加选择文件夹功能
    # def carmaker_input_dir_init(self):
    #     directory = QtWidgets.QFileDialog.getExistingDirectory(None, "请选择文件夹路径",
    #                                                            default_file.DEFAULT_INPUT_DATABASE)
    #     # 获取directory文件夹下所有xosc文件路径
    #     file_list = Path(directory).glob('**/*.xosc')
    #     # 将所有xosc文件路径转换为字符串
    #     file_list = [str(i) for i in file_list]
    #     self.carmaker_input_dir = file_list
    #     self.carmaker_show_input.setText(directory)

    # 10.26增加多选文件夹
    # def carmaker_input_dir_init(self):
    #     fileDlg = QtWidgets.QFileDialog()
    #     fileDlg.setFileMode(QFileDialog.DirectoryOnly)
    #     fileDlg.setOption(QFileDialog.DontUseNativeDialog, True)
    #     fileDlg.setDirectory(default_file.DEFAULT_INPUT_DATABASE)
    #     listView = fileDlg.findChild(QListView, "listView")
    #     if listView:
    #         listView.setSelectionMode(QAbstractItemView.ExtendedSelection)
    #     treeView = fileDlg.findChild(QTreeView, "treeView")
    #     if treeView:
    #         treeView.setSelectionMode(QAbstractItemView.ExtendedSelection)
    #     if fileDlg.exec_():
    #         directories = fileDlg.selectedFiles()
    #         self.carmaker_input_dir = []
    #         for directory in directories:
    #             file_list = Path(directory).glob('**/*.xosc')
    #             # 将所有xosc文件路径转换为字符串
    #             file_list = [str(i) for i in file_list]
    #             file_lists = self.carmaker_input_dir + file_list
    #             self.carmaker_input_dir = file_lists
    #         self.carmaker_show_input.setText(str(file_lists))

    # 勾选框多选文件夹
    def carmaker_input_dir_init(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(None, "请选择文件夹路径",
                                                                 default_file.DEFAULT_INPUT_DATABASE)
        if directory:
            # 获取文件夹中的子文件夹名
            files = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]
            self.select_dir = SelectDir(files, directory, self)
            self.select_dir.show()


    def carmaker_output_init(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(None, "请选择文件夹路径",
                                                               default_file.DEFAULT_OUTPUT_DIR)
        self.carmaker_output_dir = directory

        self.carmaker_show_output.setText(directory)

    # 10.20修改多文件
    def carmaker_openx_change(self):
        # 提示
        cur_dir = default_file.DEFAULT_CUR_DIR
        if self.carmaker_input_dir is None:
            QMessageBox.warning(self, "Warnning", "Please select input file!")
            return
        if self.carmaker_model_show.currentText() == "":
            QMessageBox.warning(self, "Warnning", "Please select model!")
            return
        if self.carmaker_output_dir is None:
            QMessageBox.warning(self, "Warnning", "Please select output file!")
            return

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



