import os
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import subprocess
from window.window_main import Ui_MainWindow
from window import window_main, window_vtd
import default_file
import App_vtd
import App_carmaker
import App_prescan
import win32api
import win32process
import numpy as np
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
        self.openx_prescan_change.clicked.connect(self.show_prescan)
        self.select_software_dir.clicked.connect(self.get_soft_dir)
        self.open_software.clicked.connect(self.open_roadrunner)

        # self.case_down.clicked.connect(self.case_update)
        self.case_down.clicked.connect(self.download_time_cont)

        self.report.clicked.connect(self.report_update)
        self.range.clicked.connect(self.range_update)

        '''# 设置打开页面即进行案例下载显示
        self.case_download_show.clear()
        openx_case = os.listdir(default_file.DEFAULT_CASE_DIR)
        self.case_download_show.addItems(openx_case)'''
        self.download_time_cont()

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

    def show_prescan(self):
        self.prescan_window = App_prescan.presc_change()
        self.prescan_window.show()

    def download_time_cont(self):
        dwc_dir = default_file.DEFAULT_DWC_SOFT_DIR
        openx_case = os.listdir(default_file.DEFAULT_CASE_DIR)
        if not os.path.exists(dwc_dir):
            dwc_file = open(dwc_dir, mode='w')
            for case in openx_case:
                # name_por = os.path.basename(str(vtd_change.vtd_inputs[0][i]))
                portion = os.path.splitext(case)
                # print(portion)
                if 'xosc' in portion[1]:
                    dwc_file.write(case + ' 下载次数：' + '0' + '\n')
                    # line = next(dwc_file)
                elif portion[1] == '':
                    dwc_file.write(case + ' 下载次数：' + '0' + '\n')
                    # line = next(dwc_file)
            dwc_file.close()
        else:
            dwc_af = []
            dwc_file = open(dwc_dir, mode='r')
            for case in openx_case:
                af_set = 0
                for line in open(dwc_dir, mode='r'):
                    if case in line:
                        # print('in file')
                        af_set = 0
                        break
                    else:
                        af_set = 1
                        # dwc_af.append(case + ' 下载次数：' + '0' + '\n')
                if af_set == 1:
                    portion = os.path.splitext(case)
                    # print(portion)
                    if 'xosc' in portion[1]:
                        dwc_af.append(case + ' 下载次数：' + '0' + '\n')
                        # line = next(dwc_file)
                    elif portion[1] == '':
                        dwc_af.append(case + ' 下载次数：' + '0' + '\n')
            dwc_file.close()
            # print(dwc_af)
            dwc_write = open(dwc_dir, mode='a')
            for line in dwc_af:
                dwc_write.write(line)
            dwc_write.close()

        # self.download_time_add('C4_4ac.xosc')
        # cont_time = 0
        # line_time = []
        dwc_read = open(dwc_dir, mode='r')
        dwc_info = []
        for line in open(dwc_dir, mode='r'):
            line_info = line.replace('\n', '')
            # line_name = line_info.replace(' 下载次数：', '')
            # line_name = line_name.replace()
            dwc_info.append(line_info)
        dwc_read.close()
        # print(dwc_info)
        self.case_download_show.clear()
        self.case_download_show.addItems(dwc_info)

    def download_time_add(self, name):
        dwc_dir = default_file.DEFAULT_DWC_SOFT_DIR
        dwc_com = []
        dwc_change = open(dwc_dir, mode='r')
        for line in open(dwc_dir, mode='r'):
            if name in line:

                line_show = line.replace('\n', '')
                show_cont = 0
                # print(len(line_show))
                # print(line_show[18])
                '''for i in len(line_show):
                    if line_show[i] == ':':
                        show_cont = i
                        print(show_cont)'''
                # print(line_show[-2], line_show[-1])

                line_time = line.replace(name, '')
                line_time = line_time.replace(' 下载次数：', '')
                line_time = line_time.replace(' \n', '')
                cont_time = int(line_time)
                cont_time = cont_time + 1
                # print(cont_time)
                dwc_com.append(name + ' 下载次数：' + str(cont_time) + '\n')
                line = next(dwc_change)
                # print(dwc_com)
            else:
                dwc_com.append(dwc_change.readline())

        dwc_change.close()

        dwc_sum = open(dwc_dir, mode='w')
        dwc_sum.truncate()
        for line in dwc_com:
            dwc_sum.writelines(line)
        dwc_sum.close()

        # self.download_time_cont()
        new_thread = Thread(target=self.download_time_cont)
        new_thread.start()


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