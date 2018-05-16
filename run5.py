# -*- coding: UTF-8 -*-
from proxy import ProxySend
import datetime
from threading import Thread

urlStr = 'https://www.toutiao.com/i6556004024666030605/'
# 父亲节就要到了，选什么礼物最贴心？浪琴表温情呈献
threadCount = 40  #线程数量
threadColumn = 50 #每个线程执行次数

sendRequest = ProxySend(urlStr)

class MyThread(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        for i in range(0, threadColumn):
            rspCode = sendRequest.sendRequest()
            if rspCode == -2:
                print('I can not find any useful IPAddress!!!!!!!!!!!!!!!!please check it')
                break
            elif rspCode == 200:
                print('subThread : respCode = ',rspCode,' ',self.name,' ',' Start:It is',str(i),' time open:', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
            else:
                print('error hanpaend')

print('mainThread Start:',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
for i in range(0,threadCount):
    threadTmp = MyThread(str(i))
    threadTmp.start()