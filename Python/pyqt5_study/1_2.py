import sys
from PyQt5.QtWidgets import QApplication, QLabel


if __name__ == '__main__':
    # 实例化QApplication 并传入sys.argv参数
    app = QApplication(sys.argv)  # 1
    # 实例化QLabel控件，用来展示文字或图片
    # 可以直接添加html代码，修改文本样式
    label = QLabel('<font color="blue">Hello</font> <h2>World</h2>') # 2
    # 调用show()方法让控件处于可见状态（默认是隐藏）
    label.show()                  # 3
    # app.exec_()是执行应用，让应用开始运转
    # 窗口关闭返回0给sys.exit()即可让程序退出
    # app.exec_()函数用来执行应用
    # sys.exit()函数用来退出程序
    sys.exit(app.exec_())         # 4