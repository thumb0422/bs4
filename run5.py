# -*- coding: UTF-8 -*-
from proxy import ProxySend



sendRequest = ProxySend("http://www.baidu.com")
rspCode = sendRequest.sendRequest()
