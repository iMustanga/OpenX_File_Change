一、roadrunner操作 
1.需要在车辆设置界面将车辆主体名称命名为ego，车辆型号名称可以不作修改 
 
2.加速场景的加速方式都可以选择，减速模式不可以选择加速度方式，其余时间或是长度方式都可以，但模式必须选择为线性“Liner”，其余模式VTD无法识别 
 
3.roadrunner动作中目前只能够导入变道、变速两个动作 
 
二、软件操作 
1.软件使用：首先点击select file按钮，选取需要更改格式的xosc文件；随后点击select folder按钮，选择更改后xosc文件需要保存的位置；最后在new filename后的对话框输入新xosc的文件名；最终点击VTD按钮即可。 
 
2.若需要导入车辆模型，需要在点击VTD按钮前点击vehicle Models选取车辆模型所在的文件夹，并在后面的下拉框内选择需要的车辆模型最终会将该文件写入到Vehicle Modles文件夹中 
 
3.需要注意的是输入的新的xosc文件名必须与osgb以及xodr文件的文件名完全相同，否则会导致在读取osgb以及xodr文件时发生错误 
 
4.需要在路径~/VIRES/VTD.2021.4/Data/Projects/Current/Databases下新建一个名为roadrunner的文件夹，并将osgb以及xodr文件存储在该路径下，否则会导致在读取osgb以及xodr文件时发生错误 
 
