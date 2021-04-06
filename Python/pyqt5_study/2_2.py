import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.button = QPushButton('Start', self)
        # pressed: 当鼠标在button上并点击左键的时候，触发信号
        self.button.pressed.connect(self.change_text)     # 1
        # released: 当鼠标左键被释放的时候触发信号
        self.button.released.connect(self.change_text)    # 2
        # 将pressed和released信号连接搭配change_text()槽函数上

    def change_text(self):
        # 若当前按钮文本为‘Start’，则将文本改为‘Stop’
        # 若为‘Stop’，则改为‘Start’
        if self.button.text() == 'Start':                 # 3
            self.button.setText('Stop')
        else:
            self.button.setText('Start')
        """
        所以当鼠标点击按钮不放时，发出pressed信号
        调用槽函数，将‘Start’文本改为‘Stop’
        当鼠标放开后释放released信号，再次调用槽函数，将文本改回‘Start’。
        """

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())