import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Demo(QWidget):                                            # 1
    # 该类继承QWidget
    # 可以放入QPushButton,QLabel等控件
    def __init__(self):
        super(Demo, self).__init__()
        # 文本名为Start的按钮
        # 实例化QPushButton,继承QWidget所以要加上self
        # (相当于告诉程序这个QPushButton是放在QWidget这个房子中的)
        self.button = QPushButton('Start', self)                # 2
        # 连接信号与槽函数
        # self.button就是一个控件
        # clicked（当按钮被点击时）是该控件的一个信号
        # self.change_text即下方定义的函数（槽函数）
        # 语法结构：  控件.信号.connect(槽)
        # self.button控件--->clicked.connect信号连接--->self.change_text槽函数
        self.button.clicked.connect(self.change_text)           # 3

    # 槽
    def change_text(self):
        print('change text')
        # 将按钮文本从Start改为stop
        self.button.setText('Stop')                             # 4
        # 信号和槽解绑
        self.button.clicked.disconnect(self.change_text)        # 5


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 实例化Demo类
    demo = Demo()                                               # 6
    # 使demo可见
    demo.show()                                                 # 7
    sys.exit(app.exec_())