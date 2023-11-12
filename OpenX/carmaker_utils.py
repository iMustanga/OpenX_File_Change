import sys
import os
from shutil import copy, copyfile
import xml.etree.ElementTree as ET
import Xml_change_followtrajectory
import Xml_change_dur
import Xml_changetools
import rd5_change
import Log_Output
import socket
# 2023.09.13 移除了对xosc文件进行改名的功能

class CarMakerUtils:
    def __init__(self,
                 cur_dir: str,
                 cmaker_dir: str,
                 file_name: str,
                 input_dir: str,
                 output_dir: str = '../output/',
                 cmaker_data_dir: str = 'Data',
                 cmaker_vehicle_dir: str = 'Vehicle',
                 cmaker_sensor_dir: str = 'Sensor',
                 cmaker_src_dir: str = 'src',
                 xosc_dir: str = 'Data_osc',
                 rd5_dir: str = 'Data/Road'):
        """
        :param cmaker_dir:CarMaker工程根目录
        :param input_dir:输入路径，就是存放xosc、xodr与osgb文件的路径
        :param output_dir:输出路径，默认输出到output/new_file_name_CarMaker文件夹中
        :param cmaker_data_dir:不建议更改，CarMaker工程的Data路径
        :param cmaker_vehicle_dir:不建议更改，CarMaker工程的Vehicle路径
        :param cmaker_sensor_dir:不建议更改，CarMaker工程的Sensor路径
        :param cmaker_src_dir:不建议更改，CarMaker工程的src路径
        :param xosc_dir:不建议更改，CarMaker工程的Data_osc路径
        :param rd5_dir:不建议更改，CarMaker工程的Data/Road路径
        """
        self.cur_dir = cur_dir
        self.cmaker_dir = cmaker_dir
        self.file_name = file_name
        self.input_dir = input_dir
        self.output_dir = os.path.join(output_dir, file_name + '_CarMaker')
        self.cmaker_data_dir = cmaker_data_dir
        self.cmaker_vehicle_dir = cmaker_vehicle_dir
        self.cmaker_sensor_dir = cmaker_sensor_dir
        self.cmaker_src_dir = cmaker_src_dir

        self.rd5_dir = rd5_dir
        self.xosc_dir = xosc_dir
        self.new_file_path_and_name = \
            os.path.join(cmaker_dir, xosc_dir, file_name + '.xosc')
        self.vehicle_model_database = cur_dir + "\\CarMaker_Vehicle"
        self.sensor_model_database = cur_dir + "\\CarMaker_Sensor"
        # 10.19修改
        self.model_database = cur_dir + "\\Carmaker_VehicleSensor"

        self.src_database = cur_dir + "\\CarMaker_Src"
        self.package_xosc_dir = None
        self.package_vehicle_dir = None
        self.package_sensor_dir = None
        self.package_src_dir = None
        self.package_others_dir = None

    def create_package(self):
        if not os.path.exists(self.output_dir):
            self.package_xosc_dir = os.path.join(self.output_dir, self.xosc_dir)
            self.package_vehicle_dir = os.path.join(self.output_dir, self.cmaker_data_dir, self.cmaker_vehicle_dir)
            self.package_sensor_dir = os.path.join(self.output_dir, self.cmaker_data_dir, self.cmaker_sensor_dir)
            self.package_src_dir = os.path.join(self.output_dir, self.cmaker_src_dir)
            self.package_others_dir = os.path.join(self.output_dir, "others")
            os.makedirs(self.package_xosc_dir)
            os.makedirs(self.package_vehicle_dir)
            os.makedirs(self.package_sensor_dir)
            os.makedirs(self.package_src_dir)
            os.makedirs(self.package_others_dir)
        else:
            self.package_xosc_dir = os.path.join(self.output_dir, self.xosc_dir)
            self.package_vehicle_dir = os.path.join(self.output_dir, self.cmaker_data_dir, self.cmaker_vehicle_dir)
            self.package_sensor_dir = os.path.join(self.output_dir, self.cmaker_data_dir, self.cmaker_sensor_dir)
            self.package_src_dir = os.path.join(self.output_dir, self.cmaker_src_dir)
            self.package_others_dir = os.path.join(self.output_dir, "others")
            return

    def copy_readme(self):
        readme_path = os.path.join(self.cur_dir, "CM_README.txt")
        if os.path.exists(readme_path) and os.path.exists(self.output_dir):
            copy(readme_path, os.path.join(self.output_dir, "CM_README.txt"))
        else:
            return

    def copy_xodr_and_osgb(self):
        old_xodr_file_path = os.path.join(self.input_dir, self.file_name + '.xodr')
        old_osgb_file_path = os.path.join(self.input_dir, self.file_name + '.osgb')
        # xodr与osgb文件需要存放到Data_osc目录下
        new_xodr_file_path = os.path.join(self.cmaker_dir, self.xosc_dir, self.file_name + '.xodr')
        new_osgb_file_path = os.path.join(self.cmaker_dir, self.xosc_dir, self.file_name + '.osgb')
        copy(old_xodr_file_path, new_xodr_file_path)
        # osgb文件不是必备的
        if os.path.exists(old_osgb_file_path):
            copy(old_osgb_file_path, new_osgb_file_path)
        # 打包xodr与osgb文件
        if os.path.exists(self.output_dir):
            copy(new_xodr_file_path, os.path.join(self.output_dir, self.file_name + '.xodr'))
            if os.path.exists(old_osgb_file_path):
                copy(new_osgb_file_path, os.path.join(self.output_dir, self.file_name + '.osgb'))
        else:
            return

    # 10.24修改 加入src打包
    def copy_models(self, model_name: str):
        model_file_path = os.path.join(self.model_database, model_name)
        # 获取文件夹下的所有子文件夹
        file_names = os.listdir(model_file_path)
        for file_name in file_names:
            if file_name == 'vehicle':
                Vehicle_file_path = os.path.join(model_file_path, file_name)
                vehicle_name = os.listdir(Vehicle_file_path)
                for vehicle in vehicle_name:
                    Vehicle_file_paths = os.path.join(Vehicle_file_path, vehicle)
                    cmaker_vehicle_model_path = os.path.join(self.cmaker_dir, self.cmaker_data_dir,
                                                             self.cmaker_vehicle_dir)
                    copy(Vehicle_file_paths, cmaker_vehicle_model_path)
                    if os.path.exists(self.package_vehicle_dir):
                        copy(Vehicle_file_paths, os.path.join(self.package_vehicle_dir))

            if file_name == 'sensor':
                Sensor_file_path = os.path.join(model_file_path, file_name)
                sensor_name = os.listdir(Sensor_file_path)
                for sensor in sensor_name:
                    Sensor_file_paths = os.path.join(Sensor_file_path, sensor)
                    cmaker_sensor_model_path = os.path.join(self.cmaker_dir, self.cmaker_data_dir,
                                                            self.cmaker_sensor_dir)
                    copy(Sensor_file_paths, cmaker_sensor_model_path)
                    if os.path.exists(self.package_sensor_dir):
                        copy(Sensor_file_paths, os.path.join(self.package_sensor_dir))

            if file_name == 'src':
                Src_file_path = os.path.join(model_file_path, file_name)
                src_name = os.listdir(Src_file_path)
                for src in src_name:
                    Src_file_paths = os.path.join(Src_file_path, src)
                    cmaker_src_model_path = os.path.join(self.cmaker_dir, self.cmaker_src_dir)
                    copy(Src_file_paths, cmaker_src_model_path)
                    if os.path.exists(self.package_src_dir):
                        copy(Src_file_paths, os.path.join(self.package_src_dir))

    def xosc_change(self, vehicle_model_name: str):
        # 接入xosc转换API
        # 包含最终文件的输入路径
        input_file_and_name = os.path.join(self.input_dir, self.file_name + '.xosc')
        # 新文件需要存放到Data_osc目录下
        new_file_path = os.path.join(self.cmaker_dir, self.xosc_dir)
        # 包含最终文件的输出路径
        new_file_path_and_name = os.path.join(new_file_path, self.file_name + '.xosc')

        tree = ET.ElementTree(file=input_file_and_name)
        root = tree.getroot()
        duration = 0
        for i in root.findall('.//Condition'):
            if i.get('name') == "Duration":
                duration += 1
        # 2023.09.03
        # 1.Condition类型为duration condition
        if duration != 0:
            Xml_change_dur.dur(self.file_name, cm_vehicle_model=vehicle_model_name,
                                input_dir=input_file_and_name,
                                output_dir=new_file_path_and_name,
                                cmaker_dir=self.cmaker_dir)
            Xml_change_followtrajectory.tra(self.file_name, cm_vehicle_model=vehicle_model_name,
                                input_dir=input_file_and_name,
                                output_dir=new_file_path_and_name,
                                cmaker_dir=self.cmaker_dir)
        # 2.FollowTrajectory
        elif root.find('.//FollowTrajectoryAction') is not None and len(root.findall('.//Private')) > 1:
            Xml_changetools.change(self.file_name, cm_vehicle_model=vehicle_model_name,
                                 input_dir=input_file_and_name,
                                 output_dir=new_file_path_and_name,
                                 cmaker_dir=self.cmaker_dir)
            Xml_change_followtrajectory.tra(self.file_name, cm_vehicle_model=vehicle_model_name,
                                 input_dir=input_file_and_name,
                                 output_dir=new_file_path_and_name,
                                 cmaker_dir=self.cmaker_dir)

        elif root.find('.//FollowTrajectoryAction') is not None and len(root.findall('.//Private')) == 1:
            Xml_change_followtrajectory.tra(self.file_name, cm_vehicle_model=vehicle_model_name,
                                 input_dir=input_file_and_name,
                                 output_dir=new_file_path_and_name,
                                 cmaker_dir=self.cmaker_dir)
        # 3.Condition类型为simulationtime condition
        else:
            Xml_changetools.change(self.file_name, cm_vehicle_model=vehicle_model_name,
                                 input_dir=input_file_and_name,
                                 output_dir=new_file_path_and_name,
                                 cmaker_dir=self.cmaker_dir)

    def rd5_file_change(self):
        # 接入rd5转换API
        # 包含最终文件的输入路径
        input_file_and_name = os.path.join(self.input_dir, self.file_name + '.xodr')
        # 新文件需要存放到Data/Road目录下
        new_file_path = os.path.join(self.cmaker_dir, self.rd5_dir)
        # 包含最终文件的输出路径
        new_file_path_and_name = os.path.join(new_file_path, self.file_name + '.rd5')
        rd5_change.road_change(input_xodr_file_and_name=input_file_and_name,new_rd5_file_path_and_name=new_file_path_and_name)

    def Log_dir(self):
        Log_Output.write_dir_path_to_file(self.cmaker_dir+'/SimOutput/{}/Log'.format(socket.gethostname()))

    def carmaker_process(self, model_name, src=None):
        self.create_package()
        self.copy_readme()
        self.copy_xodr_and_osgb()
        self.copy_models(model_name)
        self.xosc_change(model_name)
        self.rd5_file_change()
        self.Log_dir()
        # print("debug")
