import subprocess
import xml.etree.ElementTree as ET
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\CarMaker_PythonAPI\\python3.8")
import cmapi
import pathlib
import shutil
def tra(file_name, cm_vehicle_model, input_dir, output_dir, cmaker_dir):

    xosc_name = file_name+'.xosc'
    # 构建文件路径
    old_file_path = input_dir
    file_path = cmaker_dir + "/Data_osc/" + xosc_name
    if not os.path.exists(file_path):
        shutil.copy(old_file_path, file_path)
    new_file_path = output_dir
    Trajectory_file = cmaker_dir + "/Data_osc/Catalogs/Trajectory/" + xosc_name
    testrun_file = cmaker_dir + "/Data/TestRun/" + file_name

    old_tree=ET.ElementTree(file=old_file_path)
    tree = ET.ElementTree(file=file_path)
    old_root=old_tree.getroot()
    root=tree.getroot()
    elements_to_remove = []
    #提取出Trajectory标签中的内容
    trajectory_content=old_root.find('.//Trajectory')
    #提取出time=0时的初始位置
    ori_points=None
    tra_car = None
    for privatecar in old_root.findall('.//Private'):
        for points in old_root.findall('.//Vertex'):
            if float(points.attrib.get('time'))==0:
                ori_points=points
                tra_car = privatecar.attrib.get('entityRef')
    print(tra_car)
    #以下是t=0时的车辆初始位置
    ori_points=ori_points.find('.//WorldPosition')
    x=ori_points.attrib.get('x')
    y=ori_points.attrib.get('y')
    z=ori_points.attrib.get('z')
    h=ori_points.attrib.get('h')
    p=ori_points.attrib.get('p')
    r=ori_points.attrib.get('r')
    #添加的位置信息文本
    ori_points_str="""
                        <PrivateAction>
                            <TeleportAction>
                            <Position>
                                <WorldPosition x="{}" y="{}" z="{}" h="{}" p="{}" r="{}"/>
                            </Position>
                            </TeleportAction>
                        </PrivateAction>
    """.format(x,y,z,h,p,r)
    private_position=root.findall('.//Private')
    for abc in private_position:
        print(abc.attrib)
        if abc.attrib.get('entityRef')==tra_car:
            abc.insert(-1,ET.fromstring(ori_points_str))
            break

    # 头文件参数声明文本
    ParameterDeclarations="""
        <ParameterDeclarations>
            <ParameterDeclaration name="owner" parameterType="string" value="Ego1" />
        </ParameterDeclarations>
    """
    #先删除掉原有的Para
    root.remove(root.find('.//ParameterDeclarations'))

    root.insert(1,ET.fromstring(ParameterDeclarations))
    Story=root.find('.//Story')
    Story.insert(0,ET.fromstring(ParameterDeclarations))


    #路径信息文本
    trajectory_str="""
        <CatalogLocations>
            <VehicleCatalog>
                <Directory path="./Catalogs/Vehicles" />
            </VehicleCatalog>
            <PedestrianCatalog>
                <Directory path="./Catalogs/Pedestrians" />
            </PedestrianCatalog>
            <TrajectoryCatalog>
                <Directory path="./Catalogs/Trajectory" />
            </TrajectoryCatalog>
            <ControllerCatalog>
                <Directory path="./Catalogs/Controllers" />
            </ControllerCatalog>
        </CatalogLocations>
    """
    #先删除掉原有的CatalogLocations
    root.remove(root.find('.//CatalogLocations'))
    root.insert(2,ET.fromstring(trajectory_str))
    # 查找并删除<Trajectory>标签及其内容
    for follow_trajectory_action in root.findall(".//PrivateAction"):
        for trajectory in follow_trajectory_action.findall(".//RoutingAction"):
            follow_trajectory_action.remove(trajectory)
    # print(trajectory_content)

    Car=[]
    for Main in old_root.find('.//Storyboard').findall('.//Private'):
        if Main.find('.//Vertex') is not None:
            Car.append(Main.attrib.get('entityRef'))
        # print(Main)
    #print(Car)
    car=Car[0]

    #需要添加的Act文本
    Act="""
                <Act name="MyAct">
                    <ManeuverGroup maximumExecutionCount="1" name="MySequence">
                        <Actors selectTriggeringEntities="false">
                            <EntityRef entityRef="{}"/>
                        </Actors>
                        <Maneuver name="ManeuverFollowTrajectoryAction{}_1">
                            <Event maximumExecutionCount="1" name="EventFollowTrajectoryActionEgo_1" priority="overwrite">
                                <Action name="ActionFollowTrajectoryAction{}_1">
                                    <PrivateAction>
                                        <RoutingAction>
                                            <FollowTrajectoryAction>
                                                <TimeReference>
                                                    <Timing domainAbsoluteRelative="absolute" offset="0.0" scale="1.0" />
                                                </TimeReference>
                                                <TrajectoryFollowingMode followingMode="follow" />
                                                <CatalogReference catalogName="TrajectoryCatalog" entryName="{}_Trajectory" />
                                            </FollowTrajectoryAction>
                                        </RoutingAction>
                                    </PrivateAction>
                                </Action>
                                <StartTrigger>
                                    <ConditionGroup>
                                        <Condition conditionEdge="none" delay="0" name="FollowTrajectory">
                                            <ByValueCondition>
                                                <SimulationTimeCondition rule="greaterThan" value="0" />
                                            </ByValueCondition>
                                        </Condition>
                                    </ConditionGroup>
                                </StartTrigger>
                            </Event>
                        </Maneuver>
                    </ManeuverGroup>
                    <StartTrigger>
                        <ConditionGroup>
                            <Condition name="" delay="0" conditionEdge="rising">
                                <ByValueCondition>
                                    <SimulationTimeCondition value="0" rule="greaterThan"/>
                                </ByValueCondition>
                            </Condition>
                        </ConditionGroup>
                    </StartTrigger>
                    <StopTrigger>
                        <ConditionGroup>
                            <Condition conditionEdge="none" delay="0" name="FollowTrajectory">
                                <ByValueCondition>
                                    <SimulationTimeCondition rule="greaterThan" value="10e15" />
                                </ByValueCondition>
                            </Condition>
                        </ConditionGroup>
                    </StopTrigger>
                </Act>
    """.format(car,car,car,car)
    #先删除掉原有的Act
    # for child in Story:
    #     if child.tag=='Act':
    #         Story.remove(child)
    Story.insert(1,ET.fromstring(Act))
    #修改仿真时间
    Storyboard=root.find('.//Storyboard')
    stoptrigger = Storyboard.find('StopTrigger')
    byvaluecondition = stoptrigger.find('.//ByValueCondition')
    simulationtime = byvaluecondition.find('.//SimulationTimeCondition')
    time="""
                            <SimulationTimeCondition value="6.0000000000000000e+2" rule="greaterThan" />
    """
    byvaluecondition.remove(simulationtime)
    byvaluecondition.append(ET.fromstring(time))
    #写入修改后的新文件
    tree.write(new_file_path)
