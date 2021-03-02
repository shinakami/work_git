from selenium import webdriver
from time import sleep
import random as rd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
from fake_useragent import UserAgent
import os
import re
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import loguru
import pyquery
from tqdm import tqdm
os.system('cls')
def getProxiesFromFreeProxyList():
    proxies = []
    url = 'https://free-proxy-list.net/'
    loguru.logger.debug(f'getProxiesFromFreeProxyList: {url}')
    loguru.logger.warning(f'getProxiesFromFreeProxyList: downloading...')
    response = requests.get(url)
    if response.status_code != 200:
        loguru.logger.debug(f'getProxiesFromFreeProxyList: status code is not 200')
        return
    loguru.logger.success(f'getProxiesFromFreeProxyList: downloaded.')
    d = pyquery.PyQuery(response.text)
    trs = list(d('table#proxylisttable > tbody > tr').items())
    loguru.logger.warning(f'getProxiesFromFreeProxyList: scanning...')
    IPPool = []
    for tr in trs:
        # 取出所有資料格
        tds = list(tr('td').items())
        # 取出 IP 欄位值
        ip = tds[0].text().strip()
        # 取出 Port 欄位值
        port = tds[1].text().strip()
        # 取出匿名性
        anom = tds[4].text().strip()
        # 組合 IP 代理
        if anom == 'level3':
            proxy = f'{anom}:{ip}:{port}'
            proxies.append(proxy)
            IPPool.append(pd.DataFrame([{'IP':ip, 'Port':port}]))
    IPPool = pd.concat(IPPool, ignore_index=True)
    loguru.logger.success(f'getProxiesFromFreeProxyList: scanned.')
    loguru.logger.debug(f'getProxiesFromFreeProxyList: {len(proxies)} level3 proxies is found.')
    return IPPool



def IPcheater():

    ActIps = getProxiesFromFreeProxyList()
    options = webdriver.ChromeOptions()
    proxy = 'http://'+ActIps['IP'][0]+':'+ActIps['Port'][0]
    options.add_argument(('–proxy-server='+proxy))
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=options)
    os.system('cls')
    print('–proxy-server='+proxy)
    IPPool = []
    for i in range(1,6):
        # 用迴圈逐一打開分頁
        url = 'http://free-proxy.cz/zh/proxylist/country/all/https/ping/level1'.format(i)
        print('Dealing with {}'.format(url))
        driver.get(url)
        soup = BeautifulSoup(driver.page_source)
        for j in soup.select('tbody > tr'):
            if re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', str(j)):
                IP = re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', str(j))
                Port = re.findall('class="fport" style="">(.*?)</span>', str(j))
                IPPool.append(pd.DataFrame([{'IP':IP, 'Port':Port}]))
        print('There are {} IPs in Pool'.format(len(IPPool)))
    IPPool = pd.concat(IPPool, ignore_index=True)
    #print(IPPool)

    ActIps = []
    for IP, Port in zip(IPPool['IP'],IPPool['Port']):
        if len(IP) >= 1 and len(Port) >= 1:
            proxy = {'http':'http://'+ IP[0] + ':' + Port[0],
                    'https':'https://'+ IP[0] + ':' + Port[0]} 
            print(proxy)
            try:
                # 隨機找的一篇新聞即可
                url = 'https://www.youtube.com/watch?v=tfHHtMm37BI'
                resp = requests.get(url, proxies=proxy, timeout=2)
                if str(resp.status_code) == '200':
                    ActIps.append(pd.DataFrame([{'IP':IP[0], 'Port':Port[0]}]))
                    print('Succed: {}:{}'.format(IP, Port), 'code: ', resp.status_code)
                else:
                    print('Failed: {}:{}'.format(IP, Port), 'code: ', resp.status_code)
            except:
                    print('Failed: {}:{}'.format(IP, Port), 'code: NULL')
    ActIps = pd.concat(ActIps, ignore_index=True)
    print(ActIps)
    return ActIps


