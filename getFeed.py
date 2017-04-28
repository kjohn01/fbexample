#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import json
import datetime
import pandas as pd
from dateutil.parser import parse

def handleDate(x):
    if isinstance(x, datetime.date):
        return "{}-{}-{}".format(x.year, x.month, x.day)

token = 'EAACEdEose0cBADNqQCOerYjMBsE5iiUp79vrqnh3FhoYWZAPmaZBfdsuZCi43IpZBsC7S2xICxNQunP2nZB2ENrMqM5r4KyZBA7Km1fLxzvrIvNUUE9KZCdhzwS2lf2ZCRUYBT3GhfirlGa3W0zASZC7tOUkZBpGpx1ENQSdbYZC2NeswAEsjKeZAGIM'

group = {'689157281218904':'台北技能交換'}

feeds = []

for ele in group:
    res = requests.get('https://graph.facebook.com/v2.9/{}/feed?limit=100&access_token={}'.format(ele, token))

    while 'paging' in res.json():
        for information in res.json()['data']:
            if 'message' in information:
                feeds.append([group[ele], information['message'], parse(information['updated_time']).date(), information['id']])
        res = requests.get(res.json()['paging']['next'])

# print(json.dumps(feeds, indent=4, separators=(',', ': '), ensure_ascii=False, default = handleDate))

with open('feeds.json', 'w') as outfile:
    json.dump(feeds, outfile, indent=4, separators=(',', ': '), ensure_ascii=False, default = handleDate)

#最後將list轉換成dataframe，並輸出成csv檔
#
# information_df = pd.DataFrame(feeds, columns=['粉絲專頁', '發文內容', '發文時間'])
# information_df.to_csv('Data Visualization Information.csv', index=False)
