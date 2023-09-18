import subprocess
import xml.etree.ElementTree as ET
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\CarMaker_PythonAPI\\python3.8")
import cmapi
import pathlib
def change(file_name, cm_vehicle_model, input_dir, output_dir, cmaker_dir):
    # 手动输入文件名
    xosc_name = file_name+'.xosc'
    # 构建文件路径
    file_path = input_dir
    new_file_path = output_dir
    testrun_file = cmaker_dir + "/Data/TestRun/" + file_name
    tree = ET.ElementTree(file=file_path)

    root = tree.getroot()
    # 当要获取属性值时，用attrib方法。
    dict={'name':'Act'}
    simulationtimes=[]
    stoptriggers=[]
    #----把simulationtime记录到数组中
    for child in root:
        if child.tag == 'Storyboard':
            for child1 in child:
                if child1.tag == 'Story':
                    for child2 in child1:
                        #print(child2.attrib)

                        for child3 in child2:
                            #在stoptrigger中查找simulationtime
                            #print(child3)
                            if child3.tag =='StopTrigger':
                                simulationtime=child3.find('.//SimulationTimeCondition')
                                if simulationtime is not None:
                                    #将simulationtime装入数组
                                    simulationtimes.append(simulationtime.attrib['value'])
    # print(simulationtimes)
    #将带有userdefindaction的maueuver以及act全部删除
    for child in root:
        if child.tag =='Storyboard':
            for child1 in child:
                if child1.tag =='Story':
                    element_remove=[]
                    for child2 in child1:
                        element_remove1=[]
                        num=child2.findall('.//UserDefinedAction')
                        # 如果找到一个Act中有两个userdefindaction，则要将这一整个Act给删除掉
                        if len(num)>1:
                            element_remove.append(child2)
                        else:
                            for child3 in child2:
                                if child3.find('.//UserDefinedAction') is not None:
                                    element_remove1.append(child3)
                        for element1 in element_remove1:
                            child2.remove(element1)
                    for element in element_remove:
                        child1.remove(element)

    #查看删除后的结果是否正确
    # for child in root:
    #     if child.tag =='Storyboard':
    #         for child1 in child:
    #             if child1.tag =='Story':
    #                 for child2 in child1:
    #                     print(child2.attrib)
    #                     for child3 in child2:
    #                         print(child3)
    # 将多车的行为重新排序
    story_tag = root.find('.//Story')
    for child in root:
        if child.tag == 'Storyboard':
            for child1 in child:
                if child1.tag == 'Story':
                    maneuver_removes = []
                    maneuver_act = []
                    #child2为遍历story下的每一个Act标签
                    for child2 in child1:
                        #print(child2.attrib)
                        num1=child2.findall('.//ManeuverGroup')
                        #print(len(num1),num1)
                        if len(num1)>1:
                            #由于roadrunner导出的行为规则，Ego的最后的行为与其他车辆的最后的行为被放到了同一个Act标签中，所以这里要把其他车辆的maneuver标签取出，放到对应处，放置地方由storyboardElementRef确定
                            for ref in num1:
                                #判断是不是Ego的行为，不是的话就要移走
                                judge_ego=ref.find('.//EntityRef')
                                if judge_ego.get('entityRef') !='Ego':
                                    # 使用 .find() 方法查找 XML 标签内的 StoryboardElementStateCondition 子标签
                                    storyboard_element_state_condition = ref.find(".//StoryboardElementStateCondition")
                                    # 使用 .get() 方法获取 storyboardElementRef 属性的值
                                    storyboard_element_ref = storyboard_element_state_condition.get("storyboardElementRef")
                                    # 将 storyboardElementRef 属性的值赋给 Ref 变量
                                    Ref = storyboard_element_ref
                                    # print(Ref, type(Ref))
                                    maneuver_act.append(Ref)
                                    maneuver_removes.append(ref)
                            #从Act里面删除多余的maneuver标签
                            for maneuver_remove in maneuver_removes:
                                child2.remove(maneuver_remove)
                    # print(maneuver_removes)
                    # print(maneuver_act)
                    j=0
                    for child2 in child1:
                        #print(child2.attrib['name'])
                        if child2.attrib['name'] in maneuver_act:
                            # 找到第一段文本中的<Act>标签，并将第二段文本作为子元素插入到其中
                            maneuver_remove_xml=ET.tostring(maneuver_removes[j],encoding='unicode',method='xml')
                            # 找到第一段代码中的</ManeuverGroup>标签
                            child2.insert(1,maneuver_removes[j])
                            #print(maneuver_remove_xml)
                            j=j+1
    #删除Act直属的starttrigger和stoptrigger
    story_tag = root.find('.//Story')
    for child in root:
        if child.tag == 'Storyboard':
            for child1 in child:
                if child1.tag == 'Story':
                    maneuver_removes = []
                    maneuver_act = []
                    #child2为遍历story下的每一个Act标签
                    for child2 in child1:
                        if child2.find('StartTrigger') is not None:
                            child2.remove(child2.find('StartTrigger'))
                        if child2.find('StopTrigger') is not None:
                            child2.remove(child2.find('StopTrigger'))
    #将byvaluecondition标签内容更改为simulationtimecondition并且赋值
    for child in root:
        if child.tag == 'Storyboard':
            for child1 in child:
                if child1.tag == 'Story':
                    i=0
                    for child2 in child1:
                        for child3 in child2.findall('.//ManeuverGroup'):
                            by_value_conditions = child3.findall(".//ByValueCondition")
                            for by_value_condition in by_value_conditions:
                                # 找到子标签<StoryboardElementStateCondition>
                                storyboard_state_condition = by_value_condition.find("StoryboardElementStateCondition")
                                if storyboard_state_condition is not None:
                                    # 获取<StoryboardElementStateCondition>标签的属性值
                                    state = storyboard_state_condition.get("state")
                                    # 移除子标签<StoryboardElementStateCondition>
                                    by_value_condition.remove(storyboard_state_condition)

                                    # 创建新的<SimulationTimeCondition>标签，并添加属性值
                                    simulation_time_condition = ET.SubElement(by_value_condition, "SimulationTimeCondition")

                                    simulation_time_condition.set("value",simulationtimes[i])

                                    simulation_time_condition.set("rule", "greaterThan")  # 设置rule属性值为"greaterThan"（示例值，你可以根据需求设置其他值）
                            i=i+1



    # 找到所有具有priority="parallel"属性的标签
    parallel_elements = root.findall(".//*[@priority='parallel']")
    # 遍历每个具有priority="parallel"属性的标签
    for parallel_element in parallel_elements:
        # 检查是否已经存在maximumExecutionCount属性
        if "maximumExecutionCount" not in parallel_element.attrib:
            # 如果不存在，添加maximumExecutionCount="1"属性
            parallel_element.set("maximumExecutionCount", "1")
    #判断是不是laneoffset行为，laneoffset需要单独修改
    if root.findall('.//LaneOffsetAction') is not None:
        for LaneOffsetAction in root.findall('.//LaneOffsetAction'):
            for LaneOffsetActionDynamics in LaneOffsetAction:
                if LaneOffsetActionDynamics.tag =='LaneOffsetActionDynamics':
                    LaneOffsetActionDynamics.set("maxLateralAcc",'{}'.format(int(1)))
    #判断是不是relativespeed行为，如果是的话需要单独修改
    #修改初始条件中的相对速度
    privates = root.findall('.//Private')
    for private in privates:
        if private.find('.//RelativeTargetSpeed') is not None:
            SpeedActionTarget=private.find('.//SpeedActionTarget')
            RelativeTargetSpeed=private.find('.//RelativeTargetSpeed')
            entityRef=RelativeTargetSpeed.get('entityRef')
            value = RelativeTargetSpeed.get('value')
            for i in privates:
                if i.get('entityRef')==entityRef:
                    #targetspeed=float(i.find('.//AbsoluteTargetSpeed').get('value'))+float(value)
                    SpeedActionTarget.remove(RelativeTargetSpeed)
                    # 创建新的<SimulationTimeCondition>标签，并添加属性值
                    new_target = ET.SubElement(SpeedActionTarget, "AbsoluteTargetSpeed")
                    AbsoluteTargetSpeed=i.find('.//AbsoluteTargetSpeed')
                    new_target.set('value',str(float(AbsoluteTargetSpeed.get('value'))+float(value)))


    #写入修改后的新文件
    tree.write(new_file_path)
    # 打开文件并读取内容
    with open(new_file_path, 'r') as file:
        file_contents = file.read()
    # 在内容开头插入指定的文本行
    inserted_line = '<?xml version="1.0" encoding="UTF-8"?>\n'
    file_contents = inserted_line + file_contents

    # 再次打开文件以写入修改后的内容
    with open(new_file_path, 'w') as file:
        file.write(file_contents)
        file.close()
    print('Xml_changetools finished successfully')
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
#以下作用为修改testrun文件中的Traffic.0.Man.n.LatStep.0.Limit参数，这样有lateral offset动作时直接转换不会报错
    with open(testrun_file,'r+') as testrun:
        testrun_contents=testrun.readlines()
        for i, line in enumerate(testrun_contents):
            # 如果找到了目标行
            if line.startswith("Traffic") and line.endswith(".Limit =\n"):
                # 修改该行的内容
                testrun_contents[i] = line[:-2] + "= t {}\n"
            # 回到文件开头
        testrun.seek(0)
        # 用修改后的内容覆盖原文件
        testrun.writelines(testrun_contents)
    print('testrun file fixed successfully')
    #以下为CarMaker官方定义函数，此处的作用为设置车辆初始速度
    # async def make_variations():
    #     project_path = pathlib.Path("C:/CM_Projects/PROJECTNAME")
    #     cmapi.Project.load(project_path)
    #
    #     testrun_path = pathlib.Path(testrun_file)
    #     testrun = cmapi.Project.instance().load_testrun_parametrization(testrun_path)
    #     #print(testrun.get_path())
    #     # vehicle_path = pathlib.Path("Examples/DemoCar_SensorRadarRSI")
    #     # vehicle = cmapi.Project.instance().load_vehicle_parametrization(vehicle_path)
    #     #
    #     trailer_path = pathlib.Path("Examples/HorseTrailer")
    #     trailer = cmapi.Project.instance().load_trailer_parametrization(trailer_path)
    #
    #     # Select vehicle by modifying the Parameter 'Vehicle' of the testrun parametrization object.
    #     # This Parameter corresponds with the infofile key 'Vehicle' in the testrun infofile.
    #
    #     a=testrun.set_parameter_value("Traffic.0.Man.3.LatStep.0.Limit", 't {}')
    #
    #     cmapi.Project.write_parametrization(a,testrun)
    #     # Make a variation containing a copy of the testrun
    #     variation = cmapi.Variation.create_from_testrun(testrun.clone())
    #     variation.set_name("Variation")
    #
    #     # Make a variation containing a trailer
    #     variation_trailer = variation.clone()
    #     variation_trailer.set_name("Variation with Trailer")
    #
    #     # Append trailer by key value for this variation
    #     kvalues = []
    #     kvalues.append(cmapi.KeyValue(cmapi.Category.TestRun, "Trailer", trailer))
    #     variation_trailer.set_kvalues(kvalues)
    #
    #     return [variation, variation_trailer]
    # async def main():
    #     variations = await make_variations()
    #     for variation in variations:
    #
    #         cmapi.logger.info(f"Testrun parametrization of variation {variation.get_name()}:")
    #         param_string = []
    #         for parameter in variation.get_testrun().params_by_key.values():
    #             param_string.append(f"{parameter.key} : {parameter.value}")
    #
    #         cmapi.logger.info("\n".join(param_string))
    #
    # cmapi.Task.run_main_task(main())

