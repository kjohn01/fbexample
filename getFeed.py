#!/usr/bin/python
# -*- coding: latin-1 -*-
import requests
import json
import pandas as pd
from dateutil.parser import parse

token = 'EAACEdEose0cBANKDqQ2ZBbleC9yF9diyLZABMT5H7oxm0zraQ20F05VnhN5yZBFLL6gXxoUNuTlGZCvWSTAiiDxXQ6TYfl27lvOGY4TJhTHZCbDmzNP8dUIDrZBvFXzhbxpxArOnEi9x73JJ3kx78z2sAIZCPEaonS5fUnwpOfA5vGmTLSAtBPJ'

group = {'689157281218904':'台北技能交換'}

feeds = []

for ele in group:
    res = requests.get('https://graph.facebook.com/v2.9/{}/feed?limit=100&access_token={}'.format(ele, token))

    while 'paging' in res.json():
        for information in res.json()['data']:
            if 'message' in information:
                feeds.append([group[ele], information['message'], parse(information['updated_time']).date(), information['id']])
        res = requests.get(res.json()['paging']['next'])

print(json.dump(feeds, sort_keys=True, indent=4, separators=(',', ': ')))
#最後將list轉換成dataframe，並輸出成csv檔
#
# information_df = pd.DataFrame(feeds, columns=['粉絲專頁', '發文內容', '發文時間'])
# information_df.to_csv('Data Visualization Information.csv', index=False)
