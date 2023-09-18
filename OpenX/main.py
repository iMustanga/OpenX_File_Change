import sys
from PyQt5.QtWidgets import *
import App_main

# 2023.09.14 增加了按钮按下颜色变化的功能

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Mainwindow = App_main.window_main()
    Mainwindow.show()
    sys.exit(app.exec_())

