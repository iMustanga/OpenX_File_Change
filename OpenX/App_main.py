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

        # 案例下载次数统计
        # self.case_down.clicked.connect(self.case_update)
        self.case_down.clicked.connect(self.download_time_cont)
        self.download_time_cont()

        # 测试里程统计
        # self.range.clicked.connect(self.range_update)test_range_stat
        self.range.clicked.connect(self.test_range_stat)
        self.test_range_stat()
        self.range_zero.clicked.connect(self.test_range_zero)

        # 测试报告获取
        self.report.clicked.connect(self.report_update)

        # 设置打开页面即进行测试报告显示
        self.report_show.clear()
        report = os.listdir(default_file.DEFAULT_REPORT_DIR)
        self.report_show.addItems(report)

    def show_vtd(self):
        self.vtd_window = App_vtd.vtd_change()
        self.vtd_window.show()

    def show_carmaker(self):
        self.carmaker_window = App_carmaker.window_carmaker_change()
        self.carmaker_window.show()

    def show_prescan(self):
        self.prescan_window = App_prescan.presc_change()
        self.prescan_window.show()

    def test_range_stat(self):
        # trs_dir = os.path.abspath(os.path.dirname(os.getcwd())) + "\\log"
        log_path = []
        log_dir = default_file.DEFAULT_LOG_DIR # 'E:\RLearning\VTD\OpenX_V8.4.2\OpenX_FileChange\log_path.txt'
        # 新建文件存储数据
        if not os.path.exists(default_file.DEFAULT_TRS_SOFT_DIR):
            trs_make = open(default_file.DEFAULT_TRS_SOFT_DIR, mode='w')
            trs_make.write('测试总里程： 0m \n')
            trs_make.close()
        if not os.path.exists(default_file.DEFAULT_TRS_CHECK_SOFT_DIR):
            trs_check = open(default_file.DEFAULT_TRS_CHECK_SOFT_DIR, mode='w')
            trs_check.close()

        if os.path.exists(log_dir):
            path_read = open(log_dir, mode='r')
            for lane in open(log_dir, mode='r'):
                lane_write = lane.replace('\n', '')
                lane_write = lane_write.replace(' ', '')
                log_path.append(lane_write)
            path_read.close()
        else:
            print('路径文件不存在')
            # msg_box = QMessageBox.information(QtWidgets.QWidget(), default_file.DISPLAY_WARN, '未导出carmaker')

        if not log_path == []:
            for file_dir in log_path:
                if os.path.exists(file_dir):
                    print(file_dir)
                    # 对文件夹内文件进行遍历
                    range_log = os.listdir(file_dir)
                    # done_file = []
                    # print(range_log)
                    for log in range_log:
                        portion = os.path.splitext(log)
                        done_file = []
                        done_sta = 0
                        # 后缀为.log文件时进行遍历
                        if 'log' in portion[1]:
                            # 验证是否遍历过该文件
                            done_check = open(default_file.DEFAULT_TRS_CHECK_SOFT_DIR, mode='r')
                            for check in open(default_file.DEFAULT_TRS_CHECK_SOFT_DIR, mode='r'):
                                if log in check:
                                    done_sta = 1
                            done_check.close()

                            if done_sta == 0:

                                # 将当前遍历文件的文件名写入已遍历文件存储
                                done_file.append(log)
                                done_write = open(default_file.DEFAULT_TRS_CHECK_SOFT_DIR, mode='a')
                                for done in done_file:
                                    done_write.write(done + '\n')
                                done_write.close()

                                # 读取场景名称以及测试距离
                                trs_read = open(file_dir + '\\' + log, mode='r')
                                for line in open(file_dir + '\\' + log, mode='r'):
                                    if 'SIM_END' in line:
                                        # sim_range = line.replace('SIM_END', '')
                                        sim_range = []
                                        line_m = 0
                                        line_s = 0
                                        line_na0 = 0
                                        line_na1 = 0
                                        text_len = len(line) - 1
                                        # print(line)
                                        for i in range(text_len, -1, -1):
                                            if 'm' in line[i]:
                                                if line_m == 0:
                                                    line_m = i

                                            if 's' in line[i]:
                                                if line_s == 0:
                                                    line_s = i

                                            if '	' in line[i]:
                                                if not line_na1 == 0:
                                                    if line_na0 == 0:
                                                        # print('blank0')
                                                        line_na0 = i

                                            if '	' in line[i]:
                                                # print('blank')
                                                if not line_s == 0:
                                                    if line_na1 == 0:
                                                        # print('blank1')
                                                        line_na1 = i

                                        # sim_range.append(line[i])
                                        sim_range_mid = line[line_s + 2:line_m]
                                        sim_range = sim_range_mid.replace('	', '')
                                        sim_range = float(sim_range)
                                        # print(sim_range)

                                        sim_name = line[line_na0:line_na1]
                                        sim_name = sim_name.replace('	', '')
                                        # print(sim_name)

                                        # 若距离不为0 且场景名称不为空则写入数据
                                        if not sim_range == 0:
                                            if ' ' not in sim_name:
                                                openx_case = os.listdir(default_file.DEFAULT_CASE_DIR)
                                                if sim_name in openx_case:

                                                    # 总里程统计
                                                    total_temp = []
                                                    trs_total_read = open(default_file.DEFAULT_TRS_SOFT_DIR, mode='r')
                                                    for tol_ran in open(default_file.DEFAULT_TRS_SOFT_DIR, mode='r'):
                                                        if '总里程' in tol_ran:
                                                            total_range = tol_ran.replace('测试总里程：', '')
                                                            total_range = total_range.replace('m', '')
                                                            total_range = total_range.replace(' ', '')
                                                            total_range = total_range.replace('\n', '')
                                                            cont_total = float(total_range)
                                                            new_total = cont_total + sim_range
                                                            total_temp.append('测试总里程： ' + str(new_total) + 'm \n')
                                                            line = next(trs_total_read)
                                                        else:
                                                            total_temp.append(trs_total_read.readline())
                                                    trs_total_read.close()

                                                    trs_total_write = open(default_file.DEFAULT_TRS_SOFT_DIR, mode='w')
                                                    for total in total_temp:
                                                        trs_total_write.writelines(total)
                                                    trs_total_write.close()

                                                    # 写入各场景测试距离
                                                    check_sta = 0
                                                    trs_check = open(default_file.DEFAULT_TRS_SOFT_DIR, mode='r')
                                                    for sim in open(default_file.DEFAULT_TRS_SOFT_DIR, mode='r'):
                                                        if sim_name in sim:
                                                            check_sta = 1
                                                    trs_check.close()

                                                    # 若该场景未存储于数据文件内，则新建行写入数据
                                                    if check_sta == 0:
                                                        print(sim_range)
                                                        print(sim_name)
                                                        trs_write = open(default_file.DEFAULT_TRS_SOFT_DIR, mode='a')
                                                        trs_write.write(sim_name + ' 测试里程：' + str(sim_range) + 'm \n')
                                                        trs_write.close()

                                                    # 若该场景已经存在于数据文件内，则对测试里程进行相加处理
                                                    if check_sta == 1:
                                                        # 单场景里程统计
                                                        trs_com = []
                                                        trs_read = open(default_file.DEFAULT_TRS_SOFT_DIR, mode='r')
                                                        for case in open(default_file.DEFAULT_TRS_SOFT_DIR, mode='r'):
                                                            if sim_name in case:
                                                                print("find!")
                                                                case_range = case.replace(sim_name, '')
                                                                case_range = case_range.replace(' 测试里程：', '')
                                                                case_range = case_range.replace('\n', '')
                                                                case_range = case_range.replace(' ', '')
                                                                case_range = case_range.replace('m', '')
                                                                cont_range = float(case_range)
                                                                cont_range = cont_range + sim_range
                                                                trs_com.append(
                                                                    sim_name + ' 测试里程：' + str(cont_range) + 'm \n')
                                                                line = next(trs_read)
                                                                # print(dwc_com)
                                                            else:
                                                                trs_com.append(trs_read.readline())
                                                        trs_read.close()

                                                        trs_sum = open(default_file.DEFAULT_TRS_SOFT_DIR, mode='w')
                                                        trs_sum.truncate()
                                                        for comp in trs_com:
                                                            trs_sum.writelines(comp)
                                                        trs_sum.close()

                                trs_read.close()
                                # name_ck = line[0:j]
                else:
                    msg_box = QMessageBox.information(QtWidgets.QWidget(), default_file.DISPLAY_WARN,
                                                      '当前Log文件路径不存在：\n' + file_dir)

        # 调用数据到显示框
        trs_read = open(default_file.DEFAULT_TRS_SOFT_DIR, mode='r')
        trs_info = []
        for line in open(default_file.DEFAULT_TRS_SOFT_DIR, mode='r'):
            line_info = line.replace('\n', '')
            # line_name = line_info.replace(' 下载次数：', '')
            # line_name = line_name.replace()
            trs_info.append(line_info)
        trs_read.close()
        # print(dwc_info)
        self.range_show.clear()
        self.range_show.addItems(trs_info)


    def test_range_zero(self):
        total_temp = []

        keep_temp = []
        trs_keep_read = open(default_file.DEFAULT_TRS_SOFT_DIR, mode='r')
        for line in open(default_file.DEFAULT_TRS_SOFT_DIR, mode='r'):
            keep_temp.append(trs_keep_read.readline())
        trs_keep_read.close()
        trs_keep_write = open(default_file.DEFAULT_TRS_OLD_SOFT_DIR, mode='w')
        for keep in keep_temp:
            trs_keep_write.writelines(keep)
        trs_keep_write.close()



        trs_total_read = open(default_file.DEFAULT_TRS_SOFT_DIR, mode='r')
        for tol_ran in open(default_file.DEFAULT_TRS_SOFT_DIR, mode='r'):
            if '总里程' in tol_ran:
                '''total_range = tol_ran.replace('测试总里程：', '')
                total_range = total_range.replace('m', '')
                total_range = total_range.replace(' ', '')
                total_range = total_range.replace('\n', '')
                cont_total = float(total_range)
                new_total = cont_total + sim_range'''
                total_temp.append('测试总里程： ' + '0' + 'm \n')
                line = next(trs_total_read)
            else:
                total_temp.append(trs_total_read.readline())
        trs_total_read.close()

        trs_total_write = open(default_file.DEFAULT_TRS_SOFT_DIR, mode='w')
        for total in total_temp:
            trs_total_write.writelines(total)
        trs_total_write.close()

        # 调用数据到显示框
        trs_read = open(default_file.DEFAULT_TRS_SOFT_DIR, mode='r')
        trs_info = []
        for line in open(default_file.DEFAULT_TRS_SOFT_DIR, mode='r'):
            line_info = line.replace('\n', '')
            # line_name = line_info.replace(' 下载次数：', '')
            # line_name = line_name.replace()
            trs_info.append(line_info)
        trs_read.close()
        # print(dwc_info)
        self.range_show.clear()
        self.range_show.addItems(trs_info)



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

            name_set = 0
            dwc_st = []
            dwc_check = open(dwc_dir, mode='r')
            for line in open(dwc_dir, mode='r'):
                j = 0
                for i in line:
                    if i == ' ':

                        name_ck = line[0:j]
                        name_in = str(name_ck)
                        for case in openx_case:
                            # name_in = str(name_ck)
                            if name_in in case:
                                # print(name_in)
                                name_set = 1
                                # print(i)
                    j = j + 1

                if name_set == 0:
                    # line = next(dwc_file)
                    
                    print('min')
                    name_set = 0
                else:
                    dwc_st.append(dwc_check.readline())
                    # print(dwc_st)
                    name_set = 0
            dwc_check.close()

            dwc_min = open(dwc_dir, mode='w')
            for line in dwc_st:
                dwc_min.write(line)
            dwc_min.close()

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