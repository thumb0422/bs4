# -*- coding: UTF-8 -*-
from proxy import ProxySend
import datetime
from threading import Thread

urlStr = 'https://www.toutiao.com/i6536031732813005316/'
# 2018年巴塞尔表展新品： 浪琴表嘉岚系列呈献蓝色超薄魅力
threadCount = 10  #线程数量
threadColumn = 50 #每个线程执行次数

sendRequest = ProxySend(urlStr)

class MyThread(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        for i in range(0, threadColumn):
            rspCode = sendRequest.sendRequest()
            print('subThread : respCode = ',rspCode,' ',self.name,' ',' Start:It is',str(i),' time open:', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))

print('mainThread Start:',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
for i in range(0,threadCount):
    threadTmp = MyThread(str(i))
    threadTmp.start()