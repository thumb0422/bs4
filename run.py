# -*- coding=utf-8 -*-
import datetime
import urllib
from threading import Thread

urlStr = 'https://www.toutiao.com/i6537157013078540814/' #执行网址
threadCount = 100  #线程数量
threadColumn = 100 #每个线程执行次数

class MyThread(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        for i in range(0, threadColumn):
            from urllib.request import Request, urlopen
            from urllib.error import URLError
            req = Request(urlStr)
            try:
                response = urlopen(req)
            except URLError as e:
                print('异常线程:',self.name,',第',str(i),'次开始打开网页:', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
            else:
                print('线程: ',self.name,' ,第',str(i),'次开始打开网页:', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))

print('开始:',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
for i in range(0,threadCount):
    threadTmp = MyThread(str(i))
    threadTmp.start()