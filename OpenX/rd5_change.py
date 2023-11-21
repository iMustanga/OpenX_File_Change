import re
import subprocess
import xml.etree.ElementTree as ET
import os
import sys
import pathlib
import shutil
import math
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
'''------------此模块功能为通过矩形的中心点坐标，长和宽以及偏转角来计算出四个顶点的坐标-------'''
def calculate_rectangle_vertices(x, y, angle, width, length):
    # 将角度转换为弧度
    angle_rad = angle+math.pi/2

    # 长方形的半宽和半长
    half_width = width / 2
    half_length = length / 2

    # 长方形的中心点坐标
    center_x = x
    center_y = y

    # 计算4个顶点的坐标
    vertex1_x = center_x + half_width * math.cos(angle_rad) - half_length * math.sin(angle_rad)
    vertex1_y = center_y + half_width * math.sin(angle_rad) + half_length * math.cos(angle_rad)

    vertex2_x = center_x - half_width * math.cos(angle_rad) - half_length * math.sin(angle_rad)
    vertex2_y = center_y - half_width * math.sin(angle_rad) + half_length * math.cos(angle_rad)

    vertex3_x = center_x - half_width * math.cos(angle_rad) + half_length * math.sin(angle_rad)
    vertex3_y = center_y - half_width * math.sin(angle_rad) - half_length * math.cos(angle_rad)

    vertex4_x = center_x + half_width * math.cos(angle_rad) + half_length * math.sin(angle_rad)
    vertex4_y = center_y + half_width * math.sin(angle_rad) - half_length * math.cos(angle_rad)

    return [(vertex1_x, vertex1_y), (vertex4_x, vertex4_y), (vertex3_x, vertex3_y), (vertex2_x, vertex2_y)]

'''------此模块功能是读取opendrive文件，然后将要添加的车道线提取出来------'''
def road_change(input_xodr_file_and_name,new_rd5_file_path_and_name):
    IDs = []
    try:
        '''--------------此模块功能为将所有的物体的ID提取出来，这些ID不能用，否则新增的物体不显示----------'''
        with open(new_rd5_file_path_and_name, 'r+') as datas:
            data = datas.read()
            # 使用正则表达式提取所有的 ID 号码
            id_numbers = re.findall(r'ID = (\d+)', data)
            pattern = r'RL\.\d+\.RoadMarking\.(\d+)\.ID = \d+'
            markingID = re.findall(pattern, data)
            markingIDs = [int(match) for match in markingID]
            # 输出提取的 ID 号码
            for id_number in id_numbers:
                IDs.append(int(id_number))
            # print(markingIDs)
            # print(IDs)
        xodr_file_path=input_xodr_file_and_name
        #rd5_file= cmaker_dir+"/Data/Road/"+rd5_file_name
        tree = ET.ElementTree(file=xodr_file_path)
        root = tree.getroot()
        points=[]
        time=6666
        for child in root.findall('.//object'):
            if child.find('.//parkingSpace') is not None:
                s=round(float(child.get('s')),10)
                t=round(float(child.get('t')),10)
                width=round(float(child.get('width')),10)
                length=round(float(child.get('length')),10)
                zoffset=float(child.get('zOffset'))
                hdg=round(float(child.get('hdg')),10)
                roll=float(child.get('roll'))
                pitch=float(child.get('pitch'))
                orientation=child.get('orientation')
                type=child.get('type')
                vertices=calculate_rectangle_vertices(s,t,hdg,width,length)
                # print(vertices)
                points.append(vertices)
                # 计算每条直线的表达式
                lines = []

                for i in range(4):
                    start_point = vertices[i]
                    end_point = vertices[(i + 1) % 4]  # 循环到下一个顶点
                    # 计算矢量
                    vector = (end_point[0] - start_point[0], end_point[1] - start_point[1])
                    line_expression = f"{start_point} + {vector}"
                    # print(line_expression)
                    marking_id=markingIDs[-1]+1
                    markingIDs.append(marking_id)
                    str ='''
    RL.1.RoadMarking.{}.ID = {} 11
    RL.1.RoadMarking.{} = {} 0 0 1 {} 100 0.15 0 1 1 0 2 4 1 1 0 ""
    RL.1.RoadMarking.{}.Material.0 = 1.0,1.0,1.0 0 0 0 0 0 0 0 0 0 0 0'
    RL.1.RoadMarking.{}.PointList:
        0 0
        {} {}'''.format(marking_id,time,marking_id,start_point[0],start_point[1],marking_id,marking_id,vector[0],vector[1])
                    # print(str)
                    time=time+1
                    with open(new_rd5_file_path_and_name,'a') as road:
                        road.write(str)
                        road.close()
    except Exception as e:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("发生异常!")
        msg.setInformativeText(f"rd5文件未写入")
        msg.setWindowTitle("错误提示")
        # 设置消息框的最小和最大大小范围
        msg.exec_()
        return