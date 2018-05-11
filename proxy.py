# -*- coding: UTF-8 -*-
# 代理IP发送网页请求
import os
from urllib import request
from random import choice
from config import userAgents
from proxy_ip import proxy_IP

class ProxySend():
    def __init__(self,url):
        self.url = url
        self.ipArrays = self.readIPArrayFromLocal()

    def sendRequest(self):
        if len(self.ipArrays) < 1:
            print('I can not find any useful IPAddress!!!!!!!!!!!!!!!!please check it')
            return
        # 访问网址
        url = self.url
        # url = 'http://www.baidu.com/'
        # url = 'http://www.whatismyip.com.tw/' #访问这个地址可以获取本机IP

        # 这是代理IP
        proxy = {'http': choice(self.ipArrays)}#随机一个代理IP
        print('current request Address is ',proxy)
        try:
            # 创建ProxyHandler
            proxy_support = request.ProxyHandler(proxy)
            # 创建Opener
            opener = request.build_opener(proxy_support)
            # 添加User Angent
            opener.addheaders = [('User-Agent', choice(userAgents))]
            # 安装OPener
            request.install_opener(opener)
            # 使用自己安装好的Opener
            response = request.urlopen(url)
            # 读取相应信息并解码
            html = response.read().decode("utf-8")
            # 返回状态
            code = response.code
            # 打印信息
            print('current request status is ', code)
        except Exception as e:
            print('current request error is ', e)
            code = "-1"

        return code

    def readIPArrayFromLocal(self):
        fileName = "proxy_ip.txt"
        tmpIpAddress = []
        if os.path.isfile(fileName):
            with open('proxy_ip.txt') as f:
                for line in f:
                    linesArray = line.split(":")
                    ip = linesArray[1].replace("\\","").replace("'","").replace(" ","")
                    port = linesArray[2].replace("\\", "").replace("'", "").replace("}","").replace("\n","").replace(" ","")
                    address = ip+':'+port
                    print('request Address = ',address)
                    tmpIpAddress.append(address)
        else:
            proxyIP = proxy_IP()
            proxyIP.checkIPValids()
        return tmpIpAddress