#添加头文件描述，这样vscode就可以识别出是xml代码
    with open(new_file_path, 'r') as file:
        file_contents = file.read()
    # 在内容开头插入指定的文本行
    inserted_line = '<?xml version="1.0" encoding="UTF-8"?>\n'
    file_contents = inserted_line + file_contents

    # 再次打开文件以写入修改后的内容
    with open(new_file_path, 'w') as file:
        file.write(file_contents)
        file.close()



    #创建Trajectory文件并且写入路径内容
    xml_content="""
    <OpenSCENARIO>
      <FileHeader author="IPG Automotive GmbH" date="2021-11-24T09:38:23" description="Example of FollowTrajectory" revMajor="1" revMinor="0" />
      <Catalog name="TrajectoryCatalog">
      </Catalog>
    </OpenSCENARIO>"""
    # 创建一个文本文件以写入路径内容
    with open(Trajectory_file, "w") as file:
        file.write(xml_content)
    Trajectory_file_tree=ET.ElementTree(file=Trajectory_file)
    Trajectory_file_root=Trajectory_file_tree.getroot()


    # 找到要插入的位置（在child1标签内部）
    child1_element = Trajectory_file_root.find('.//Catalog')
    child1_element.insert(1,trajectory_content)

    #以下为将所有的time标签替换
    # 找到所有<WorldPosition>标签
    world_positions = Trajectory_file_tree.findall(".//WorldPosition")
    # print(len(world_positions))
    # 计算每两个<WorldPosition>标签之间的距离并相加
    init_speed=float(Storyboard.find('.//AbsoluteTargetSpeed').get('value'))
    total_distance = 0.0
    for i in range(1, len(world_positions)):
        prev_position = world_positions[i - 1]
        curr_position = world_positions[i]

        prev_x = float(prev_position.get("x"))
        prev_y = float(prev_position.get("y"))
        prev_z = float(prev_position.get("z"))

        curr_x = float(curr_position.get("x"))
        curr_y = float(curr_position.get("y"))
        curr_z = float(curr_position.get("z"))

        distance = ((curr_x - prev_x)**2 + (curr_y - prev_y)**2 + (curr_z - prev_z)**2)**0.5
        total_distance += distance
    # print("总距离:", total_distance)
    # print("总时间",total_distance/init_speed)
    time_split=total_distance/init_speed/len(world_positions)
    # print('分割的每小段时间为',time_split,'s')
    time_array=[]
    for i in range(0,len(world_positions)+1):
        time_array.append(time_split*i)
    # print(time_array)
    j=0
    for vertex in Trajectory_file_tree.findall('.//Vertex'):
        vertex.set('time',str(time_array[j]))
        j=j+1

    Trajectory_file_tree.write(Trajectory_file)

    # 添加头文件描述，这样vscode就可以识别出是xml代码
    with open(Trajectory_file, 'r') as file:
        file_contents = file.read()
    # 在内容开头插入指定的文本行
    inserted_line = '<?xml version="1.0" encoding="UTF-8"?>\n'
    file_contents = inserted_line + file_contents

    # 再次打开文件以写入修改后的内容
    with open(Trajectory_file, 'w') as file:
        file.write(file_contents)
        file.close()

    # 执行命令行操作，就不用另外打开cmd窗口去转化
    cmd_command = cmaker_dir + f'/bin/osc2cm.win64.exe --cmprojpath ../ ' \
                                   f'--oscfname Data_osc/{xosc_name} --validate --egoname Ego ' \
                                   f'--trfname {file_name} --rdfname {file_name}_road ' \
                                   f'--egoinf {cm_vehicle_model} --trfendmode 2 --loglevel 4 ' \
                                   f'--logtofile --logtoconsole --trfmobj --defaultman 1.0 '
    try:
        subprocess.run(cmd_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("命令执行出错：", e)

    # 以下作用为修改testrun文件中的Traffic.0.Man.n.LatStep.0.Limit参数，这样有lateral offset动作时直接转换不会报错
    with open(testrun_file, 'r+') as testrun:
        testrun_contents = testrun.readlines()
        for i, line in enumerate(testrun_contents):
            # 如果找到了目标行
            if line.startswith("Traffic.") and line.endswith(".Limit =\n"):
                # 修改该行的内容
                testrun_contents[i] = line[:-2] + "=t {}\n"
            # 回到文件开头
        testrun.seek(0)
        # 用修改后的内容覆盖原文件
        testrun.writelines(testrun_contents)


    #以下为CarMaker官方定义函数，此处的作用为设置车辆初始速度

#以下为CarMaker官方定义函数，此处的作用为设置车辆初始速度
    async def make_variations():
        project_path = pathlib.Path(cmaker_dir)
        cmapi.Project.load(project_path)

        testrun_path = pathlib.Path(testrun_file)
        testrun = cmapi.Project.instance().load_testrun_parametrization(testrun_path)
        #print(testrun.get_path())
        # vehicle_path = pathlib.Path("Examples/DemoCar_SensorRadarRSI")
        # vehicle = cmapi.Project.instance().load_vehicle_parametrization(vehicle_path)

        # Select vehicle by modifying the Parameter 'Vehicle' of the testrun parametrization object.
        # This Parameter corresponds with the infofile key 'Vehicle' in the testrun infofile.
        a=testrun.set_parameter_value("DrivMan.Man.0.LongStep.0.Dyn", 'VelControl {} 0.0 1.0 0 1 0'.format(3.6*init_speed))

        cmapi.Project.write_parametrization(a,testrun)
        # Make a variation containing a copy of the testrun
        variation = cmapi.Variation.create_from_testrun(testrun.clone())
        variation.set_name("Variation")

        return [variation]
    async def main():
        variations = await make_variations()
        # for variation in variations:
        #
        #     cmapi.logger.info(f"Testrun parametrization of variation {variation.get_name()}:")
        #     param_string = []
        #     for parameter in variation.get_testrun().params_by_key.values():
        #         param_string.append(f"{parameter.key} : {parameter.value}")
        #
        #     cmapi.logger.info("\n".join(param_string))

    cmapi.Task.run_main_task(main())
