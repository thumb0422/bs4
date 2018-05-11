# -*- coding: UTF-8 -*-
# 抓取代理IP
import urllib.request
import urllib
import re
import time
import random
import socket
import threading

class proxy_IP:
    def __init__(self):
        self.ip_totle = []
        self.proxy_ip = open('proxy_ip.txt', 'w')  # 新建一个储存有效IP的文档
        self.lock = threading.Lock()  # 建立一个锁
        # 整理代理IP格式
        self.proxys = []

    def initData(self):
        for page in range(1, 6):
            # url = 'http://ip84.com/dlgn/' + str(page)
            url='http://www.xicidaili.com/nn/'+str(page) #西刺代理
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64)"}
            request = urllib.request.Request(url=url, headers=headers)
            response = urllib.request.urlopen(request)
            content = response.read().decode('utf-8')
            pattern = re.compile('<td>(\d.*?)</td>')  # 截取<td>与</td>之间第一个数为数字的内容
            ip_page = re.findall(pattern, str(content))
            self.ip_totle.extend(ip_page)
            time.sleep(random.choice(range(1, 3)))
        for i in range(0, len(self.ip_totle), 4):
            proxy_host = self.ip_totle[i] + ':' + self.ip_totle[i + 1]
            proxy_temp = {"http": proxy_host}
            self.proxys.append(proxy_temp)


    # 验证代理IP有效性的方法
    def test(self,i):
        socket.setdefaulttimeout(5)  # 设置全局超时时间
        url = "http://www.baidu.com"
        try:
            proxy_support = urllib.request.ProxyHandler(self.proxys[i])
            opener = urllib.request.build_opener(proxy_support)
            opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64)")]
            urllib.request.install_opener(opener)
            res = urllib.request.urlopen(url).read()
            self.lock.acquire()  # 获得锁
            self.proxy_ip.write(str(self.proxys[i])+'\n')  # 写入该代理IP
            self.lock.release()  # 释放锁
            print(str(self.proxys[i]),' is ok')
        except Exception as e:
            self.lock.acquire()
            print(self.proxys[i], e)
            self.lock.release()

    def checkIPValids(self):
        self.initData()
        # 多线程验证
        threads = []
        for i in range(len(self.proxys)):
            thread = threading.Thread(target=self.test, args=[i])
            threads.append(thread)
            thread.start()
        # 阻塞主进程，等待所有子线程结束
        for thread in threads:
            thread.join()

        self.proxy_ip.close()  # 关闭文件