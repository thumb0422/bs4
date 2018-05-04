# -*- coding: utf-8 -*-
# import urllib.request
# import urllib.error
import urllib
import urllib2
import re
import time
import random

class ObtainProxy:
    def __init__(self, region='国内普通'):

        self.region = {'国内普通': 'nt/', '国内高匿': 'nn/', '国外普通': 'wt/', '国外高匿': 'wn/', 'SOCKS': 'qq/'}

        self.url = 'http://www.xicidaili.com/' + self.region[region]
        self.header = {}
        self.header[
            'User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'

    def get_prpxy(self):

        req = urllib2.Request(self.url, headers=self.header)
        resp = urllib2.urlopen(req)
        content = resp.read()

        self.get_ip = re.findall(r'(\d+\.\d+\.\d+\.\d+)</td>\s*<td>(\d+)</td>', content)

        self.pro_list = []
        for each in self.get_ip:
            a_info = each[0] + ':' + each[1]
            self.pro_list.append(a_info)

        return self.pro_list

# 创建get方法
def get(url,proxies):
    random_proxy = random.choice(proxies)
    proxy_support = urllib2.ProxyHandler({"http": random_proxy})
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)
    code = urllib2.urlopen(url).code
    return code

if __name__ == '__main__':
    url = "https://www.toutiao.com/i6546394013665067528/"
    proxy = ObtainProxy()
    proxies = proxy.get_prpxy()
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36"
    headers = {'User-Agent':user_agent}
    req = urllib2.Request(url, headers=headers)
    i = 1
    while i<100:
    # 添加参数
        code = get(url,proxies)
        print('第'+str(i)+'次代理访问:')
        i = i+1