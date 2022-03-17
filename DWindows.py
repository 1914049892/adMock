# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Translation_2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import requests
import time

from PyQt5.QtCore import pyqtSignal

from double import Ui_TabWidget
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys
import time
class Runthread(QtCore.QThread):
    _signal = pyqtSignal(str)

    def __init__(self):
        super(Runthread, self).__init__()

    #def __del__(self):
        #self.wait()

    def run(self):
        for i in range(20):
            time.sleep(0.2)
            self._signal.emit(str(i))  # 注意这里与_signal = pyqtSignal(str)中的类型相同

class TabWidget(QtWidgets.QTabWidget,Ui_TabWidget):
    def __init__(self, parent=None):
        super(TabWidget, self).__init__(parent)
        self.setupUi(self)
        self.thread = None
        # 给button 的 点击动作绑定一个事件处理函数
        self.pushButton.clicked.connect(self.findmsg_1)
        self.pushButton_4.clicked.connect(self.btn_4)
        self.pushButton_7.clicked.connect(self.IOS_2_result)
        self.pushButton_10.clicked.connect(self.IOS_4_result)
        self.pushButton_12.clicked.connect(self.IOS_3_result)
        self.pushButton_13.clicked.connect(self.IOS_5_result)
        self.pushButton_9.clicked.connect(self.IOS_6_result)
    #展示安卓查询信息
    def findmsg_1(self):
        self.textEdit_2.append(self.input_msg()[3]+'\n')
    #安卓查询信息
    def input_msg(self):
        if len(self.lineEdit.text())==0:
            return '请输入posid','请输入posid','请输入posid','请输入posid'
        else:
            input = self.lineEdit.text()
        f1 = open('Android.txt', 'r', encoding='utf-8')
        a1 = f1.read()
        dict_name = eval(a1)
        f1.close()

        qq = dict_name.get(input,0)
        if qq == 0:
            return "查询的posid不存在","查询的posid不存在","查询的posid不存在","查询的posid不存在"
        else:
            name = dict_name[input][0]
            cmdmsg = dict_name[input][1]
            message = 'posid:{}\n广告位名称：{}\ncmd命令:{}'.format(input, name, cmdmsg)
            return input, name, cmdmsg, message
    #发送安卓mock动作信息
    def btn_4(self):
        #self.textEdit.append(self.action()+'\n')
        self.textEdit.append(self.actionresult()+'\n')

    #mock动作信息
    def actionresult(self):
        mm = self.input_msg()[2]
        if mm == '请输入posid':
            return '请输入posid'
        elif mm == "查询的posid不存在":
            return "查询的posid不存在"
        else:
            res = os.popen(self.input_msg()[2])
            out_msg = res.read()
        if len(out_msg) == 0:
            return 'error: no devices/emulators found'
        else:
            check_msg = 'Broadcast completed: result=0'
            slipt_1 = out_msg.split('\n')
            result = [x for x in slipt_1 if x != '']
            if check_msg in result:
                return 'mock 成功'
            else:
                return '请检查手机是否连接,并且打开开发者模式'
    #IOS查询广告信息
    def IOS_1(self):
        if len(self.lineEdit_2.text())==0:
            return '输入posid','输入posid','输入posid','输入posid'
        else:
            input = self.lineEdit_2.text()
        f2 = open('ios.txt', 'r', encoding='utf-8')
        a2 = f2.read()
        dict_name = eval(a2)
        f2.close()

        qq = dict_name.get(input, 0)
        if qq == 0:
            return "查询的posid不存在", "查询的posid不存在", "查询的posid不存在", "查询的posid不存在"
        else:
            name = dict_name[input][0]
            acmsg = dict_name[input][1]
            message = 'posid:{}\n广告位名称：{}\n命令:{}'.format(input, name, acmsg)
            return input, name, acmsg, message
    #IOS发送广告查询信息
    def IOS_2_result(self):
        self.textEdit_5.append(self.IOS_1()[3]+'\n')

    #IOS连接手机
    def IOS_3(self):

        if len(self.lineEdit_3.text())==0:
            return '请输入手机ip'
        else:
            ipmsg = self.lineEdit_3.text()
        try:
            response = requests.get('http://'+ipmsg+':12345/getEnv')
            time.sleep(5)
            print(response.raise_for_status())
            #response.encoding = response.apparent_encoding
            respect = response.json()['data']

            if respect==0:
                return '当前是联调站'
            elif respect == 1:
                return 'live站'
            elif respect == 2:
                return '当前是预发布站'
            elif respect == 3:
                return '当前是正式站'

        except:
            return '产生异常,重启斗鱼'

    #IOS发送连接手机信息
    def IOS_3_result(self,msg):

        self.textEdit_6.append(self.IOS_3()+'\n')
    #IOS 开启MOCK信息
    def IOS_4(self):
        if len(self.lineEdit_2.text())==0:
            return'请输入posid'
        else:
            ipm= self.lineEdit_3.text()
        if len(self.lineEdit_3.text())==0:
            return'请输入手机IP'
        else:

            idm = self.IOS_1()[2]
        try:
            ac_2=requests.get('http://'+ipm+idm)
            print(ac_2.raise_for_status())
            ac_2.encoding = ac_2.apparent_encoding
            respect = ac_2.json()['error']
            print(respect)
            if respect==0:
                return 'Mock成功,记得重启斗鱼哦'
            else:
                return '重试'
        except:
            return '产生异常,重启斗鱼'

    #IOS发送开启MOck消息
    def IOS_4_result(self):
        self.textEdit_6.append(self.IOS_4()+'\n')
    #关闭mock信息
    def IOS_5(self):
        try:
            clock = requests.get('http://'+self.lineEdit_3.text()+':12345/disableHttpMock')
            print(clock.raise_for_status())
            clock.encoding = clock.apparent_encoding
            respect = clock.json()['error']
            print(respect)
            if respect==0:
                return '关闭Mock成功'
            else:
                return '重试'
        except:
            return '产生异常,重启斗鱼'
    #IOS发送关闭mock信息
    def IOS_5_result(self):
        self.textEdit_6.append(self.IOS_5()+'\n')

    #IOS切换环境信息
    def IOS_6(self):
        if len(self.lineEdit_3.text())==0:
            return'请打开斗鱼app'
        else:
            url = 'http://'+self.lineEdit_3.text()+':12345/switchEnv?'
        incombox = self.comboBox.currentText()
        dic = {'联调站':'0','live站':'1','预发布站':'2','正式站':'3'}
        kw={'env':dic[incombox]}
        try:
            check = requests.get(url,params=kw)
            print(check.raise_for_status())
            check.encoding = check.apparent_encoding
            respect = check.json()['error']
            print(respect)
            if respect==0:
                return '切换成功,目前为{}'.format(incombox)
            else:
                return '检查ip地址'
        except:
            return '检查IP地址'
    #发送IOS切换环境信息
    def IOS_6_result(self):
        self.textEdit_6.append(self.IOS_6()+'\n')
