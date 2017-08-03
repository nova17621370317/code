# _*_ coding: utf-8 _*_

import requests
import json


headers = {'Content-Type':'application/json'}
gps_data = {

}

url = 'dev_supply'
req = requests.post(url,headers=headers,gps_data)

