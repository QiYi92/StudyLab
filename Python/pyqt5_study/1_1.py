import sys
from PyQt5.QtWidgets import QApplication, QLabel


if __name__ == '__main__':
    # 实例化QApplication 并传入sys.argv参数
    app = QApplication(sys.argv)  # 1
    # 实例化QLabel控件，用来展示文字或图片
    label = QLabel("Hello World") # 2
    # 调用show()方法让控件处于可见状态（默认是隐藏）
    label.show()                  # 3
    # app.exec_()是执行应用，让应用开始运转
    # 窗口关闭返回0给sys.exit()即可让程序退出
    sys.exit(app.exec_())         # 4