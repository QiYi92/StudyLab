import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.button = QPushButton('Start', self)
        self.button.pressed.connect(self.button.released)  # 1
        self.button.released.connect(self.change_text)     # 2
        """
        将pressed信号和released信号连接起来，而released信号则与槽函数连接。
        这样当点击不放时，pressed信号发出，released信号也会发出，从而启动槽函数。
        释放鼠标则发出released信号，再次启动槽函数。
        所以程序运行效果跟2_2小节其实是一样的。
        """

    def change_text(self):
        if self.button.text() == 'Start':
            self.button.setText('Stop')
        else:
            self.button.setText('Start')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())