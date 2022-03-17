# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Translation_2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from new import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys


class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # 给button 的 点击动作绑定一个事件处理函数
        self.pushButton.clicked.connect(self.btn_1)
        self.pushButton_4.clicked.connect(self.btn_4)

    def btn_1(self):
        self.textEdit_2.append(self.input_msg()[3]+'\n')

    def input_msg(self):
        f = open('Android.txt', 'r', encoding='utf-8')
        a = f.read()
        dict_name = eval(a)
        f.close()
        input = self.lineEdit.text()
        qq = dict_name.get(input,0)
        if qq == 0:
            return "查询的posid不存在","查询的posid不存在","查询的posid不存在","查询的posid不存在"
        else:
            name = dict_name[input][0]
            cmdmsg = dict_name[input][1]
            message = 'posid:{}\n广告位名称：{}\ncmd命令:{}'.format(input, name, cmdmsg)
            return input, name, cmdmsg, message
    def btn_4(self):
        self.textEdit.append(self.action())
        self.textEdit.append(self.actionresult())
    def action(self):
        res = os.popen(self.input_msg()[2])
        out_msg= res.read()
        return out_msg
    def actionresult(self):
        check_msg = 'Broadcast completed: result=0'
        slipt_1 = self.action().split('\n')
        result = [x for x in slipt_1 if x != '']
        if check_msg in result:
            acresult = '成功'
        else:
            acresult = '请检查手机是否连接到手机并且打开开发者模式'
        return acresult

