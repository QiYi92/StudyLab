import sys
from PyQt5.QtCore import pyqtSignal                             # 1
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
# 导入pyqtSignal


class Demo(QWidget):
    # 实例化一个自定义信号
    my_signal = pyqtSignal()                                    # 2

    def __init__(self):
        super(Demo, self).__init__()
        self.label = QLabel('Hello World', self)
        # 将自定义的信号连接到自定义的槽函数上
        self.my_signal.connect(self.change_text)                # 3

    def change_text(self):
        if self.label.text() == 'Hello World':
            self.label.setText('Hello PyQt5')
        else:
            self.label.setText('Hello World')

    # 使用自带的mousePressEvent()方法，这里来自QWidget
    # 监控鼠标是否按下，如果鼠标被按下，则会发出自定义信号。
    def mousePressEvent(self, QMouseEvent):                     # 4
        self.my_signal.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())