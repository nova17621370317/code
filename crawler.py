# _*_ coding: utf-8 _*_

import urllib2
import requests
import ssl

def crawler(url):
    ssl._create_default_https_context = ssl._create_unverified_context
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    req = urllib2.Request(url,headers=headers)
    html = urllib2.urlopen(url,req)

if __name__ == '__main__':
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-07-25&leftTicketDTO.from_station=SHH&leftTicketDTO.to_station=HKN&purpose_codes=ADULT'

