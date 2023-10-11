import os
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import subprocess
from window.window_main import Ui_MainWindow
from window import window_main, window_vtd
import default_file
import App_vtd
import App_carmaker
import win32api
import win32process
from threading import Thread

class window_main(QtWidgets.QWidget, Ui_MainWindow):
    soft_path = []
    def __init__(self):
        super(window_main, self).__init__()
        self.setupUi(self)
        self.setfun_main()

    # 设置各个按钮功能以及显示框初始功能
    def setfun_main(self):
        self.openx_vtd_change.clicked.connect(self.show_vtd)
        self.openx_carmaker_change.clicked.connect(self.show_carmaker)
        self.select_software_dir.clicked.connect(self.get_soft_dir)
        self.open_software.clicked.connect(self.open_roadrunner)
        self.case_down.clicked.connect(self.case_update)
        self.report.clicked.connect(self.report_update)
        self.range.clicked.connect(self.range_update)

        # 设置打开页面即进行案例下载显示
        self.case_download_show.clear()
        openx_case = os.listdir(default_file.DEFAULT_CASE_DIR)
        self.case_download_show.addItems(openx_case)

        # 设置打开页面即进行测试报告显示
        self.report_show.clear()
        report = os.listdir(default_file.DEFAULT_REPORT_DIR)
        self.report_show.addItems(report)

        # 设置打开页面即进行测试里程显示
        self.range_show.clear()
        range_dis = os.listdir(default_file.DEFAULT_RANGE_DIR)
        self.range_show.addItems(range_dis)

    def show_vtd(self):
        self.vtd_window = App_vtd.vtd_change()
        self.vtd_window.show()

    def show_carmaker(self):
        self.carmaker_window = App_carmaker.window_carmaker_change()
        self.carmaker_window.show()

    def get_soft_dir(self):
        stri = '\n'
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件")
        window_main.soft_path.clear()
        window_main.soft_path.append(fileName)
        # print(soft_path)
        file_softpath = open(default_file.DEFAULT_ROADRUNNER_SOFT_DIR, mode="w")
        file_softpath.truncate(0)
        file_softpath.writelines(window_main.soft_path)
        file_softpath.close()

    def open_roadrunner(self):
        stri = '\n'
        if not os.path.exists(default_file.DEFAULT_ROADRUNNER_SOFT_DIR):
            msg_box = QMessageBox.information(QtWidgets.QWidget(), default_file.DISPLAY_WARN, default_file.DISPLAY_WARN_SELECT_SOFTWARE)
        else:
            soft_dir = []
            file_opensoft = open(default_file.DEFAULT_ROADRUNNER_SOFT_DIR, mode="r")
            soft_dir.append(file_opensoft.readline())
            file_opensoft.close()
            if not os.path.exists(stri.join(soft_dir)):
                msg_box = QMessageBox.information(QtWidgets.QWidget(), default_file.DISPLAY_WARN,
                                                  default_file.DISPLAY_WARN_RELOAD_SOFTWARE)
            else:
                new_thread = Thread(target=self.thread_open_soft)
                new_thread.start()

    def thread_open_soft(self):
        stri = "\n"
        soft_dir = []
        file_opensoft = open(default_file.DEFAULT_ROADRUNNER_SOFT_DIR, mode="r")
        soft_dir.append(file_opensoft.readline())
        file_opensoft.close()
        subprocess.Popen(stri.join(soft_dir))
        # subprocess.Popen(stri.join(soft_dir))
        # subprocess.getstatusoutput(soft_dir)
        # subprocess.Popen(stri.join(soft_dir), shell=False, close_fds=True)
        # subprocess.run(soft_dir)
        # subprocess.check_call(soft_dir, shell=True)
        # os.system(r + "'" + stri.join(soft_dir) + "'")
        # os.execv(soft_dir, ['', '2.txt'])
        # os.popen(stri.join(soft_dir))
        # win32api.ShellExecute(0, 'open', stri.join(soft_dir), '', '', 1)
        # handle = win32process.CreateProcess(soft_dir, '', None, None, 0, win32process.CREATE_NO_WINDOW,
        #                                    None, None, win32process.STARTUPINFO())


    # 点击按钮更新案例下载内容
    def case_update(self):
        self.case_download_show.clear()
        openx_case = os.listdir(default_file.DEFAULT_CASE_DIR)
        self.case_download_show.addItems(openx_case)

    # 点击按钮更新测试报告内容
    def report_update(self):
        self.report_show.clear()
        report = os.listdir(default_file.DEFAULT_REPORT_DIR)
        self.report_show.addItems(report)

    # 点击按钮更新测试里程内容
    def range_update(self):
        self.range_show.clear()
        range_dis = os.listdir(default_file.DEFAULT_RANGE_DIR)
        self.range_show.addItems(range_dis)