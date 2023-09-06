import subprocess
import xml.etree.ElementTree as ET
import xml.etree as ET1
def main(file_name, cm_vehicle_model, input_dir, output_dir, cmaker_dir):
    # input_dir,output_dir都是xosc文件的绝对路径
    xosc_name = file_name+'.xosc'
    # 构建文件路径
    # file_path = r"C:\IPG\RoadRunner R2022b\Test\Exports\\" + xosc_name
    # new_file_path = r"C:\CM_Projects\PROJECTNAME\Data_osc\\" + xosc_name
    file_path = input_dir
    new_file_path = output_dir
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
                        print(child2.attrib)

                        for child3 in child2:
                            #在stoptrigger中查找simulationtime
                            #print(child3)
                            if child3.tag =='StopTrigger':
                                simulationtime=child3.find('.//SimulationTimeCondition')
                                if simulationtime is not None:
                                    #将simulationtime装入数组
                                    simulationtimes.append(simulationtime.attrib['value'])
    print(simulationtimes)
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
                                    print(Ref, type(Ref))
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
                        by_value_conditions = child2.findall(".//ByValueCondition")
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
                    LaneOffsetActionDynamics.set("maxLateralAcc",'3')
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
