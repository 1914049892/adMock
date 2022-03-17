from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.t = 0
        window = QWidget()
        vbox = QVBoxLayout(window)
        # vbox = QVBoxLayout(window)

        self.lcdNumber = QLCDNumber()
        button = QPushButton("测试")
        vbox.addWidget(self.lcdNumber)
        vbox.addWidget(button)

        self.timer = QTimer()

        self.button.clicked.connect(self.work)  ###########################
        self.timer.timeout.connect(self.counttime)  ###########################定时器超出此时间就触发信号

        self.setLayout(vbox)
        self.show()

    def CountTime(self):
        self.t += 1
        self.lcdNumber.display(self.t)

    def Work(self):
        self.timer.start(1000)
        self.thread = RunThread()  #
        self.thread.start()  # 启动线程
        self.thread.trigger.connect(self.TimeStop)  # 一旦线程中信号传来，就执行TimeStop函数

    def TimeStop(self):
        self.timer.stop()
        print("运行结束用时", self.lcdNumber.value())
        self.t = 0


class RunThread(QThread):
    trigger = pyqtSignal()  # 新建一个信号

    def __init__(self, parent=None):
        super(RunThread, self).__init__()

    def run(self):  # 重写run函数
        # 这里写主要逻辑，如下面for循环例子
        #
        #
        for i in range(203300030):
            pass
        self.trigger.emit()  # 一旦for循环执行完，就触发这个信号
        # self._signal.emit(msg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    th = Example()
    th.show()
    sys.exit(app.exec_())