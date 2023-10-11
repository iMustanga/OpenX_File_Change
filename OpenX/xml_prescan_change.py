import sys
import os
from shutil import copy, copyfile
import xml.etree.ElementTree as ET

class roadrunnner_to_prescan:
    def __init__(self, input_file, output_file):
        self.old_file = input_file
        self.new_file = output_file

    def prescan_tranform(self):
        tree = ET.parse(self.old_file)
        root = tree.getroot()  # 获取根节点

        print("---------------分割线----------------")
        print("下面验证修改代码正确与否")

        # 将event priority从parallel修改为following
        print("event priority修改结果：")
        event_elements = root.findall('.//Event')
        for event_element in event_elements:
            print(event_element.attrib)
            if event_element.attrib['priority'] == 'parallel':
                event_element.attrib['priority'] = 'following'
                print(event_element.attrib)
        # 备用写法
        # parallel_elements = root.findall(".//*[@priority='parallel']")
        # for parallel_element in parallel_elements:
        #     print(parallel_element.attrib)# 打印输出所有含有priority='parallel'的属性及其属性值
        #     if parallel_element.attrib['priority'] == 'parallel':
        #         del parallel_element.attrib['priority']
        #         parallel_element.set('priority', 'following')
        #         print(parallel_element.attrib)# 打印修改后的结果判断是否修改成功
        # print("-------------------------------")

        # 将变道行为的DynamicShape从Linear改为Sinusoidal
        print("DynamicShape修改结果：")
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

        print("-------------------------------")

        # 删除用户自定义部分
        print("UserDefinedAction修改结果：")
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
        # 方案二：将含有UserDefinedAction的ManeuverGroup整个删掉
        # for storyboard in root:
        #     if storyboard.tag == 'Storyboard':
        #         for story in storyboard:
        #             if story.tag == 'Story':
        #                 for act in story:
        #                     groups = act.findall('.//ManeuverGroup')
        #                     for group in groups:
        #                         if group.find('.//UserDefinedAction') is not None:
        #                             act.remove(group)
        print("-------------------------------")

        # 若有相对速度初始化的设置，将relativetargetspeed里的continuous属性修改为true
        print("RelativeTargetSpeed修改结果：")
        RelTarSpeeds = root.findall('.//RelativeTargetSpeed')
        if len(RelTarSpeeds) == 0:
            print("此文件没有相对速度初始化行为。")
        else:
            for RelTarSpeed in RelTarSpeeds:
                print(RelTarSpeed.attrib)
                if RelTarSpeed.attrib['continuous'] == 'false':
                    RelTarSpeed.attrib['continuous'] = 'true'
                    print(RelTarSpeed.attrib)
        print("-------------------------------")

        # 修改触发条件为simulationTimeCondition触发
        print("SimulationTimeCondition修改结果：")

        # 原始列表，用于给需要特殊处理Act中的simulationtimecondition属性赋值
        startTime = []
        stopTime = []
        # 操作列表，用于给新的simulationtimecondition属性赋值
        startTime1= []
        stopTime1 = []
        # 用于接收condition名称的列表
        # cons = []

        # 将每个Act直属的初始时间和结束时间取出，分别存放到列表中
        for storyboard in root:
            if storyboard.tag == 'Storyboard':
                for story in storyboard:
                    if story.tag == 'Story':
                        for act in story:
                            # print(act.attrib)
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
        print("原始列表startTime: %s" % startTime)
        print("原始列表stopTime: %s" % stopTime)

        # 修改列表元素值，也就是规整触发时间和结束时间，比如说下一个Act的开始时间是上一个Act的结束时间
        # 记录列表长度用于遍历
        startlen = len(startTime)
        stoplen = len(stopTime)
        if startlen != stoplen:
            print("bugs appear in list!")
        samelen = startlen

        # 将原始列表的元素遍历赋值给造作列表
        i = 0
        while i < samelen:
            startTime1.append(startTime[i])
            stopTime1.append(stopTime[i])
            i += 1
        print("操作列表startTime1: %s" % startTime1)
        print("操作列表stopTime1: %s" % stopTime1)

        # 规整操作列表元素
        timeindex = 0
        while timeindex < (samelen - 1):
            if stopTime1[timeindex] != 'None':
                startTime1[timeindex + 1] = stopTime1[timeindex]
            timeindex += 1

        print("规整后的操作列表startTime1: %s" % startTime1)
        print("规整后的操作列表stopTime1: %s" % stopTime1)

        print("-------------------------------")
        # 将场景中的各个车辆对象分别取出并放在列表Object[]中，用于识别需要特殊处理的Act中不属于“主车”的车辆动作
        Object = []
        for entities in root:
            if entities.tag == 'Entities':
                for scenarioobject in entities:
                    if scenarioobject.tag == 'ScenarioObject':
                        print(scenarioobject.attrib)
                        Object.append(scenarioobject.attrib['name'])
                        print("Object列表: %s" % Object)

        print("-------------------------------")
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

                            print("don't need to change list: %s" % dont_need_to_changes)
                            print("need to change list: %s" % need_to_change)
                            print("需要特别修改的Act为：%s" % need_to_change)

        print("-------------------------------")
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
                                        print("judge_ego属性: %s" % judge_ego.attrib)
                                        if judge_ego.attrib['entityRef'] != Object[0]:
                                            storyboardelementstatecondition = maneuvergroup.find(
                                                ".//StoryboardElementStateCondition")
                                            print(storyboardelementstatecondition.attrib)
                                            actlist.append(storyboardelementstatecondition.attrib['storyboardElementRef'])
                                            print("actlist列表: %s" % actlist)
        # # 方案二
        # for storyboard in root:
        #     if storyboard.tag == 'Storyboard':
        #         for story in storyboard:
        #             if story.tag == 'Story':
        #                 for act in story:
        #                     maneuvergroups = act.findall('.//ManeuverGroup')
        #                     if len(maneuvergroups) > 1:
        #                         act_change.append(act.get('name'))
        #                         print("需要特别修改的Act为：%s" % act_change)
        #                         print(act_change[0])
        #                         # 含有用户自定义行为的Maneuvergroup删除之后，只有这个需要特殊处理的Act会有不止一个Maneuvergroup
        #                         for maneuvergroup in maneuvergroups:
        #                             judge_ego = maneuvergroup.find('.//EntityRef')
        #                             print("judge_ego属性: %s" % judge_ego.attrib)
        #                             if judge_ego.attrib['entityRef'] != Object[0]:
        #                                 storyboardelementstatecondition = maneuvergroup.find(
        #                                     ".//StoryboardElementStateCondition")
        #                                 print(storyboardelementstatecondition.attrib)
        #                                 actlist.append(storyboardelementstatecondition.attrib['storyboardElementRef'])
        #                                 print("actlist列表: %s" % actlist)
        # -----------------------------------------------------------------------------------------------------------
        # -----------------------------------------------------------------------------------------------------------
        # -----------------------------------------------------------------------------------------------------------
        # -----------------------------------------------------------------------------------------------------------
        # 时间修改部分
        # 如果场景只有单车，运行完模块1就修改完成；如果大于一台车，则需要再运行模块2修改需特殊处理的Act；如果大于两台车，则再需要运行模块3修改simulationstart行为的开始时间为0

        # 模块1
        # 用于将StoryboardElementStateCondition修改为SimulationTimeCondition触发，Value值为Act直属下的对应开始时间。
        print("-------------------------------")
        print("开始运行模块1")
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

                            # starttrigger备用写法
                            # acts = act.findall(".//StartTrigger")
                            # for act1 in acts:
                            #     if act1 is not None:
                            #         by_value_conditions = act1.findall(".//ByValueCondition")
                            #         for by_value_condition in by_value_conditions:
                            #             storyboard_state_condition = by_value_condition.find(
                            #                 "StoryboardElementStateCondition")
                            #             if storyboard_state_condition is not None:
                            #                 by_value_condition.remove(storyboard_state_condition)
                            #                 simulation_time_condition = ET.SubElement(by_value_condition,
                            #                                                           "SimulationTimeCondition")
                            #                 simulation_time_condition.set("value", startTime1[a])
                            #                 simulation_time_condition.set("rule", "greaterThan")
                            #
                            #             simu = by_value_condition.find(".//SimulationTimeCondition")
                            #             if simu is not None:
                            #                 simu.attrib['value'] = startTime1[a]

                            # stoptrigger备用写法
                            # actss = act.findall(".//StopTrigger")
                            # for act2 in actss:
                            #     if act2 is not None:
                            #         by_value_conditions = act2.findall(".//ByValueCondition")
                            #         for by_value_condition in by_value_conditions:
                            #             storyboard_state_condition = by_value_condition.find(
                            #                 "StoryboardElementStateCondition")
                            #             if storyboard_state_condition is not None:
                            #                 by_value_condition.remove(storyboard_state_condition)
                            #                 simulation_time_condition = ET.SubElement(by_value_condition,
                            #                                                           "SimulationTimeCondition")
                            #                 simulation_time_condition.set("value", stopTime1[a])
                            #                 simulation_time_condition.set("rule", "greaterThan")
                            #
                            #             simu1 = by_value_condition.find(".//SimulationTimeCondition")
                            #             if simu1 is not None:
                            #                 simu1.attrib['value'] = stopTime1[a]
                            a += 1
        print("模块1运行成功")

        # 模块2
        # 修改之前找到的特殊处理Act里面的触发时间值（已经是simulationtimecondition，但值需要单独修改）
        print("-------------------------------")
        print("开始运行模块2")
        acts = root.findall(".//Act")
        for act in acts:
            # print(act.attrib)
            # if act.attrib['name'] == act_change[0]:
            # 没有需要修改的Act，则跳出循环
            if not need_to_change:
                break
            else:
                if act.attrib['name'] == need_to_change[0]:
                    abc = act.findall('.//ManeuverGroup')
                    num = len(abc)
                    print("maneuvergroup数量：%s" % num)
                    e = 0
                    for maneuvergroup in abc:
                        print("maneuvergroup.attrib: %s" % maneuvergroup.attrib)
                        judge_ego = maneuvergroup.find('.//EntityRef')
                        print("judge_ego.attrib: %s" % judge_ego.attrib)
                        if judge_ego.attrib['entityRef'] == Object[0]:
                            continue
                        else:
                            starts = maneuvergroup.find(".//SimulationTimeCondition")
                            change_index = actlist[e].split('Act')
                            print("change_index：%s" % change_index)
                            d = int(change_index[1]) - 1
                            starts.attrib['value'] = stopTime[d]
                        e += 1
        print("模块2运行成功")

        # 模块3
        # 将每个对象开始时刻的Act的开始时间修正为0
        print("-------------------------------")
        print("开始运行模块3")
        acts = root.findall(".//Act")
        for act in acts:
            for child in act:
                if child.tag == 'StartTrigger':
                    simulationstart = child.find(".//Condition")
                    # print("simulationstart: %s" % simulationstart)
                    f = simulationstart.attrib['name']
                    print("f: %s" % f)
                    g = f.split('SimulationStart')
                    print("g: %s" % g)
                    exclude_values = ["", "2"]
                    if g[0] == '':
                        if g[1] not in exclude_values:
                            # 修改直属的开始时间为0
                            simulation_time_condition = child.find(".//SimulationTimeCondition")
                            print("直属的simulation_time_condition: %s" % simulation_time_condition.attrib['value'])
                            simulation_time_condition.attrib['value'] = '0.0000000000000000e+0'
                            print("修改后直属的simulation_time_condition: %s" % simulation_time_condition.attrib['value'])
                            # 修改maneuvergroup下的开始时间为0
                            maneuvergroups = act.findall(".//ManeuverGroup")
                            for maneuvergroup in maneuvergroups:
                                simulation_time_condition = maneuvergroup.find(".//SimulationTimeCondition")
                                print("操作组内的simulationtimeconditon: %s" % simulation_time_condition.attrib['value'])
                                simulation_time_condition.attrib['value'] = '0.0000000000000000e+0'
                                print("修改后操作组内的simulationtimeconditon: %s" % simulation_time_condition.attrib['value'])
        print("模块3运行成功")
        print("-------------------------------")
        # 将不含有maneuvergroup的Act删除，否则会因为文件结构不完整无法导入(删除之后每个对象开始的行为缺失，不推荐使用)
        # for storyboard in root:
        #         for story in storyboard:
        #     if storyboard.tag == 'Storyboard':
        #             if story.tag == 'Story':
        #                 for act in story:
        #                     mans = act.findall(".//ManeuverGroup")
        #                     if len(mans) == 0:
        #                         story.remove(act)

        # 某些Act直属下的StopTrigger可能是空标签，这会导致给stopTime列表赋值时元素为字符串'None'。
        # 该情况不常出现，若出现，可自行修改对应Act下的SimulationTimeCondition标签中的value为需要的时间值

        # 写入
        tree.write(self.new_file)