def IPmoder():
    print("IPmoder start")
    IPPool = []
    for i in range(666):
        IP = str(rd.randint(0,255)) + '.' + str(rd.randint(0,255)) + '.' + str(rd.randint(0,255)) + '.' + str(rd.randint(0,255))
        Port = str(rd.randint(0, 100000))
        IPPool.append(pd.DataFrame([{'IP':IP, 'Port':Port}]))
    IPPool = pd.concat(IPPool, ignore_index=True)
    return IPPool

    #ActIps = []
    #for IP, Port in zip(IPPool['IP'],IPPool['Port']):
    #    if len(IP) >= 1 and len(Port) >= 1:
    #        proxy = {'http':'http://'+ IP + ':' + Port,
    #                'https':'https://'+ IP + ':' + Port} 
    #        try:
    #            # 隨機找的一篇新聞即可
    #            url = 'https://www.youtube.com/watch?v=tfHHtMm37BI'
    #            resp = requests.get(url, proxies=proxy, timeout=2)
    #            if str(resp.status_code) == '200':
    #                ActIps.append(pd.DataFrame([{'IP':IP, 'Port':Port}]))
    #                print('Succed: {}:{}'.format(IP, Port), 'code: ', resp.status_code)
    #            else:
    #                print('Failed: {}:{}'.format(IP, Port), 'code: ', resp.status_code)
    #        except:
    #                print('Failed: {}:{}'.format(IP, Port), 'code: NULL')
    #ActIps = pd.concat(ActIps, ignore_index=True)
    #print(ActIps)
    #return ActIps


#ActIps = IPmoder()
#ActIps = IPcheater()
ActIps = getProxiesFromFreeProxyList()
ops=[]
ip = []
ID = []
for i in range(5):
    ops.append('')
    ops[i] = webdriver.ChromeOptions()
    user = UserAgent()
    us_a = user.chrome
    ID.append('')
    ip.append('')
    ID[i] = us_a
    IP_noot = rd.randint(0, len(ActIps['IP'])-1)
    Port_noot = rd.randint(0, len(ActIps['Port'])-1)
    ip[i] = ActIps['IP'][IP_noot]+':'+ActIps['Port'][Port_noot]
    proxy = 'https://'+ActIps['IP'][IP_noot]+':'+ActIps['Port'][Port_noot]
    ops[i].add_argument('user-agent='+us_a)
    ops[i].add_argument(('–proxy-server='+proxy))
    ops[i].add_argument("--mute-audio")
driver1 = webdriver.Chrome(executable_path='chromedriver', chrome_options=ops[0])
os.system('cls')
driver2 = webdriver.Chrome(executable_path='chromedriver', chrome_options=ops[1])
os.system('cls')
driver3 = webdriver.Chrome(executable_path='chromedriver', chrome_options=ops[2])
os.system('cls')
driver4 = webdriver.Chrome(executable_path='chromedriver', chrome_options=ops[3])
os.system('cls')
driver5 = webdriver.Chrome(executable_path='chromedriver', chrome_options=ops[4])
os.system('cls')
driver_root = [driver1, driver2, driver3, driver4, driver5]
os.system('cls')
net_root1 = ['https://www.youtube.com/watch?v=g78E87yt7fA', 'https://www.youtube.com/watch?v=MxsUinFbKvg' 
            ,'https://www.youtube.com/watch?v=Nqgw09nnpr8', 'https://www.youtube.com/watch?v=AM9xU9WC7do'
            ,'https://www.youtube.com/watch?v=ZqcDdqdEOM8', 'https://www.youtube.com/watch?v=4qJPYCRqCNE'
            ,'https://www.youtube.com/watch?v=PECjdj-qFrE', 'https://www.youtube.com/watch?v=1Zouz94vHMk'
            ,'https://www.youtube.com/watch?v=FiIL52UD-zM', 'https://www.youtube.com/watch?v=25ClrbBb5fI'
            ,'https://www.youtube.com/watch?v=cLmF2_g-DIo', 'https://www.youtube.com/watch?v=27bH55gqc7c'
            ,'https://www.youtube.com/watch?v=ayePHBk6q5M', 'https://www.youtube.com/watch?v=L1x4GGUV0i4'
            ,'https://www.youtube.com/watch?v=sqJgwUVO_R8', 'https://www.youtube.com/watch?v=sqJgwUVO_R8'
            ,'https://www.youtube.com/watch?v=JLz9cRxwTZg', 'https://www.youtube.com/watch?v=JLz9cRxwTZg'
            ,'https://www.youtube.com/watch?v=bDAb8ocgULo', 'https://www.youtube.com/watch?v=bDAb8ocgULo'
            ,'https://www.youtube.com/watch?v=49X2OfhlZCA', 'https://www.youtube.com/watch?v=49X2OfhlZCA'
            ,'https://www.youtube.com/watch?v=JIhGw48tv80', 'https://www.youtube.com/watch?v=JIhGw48tv80'
            ,'https://www.youtube.com/watch?v=JIhGw48tv80', 'https://www.youtube.com/watch?v=JIhGw48tv80'
            ,'https://www.youtube.com/watch?v=RkXm-nSiu9g', 'https://www.youtube.com/watch?v=N7M2R0vHfx8']


