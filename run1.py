# -*- coding=utf-8 -*-
import datetime
from threading import Thread
import urllib

urlStr = 'https://www.toutiao.com/i6537157013078540814/' #执行网址
threadCount = 100  #线程数量
threadColumn = 100 #每个线程执行次数

class MyThread(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        for i in range(0, threadColumn):
            res = urllib.urlopen(urlStr)
            print('subThread ',self.name,' Start:It is',str(i),'time open:', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))

print('mainThread Start:',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
for i in range(0,threadCount):
    threadTmp = MyThread(str(i))
    threadTmp.start()