import sys
import os
from shutil import copy, copyfile
import xml.etree.ElementTree as ET
import Xml_change_followtrajectory
import Xml_change_dur
import Xml_changetools


class CarMakerUtils:
    def __init__(self,
                 cmaker_dir: str,
                 new_file_name: str,
                 old_file_name: str,
                 input_dir: str,
                 output_dir: str = '../output/',
                 cmaker_data_dir: str = 'Data',
                 cmaker_vehicle_dir: str = 'Vehicle',
                 cmaker_sensor_dir: str = 'Sensor',
                 cmaker_src_dir: str = 'src',
                 xosc_dir: str = 'Data_osc'):
        """
        :param cmaker_dir:CarMaker工程根目录
        :param new_file_name:新文件名
        :param input_dir:输入路径，就是存放xosc、xodr与osgb文件的路径
        :param output_dir:输出路径，默认输出到output/new_file_name_CarMaker文件夹中
        :param cmaker_data_dir:不建议更改，CarMaker工程的Data路径
        :param cmaker_vehicle_dir:不建议更改，CarMaker工程的Vehicle路径
        :param cmaker_sensor_dir:不建议更改，CarMaker工程的Sensor路径
        :param cmaker_src_dir:不建议更改，CarMaker工程的src路径
        :param xosc_dir:不建议更改，CarMaker工程的Data_osc路径
        """
        self.cmaker_dir = cmaker_dir
        self.new_file_name = new_file_name
        self.old_file_name = old_file_name
        self.input_dir = input_dir
        self.output_dir = os.path.join(output_dir, new_file_name + '_CarMaker')
        self.cmaker_data_dir = cmaker_data_dir
        self.cmaker_vehicle_dir = cmaker_vehicle_dir
        self.cmaker_sensor_dir = cmaker_sensor_dir
        self.cmaker_src_dir = cmaker_src_dir

        self.xosc_dir = xosc_dir
        self.new_file_path_and_name = \
            os.path.join(cmaker_dir, xosc_dir, new_file_name + '.xosc')
        self.vehicle_model_database = "../CarMaker_Vehicle"
        self.sensor_model_database = "../CarMaker_Sensor"
        self.src_database = "../CarMaker_Src"
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
            return

    def copy_readme(self):
        if os.path.exists("../CM_README.txt") and os.path.exists(self.output_dir):
            copy("../CM_README.txt", os.path.join(self.output_dir, "CM_README.txt"))
        else:
            return

    def copy_xodr_and_osgb(self):
        old_xodr_file_path = os.path.join(self.input_dir, self.old_file_name + '.xodr')
        old_osgb_file_path = os.path.join(self.input_dir, self.old_file_name + '.osgb')
        # xodr与osgb文件需要存放到Data_osc目录下
        new_xodr_file_path = os.path.join(self.cmaker_dir, self.xosc_dir, self.old_file_name + '.xodr')
        new_osgb_file_path = os.path.join(self.cmaker_dir, self.xosc_dir, self.old_file_name + '.osgb')
        copy(old_xodr_file_path, new_xodr_file_path)
        copy(old_osgb_file_path, new_osgb_file_path)
        # 打包xodr与osgb文件
        if os.path.exists(self.output_dir):
            copy(new_xodr_file_path, os.path.join(self.output_dir, self.xosc_dir, self.old_file_name + '.xodr'))
            copy(new_osgb_file_path, os.path.join(self.output_dir, self.xosc_dir, self.old_file_name + '.osgb'))
        else:
            return

    def copy_vehicle_models(self, vehicle_model_name: str):
        vehicle_model_file_path = os.path.join(self.vehicle_model_database, vehicle_model_name)
        cmaker_vehicle_model_path = os.path.join(self.cmaker_dir, self.cmaker_data_dir,
                                                 self.cmaker_vehicle_dir, vehicle_model_name)
        copy(vehicle_model_file_path, cmaker_vehicle_model_path)
        # 打包vehicle_models文件
        if os.path.exists(self.package_vehicle_dir):
            copy(vehicle_model_file_path, os.path.join(self.package_vehicle_dir, vehicle_model_name))
        else:
            return

    def copy_sensor_models(self, sensor_name=None):
        if sensor_name is not None:
            sensor_model_file_path = os.path.join(self.sensor_model_database, sensor_name)
            cmaker_sensor_model_path = os.path.join(self.cmaker_dir, self.cmaker_data_dir,
                                                     self.cmaker_sensor_dir, sensor_name)
            copy(sensor_model_file_path, cmaker_sensor_model_path)
            # 打包sensor_models文件
            if os.path.exists(self.package_vehicle_dir):
                copy(sensor_model_file_path, os.path.join(self.package_vehicle_dir, sensor_name))
            else:
                return

    def copy_cm_src(self):
        # @TODO
        pass

    def xosc_change(self, vehicle_model_name: str):
        # 接入xosc转换API
        input_file_and_name = os.path.join(self.input_dir, self.old_file_name + '.xosc')
        # 新文件需要存放到Data_osc目录下
        new_file_path = os.path.join(self.cmaker_dir, self.xosc_dir)
        new_file_path_and_name = os.path.join(new_file_path, self.new_file_name + '.xosc')

        tree = ET.ElementTree(file=input_file_and_name)
        root = tree.getroot()
        duration = 0
        for i in root.findall('.//Condition'):
            if i.get('name') == "Duration":
                duration += 1
        # 2023.09.03
        # 1.Condition类型为duration condition
        if duration != 0:
            Xml_change_dur.main(self.new_file_name, cm_vehicle_model=vehicle_model_name,
                                input_dir=input_file_and_name,
                                output_dir=new_file_path_and_name,
                                cmaker_dir=self.cmaker_dir)
        # 2.FollowTrajectory
        elif root.find('.//FollowTrajectoryAction') is not None:
            Xml_change_followtrajectory.main(self.new_file_name, cm_vehicle_model=vehicle_model_name,
                                             input_dir=input_file_and_name,
                                             output_dir=new_file_path_and_name,
                                             cmaker_dir=self.cmaker_dir)
        # 3.Condition类型为simulationtime condition
        else:
            Xml_changetools.main(self.new_file_name, cm_vehicle_model=vehicle_model_name,
                                 input_dir=input_file_and_name,
                                 output_dir=new_file_path_and_name,
                                 cmaker_dir=self.cmaker_dir)

    def carmaker_process(self, vehicle_model_name, sensor_name=None, src=None):
        self.create_package()
        self.copy_readme()
        self.copy_xodr_and_osgb()
        self.copy_vehicle_models(vehicle_model_name)
        self.copy_sensor_models(sensor_name)
        self.copy_cm_src()
        self.xosc_change(vehicle_model_name)
        # print("debug")