net = [net_root1]
time_sleep = 0

while True :


    os.system('cls')
    if time_sleep == 2077:
        for driver_boot in driver_root:
            driver_boot.delete_all_cookies()
        sleep_time = rd.randint(10, 600)
        print('sleeping time baby!:',sleep_time)
        sleep(sleep_time)
        time_sleep = 0
        ActIps = IPmoder()
        #ActIps = IPcheater()
        ops=[]
        ip = []
        ID = []
        for i in range(5):
            ops.append('')
            ops[i] = webdriver.ChromeOptions()
            user = UserAgent()
            us_a = user.chrome
            ID.append('')
            IP_noot = rd.randint(0, len(ActIps['IP'])-1)
            Port_noot = rd.randint(0, len(ActIps['Port'])-1)
            ip[i] = ActIps['IP'][IP_noot]+':'+ActIps['Port'][Port_noot]
            ID[i] = us_a
            proxy = 'https://'+ActIps['IP'][IP_noot]+':'+ActIps['Port'][Port_noot]
            ops[i].add_argument('user-agent='+us_a)
            ops[i].add_argument(('–proxy-server='+proxy))
            ops[i].add_argument("--mute-audio")
        driver1 = webdriver.Chrome(executable_path='chromedriver', chrome_options=ops[0])
        os.system('cls')
        driver2 = webdriver.Chrome(executable_path='chromedriver', chrome_options=ops[1])
        os.system('cls')
        driver3 = webdriver.Chrome(executable_path='chromedriver', chrome_options=ops[2])
        os.system('cls')
        driver4 = webdriver.Chrome(executable_path='chromedriver', chrome_options=ops[3])
        os.system('cls')
        driver5 = webdriver.Chrome(executable_path='chromedriver', chrome_options=ops[4])
        os.system('cls')
        driver_root = [driver1, driver2, driver3, driver4, driver5]
        os.system('cls')

    os.system('cls')
    for i in range(5):    
        print(ID[i])
        print(ip[i])
        sleep(1)
    nt = 0
    time_sleep = time_sleep + 1
    time = 480
    net_root = net[nt]
    ch = rd.randint(0, len(net_root)-1)
    ch2 = rd.randint(0, len(net_root)-1)
    ch3 = rd.randint(0, len(net_root)-1)
    ch4 = rd.randint(0, len(net_root)-1)
    ch5 = rd.randint(0, len(net_root)-1)
    while(ch == ch2 or ch == ch3 or ch==ch4 or ch==ch5 or ch2==ch3 or ch2==ch4 or ch2==ch5 or ch3==ch4 or ch3==ch5 or ch4==ch5):
        ch = rd.randint(0, len(net_root)-1)
        ch2 = rd.randint(0, len(net_root)-1)
        ch3 = rd.randint(0, len(net_root)-1)
        ch4 = rd.randint(0, len(net_root)-1)
        ch5 = rd.randint(0, len(net_root)-1)
    ch_root = [ch, ch2, ch3, ch4, ch5]
 
    print('delay_time:', time, 'time-step: ', time_sleep, 'net root num: ', nt)
    print('ch1: ', ch, 'ch2: ', ch2, 'ch3: ', ch3, 'ch4: ', ch4, 'ch5: ', ch5)
    i = 0
    with tqdm(total=5) as pbar: 
        for driver_boot in driver_root:
            driver_boot.get(net_root[ch_root[i]])
            pbar.update(1)
            i = i + 1
    with tqdm(total=time) as tbar:
        for i in range(time):
            sleep(1)
            tbar.update(1)
    #sleep(time)
    for driver_boot in driver_root:
        driver_boot.delete_all_cookies()
        driver_boot.refresh()