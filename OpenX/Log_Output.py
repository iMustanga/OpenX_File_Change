# 导入os模块，用于操作文件和目录
import os
import default_file
# 定义一个函数，接受一个目录路径作为参数
def write_dir_path_to_file(directory):
    # 检查目录是否存在，如果不存在，就打印出错误信息并退出函数
    if not os.path.isdir(directory):
        print(f"{directory} 不是一个有效的目录。")
        return
    # 获取目录的绝对路径
    directory = os.path.abspath(directory)
    # 在目录下创建一个名为dir_path.txt的文件，打开它并写入目录路径
    output_file = default_file.DEFAULT_LOG_DIR
    with open(output_file, "w") as file:
        file.write(directory + "\n")
    # 打印出成功信息和文件路径
    print(f"已经将目录路径写入 {output_file}")
