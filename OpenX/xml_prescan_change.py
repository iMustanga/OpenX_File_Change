import xml.etree.ElementTree as ET

class roadrunnner_to_prescan:
    def __init__(self, input_file, output_file):
        self.old_file = input_file
        self.new_file = output_file

    def prescan_tranform(self):
        tree = ET.parse(self.old_file)
        root = tree.getroot()  # 获取根节点

        # 将event priority从parallel修改为following
        event_elements = root.findall('.//Event')
        for event_element in event_elements:
            if event_element.attrib['priority'] == 'parallel':
                event_element.attrib['priority'] = 'following'

        # 将变道行为的DynamicShape从Linear改为Sinusoidal
        for storyboard in root:
            if storyboard.tag == 'Storyboard':
                for story in storyboard:
                    if story.tag == 'Story':
                        for i in story:
                            actions = i.findall('.//LaneChangeActionDynamics')
                            for action in actions:
                                dynamic_shape = action.attrib.get('dynamicsShape')
                                if dynamic_shape == 'linear':
                                    action.attrib['dynamicsShape'] = 'sinusoidal'
                                else:
                                    return 1

                            actions1 = i.findall('.//SpeedActionDynamics')
                            for action1 in actions1:
                                dynamic_shape = action1.attrib.get('dynamicsShape')
                                if dynamic_shape != 'linear':
                                    return 1

        # 删除用户自定义部分
        # 方案一：将ManeuverGroup中的UserDefinedAction部分删除
        for storyboard in root:
            if storyboard.tag == 'Storyboard':
                for story in storyboard:
                    if story.tag == 'Story':
                        for i in story:
                            actions = i.findall('.//Action')
                            for action in actions:
                                custom = action.find("UserDefinedAction")
                                if custom is not None:
                                    action.remove(custom)
        # 若有相对速度初始化的设置，将relativetargetspeed里的continuous属性修改为true
        RelTarSpeeds = root.findall('.//RelativeTargetSpeed')
        if len(RelTarSpeeds) == 0:
            pass
        else:
            for RelTarSpeed in RelTarSpeeds:
                if RelTarSpeed.attrib['continuous'] == 'false':
                    RelTarSpeed.attrib['continuous'] = 'true'
        # 修改触发条件为simulationTimeCondition触发

        # 原始列表，用于给需要特殊处理Act中的simulationtimecondition属性赋值
        startTime = []
        stopTime = []
        # 操作列表，用于给新的simulationtimecondition属性赋值
        startTime1= []
        stopTime1 = []
        # 用于接收condition名称的列表

        # 将每个Act直属的初始时间和结束时间取出，分别存放到列表中
        for storyboard in root:
            if storyboard.tag == 'Storyboard':
                for story in storyboard:
                    if story.tag == 'Story':
                        for act in story:
                            for j in act:
                                if j.tag == 'StartTrigger':
                                    startTimes = j.find('.//SimulationTimeCondition')
                                    if startTimes is not None:
                                        startTime.append(startTimes.attrib['value'])
                                    needtobechange = j.find('.//StoryboardElementStateCondition')
                                    if needtobechange is not None:
                                        startTime.append('change')
                                if j.tag == 'StopTrigger':
                                    stopTimes = j.find('.//SimulationTimeCondition')
                                    if stopTimes is not None:
                                        stopTime.append(stopTimes.attrib['value'])
                                    if stopTimes is None:
                                        stopTime.append('None')

        # 修改列表元素值，也就是规整触发时间和结束时间，比如说下一个Act的开始时间是上一个Act的结束时间
        # 记录列表长度用于遍历
        startlen = len(startTime)
        stoplen = len(stopTime)
        if startlen != stoplen:
            # print("bugs appear in list!")
            return 1
        samelen = startlen

        # 将原始列表的元素遍历赋值给造作列表
        i = 0
        while i < samelen:
            startTime1.append(startTime[i])
            stopTime1.append(stopTime[i])
            i += 1

        # 规整操作列表元素
        timeindex = 0
        while timeindex < (samelen - 1):
            if stopTime1[timeindex] != 'None':
                startTime1[timeindex + 1] = stopTime1[timeindex]
            timeindex += 1

        # 将场景中的各个车辆对象分别取出并放在列表Object[]中，用于识别需要特殊处理的Act中不属于“主车”的车辆动作
        Object = []
        for entities in root:
            if entities.tag == 'Entities':
                for scenarioobject in entities:
                    if scenarioobject.tag == 'ScenarioObject':
                        Object.append(scenarioobject.attrib['name'])

        # 识别出需要特殊处理的Act，将其中需要修改触发时间的maneuvergroup对应的storyboardElementRef属性值记录到列表actlist[]中。
        # 如该值为Act6，表明该maneuvergroup的触发时间为Act6直属的结束时间
        act_change = []
        actlist = []
        dont_need_to_changes = []
        need_to_change = []
        # 方案一
        for storyboard in root:
            if storyboard.tag == 'Storyboard':
                for story in storyboard:
                    if story.tag == 'Story':
                        for act in story:
                            p = 0
                            maneuvergroups = act.findall('.//ManeuverGroup')
                            for maneuvergroup in maneuvergroups:
                                if maneuvergroup.find(".//EntityRef") is None:
                                    dont_need_to_changes.append(act.attrib['name'])
                                    break
                                else:
                                    p += 1
                            if p > 1:
                                need_to_change.append(act.attrib['name'])

        # 找出需要特殊处理的Act后，将直属的ManeuverGroup下对应的Act取出，用于修改对应行为的触发时间
        for storyboard in root:
            if storyboard.tag == 'Storyboard':
                for story in storyboard:
                    if story.tag == 'Story':
                        for act in story:
                            # 没有需要修改的Act，则跳出循环
                            if not need_to_change:
                                break
                            else:
                                if act.attrib['name'] == need_to_change[0]:
                                    maneuvergroups = act.findall('.//ManeuverGroup')
                                    for maneuvergroup in maneuvergroups:
                                        judge_ego = maneuvergroup.find('.//EntityRef')
                                        if judge_ego.attrib['entityRef'] != Object[0]:
                                            storyboardelementstatecondition = maneuvergroup.find(
                                                ".//StoryboardElementStateCondition")
                                            actlist.append(storyboardelementstatecondition.attrib['storyboardElementRef'])
        # -----------------------------------------------------------------------------------------------------------
        # -----------------------------------------------------------------------------------------------------------
        # -----------------------------------------------------------------------------------------------------------
        # -----------------------------------------------------------------------------------------------------------
        # 时间修改部分
        # 如果场景只有单车，运行完模块1就修改完成；如果大于一台车，则需要再运行模块2修改需特殊处理的Act；如果大于两台车，则再需要运行模块3修改simulationstart行为的开始时间为0

        # 模块1
        # 用于将StoryboardElementStateCondition修改为SimulationTimeCondition触发，Value值为Act直属下的对应开始时间。
        for storyboard in root:
            if storyboard.tag == 'Storyboard':
                for story in storyboard:
                    if story.tag == 'Story':
                        a = 0
                        for act in story:
                            # 改Act中ManeuverGroup内的触发时间
                            # ManeuverGroup内只会有StoryboardElementStateCondition需要更改
                            maneuvergroups = act.findall('.//ManeuverGroup')
                            for maneuvergroup in maneuvergroups:
                                starts = maneuvergroup.findall(".//StartTrigger")
                                for start in starts:
                                    if start is not None:
                                        by_value_conditions = start.findall(".//ByValueCondition")
                                        for by_value_condition in by_value_conditions:
                                            storyboard_state_condition = by_value_condition.find("StoryboardElementStateCondition")
                                            if storyboard_state_condition is not None:
                                                by_value_condition.remove(storyboard_state_condition)
                                                simulation_time_condition = ET.SubElement(by_value_condition,
                                                                              "SimulationTimeCondition")
                                                simulation_time_condition.set("value", startTime1[a])
                                                simulation_time_condition.set("rule", "greaterThan")

                            # 改Act直属下的触发时间
                            # Act直属下除了有StoryboardElementStateCondition需要更改，还可能有SimulationTimeCondition时间值错误需要更改
                            for child in act:
                                if child.tag == 'StartTrigger':
                                    by_value_conditions = child.findall(".//ByValueCondition")
                                    for by_value_condition in by_value_conditions:

                                        storyboard_state_condition = by_value_condition.find("StoryboardElementStateCondition")
                                        if storyboard_state_condition is not None:
                                            by_value_condition.remove(storyboard_state_condition)
                                            simulation_time_condition = ET.SubElement(by_value_condition,
                                                                                          "SimulationTimeCondition")
                                            simulation_time_condition.set("value", startTime1[a])
                                            simulation_time_condition.set("rule", "greaterThan")

                                        simu = by_value_condition.find(".//SimulationTimeCondition")
                                        if simu is not None:
                                            simu.attrib['value'] = startTime1[a]

                            for child in act:
                                if child.tag == 'StopTrigger':
                                    by_value_conditions = child.findall(".//ByValueCondition")
                                    for by_value_condition in by_value_conditions:

                                        storyboard_state_condition = by_value_condition.find("StoryboardElementStateCondition")
                                        if storyboard_state_condition is not None:
                                            by_value_condition.remove(storyboard_state_condition)
                                            simulation_time_condition = ET.SubElement(by_value_condition,
                                                                                      "SimulationTimeCondition")
                                            simulation_time_condition.set("value", stopTime1[a])
                                            simulation_time_condition.set("rule", "greaterThan")

                                        simu = by_value_condition.find(".//SimulationTimeCondition")
                                        if simu is not None:
                                            simu.attrib['value'] = stopTime1[a]
                            a += 1

        # 模块2
        # 修改之前找到的特殊处理Act里面的触发时间值（已经是simulationtimecondition，但值需要单独修改）
        acts = root.findall(".//Act")
        for act in acts:
            # 没有需要修改的Act，则跳出循环
            if not need_to_change:
                break
            else:
                if act.attrib['name'] == need_to_change[0]:
                    abc = act.findall('.//ManeuverGroup')
                    num = len(abc)
                    e = 0
                    for maneuvergroup in abc:
                        judge_ego = maneuvergroup.find('.//EntityRef')
                        if judge_ego.attrib['entityRef'] == Object[0]:
                            continue
                        else:
                            starts = maneuvergroup.find(".//SimulationTimeCondition")
                            change_index = actlist[e].split('Act')
                            d = int(change_index[1]) - 1
                            starts.attrib['value'] = stopTime[d]
                        e += 1

        # 模块3
        # 将每个对象开始时刻的Act的开始时间修正为0
        acts = root.findall(".//Act")
        for act in acts:
            for child in act:
                if child.tag == 'StartTrigger':
                    simulationstart = child.find(".//Condition")
                    f = simulationstart.attrib['name']
                    g = f.split('SimulationStart')
                    exclude_values = ["", "2"]
                    if g[0] == '':
                        if g[1] not in exclude_values:
                            # 修改直属的开始时间为0
                            simulation_time_condition = child.find(".//SimulationTimeCondition")
                            simulation_time_condition.attrib['value'] = '0.0000000000000000e+0'
                            # 修改maneuvergroup下的开始时间为0
                            maneuvergroups = act.findall(".//ManeuverGroup")
                            for maneuvergroup in maneuvergroups:
                                simulation_time_condition = maneuvergroup.find(".//SimulationTimeCondition")
                                simulation_time_condition.attrib['value'] = '0.0000000000000000e+0'
        # 某些Act直属下的StopTrigger可能是空标签，这会导致给stopTime列表赋值时元素为字符串'None'。
        # 该情况不常出现，若出现，可自行修改对应Act下的SimulationTimeCondition标签中的value为需要的时间值
        # 写入
        tree.write(self.new_file)
