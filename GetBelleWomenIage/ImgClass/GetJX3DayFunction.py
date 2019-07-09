import requests
import random
import json


class GetJx3EveryDay():

    def __init__(self):
        self.BaseUrl = "https://www.jx3tong.com:443/?m=api&c=daily&a=daily_list"

    def GetEveryDay(self):
        DayList = {}
        body = \
            {
                "category_id": 0,
                "add_ad": 1,
                "p": 1,
                "num": 20
            }
        Host = \
            {
                "charset": "UTF-8",
                "Content-Type": "application/x-www-form-urlencoded",
                # "Content-Length": 33,
                "Host": "www.jx3tong.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/3.9.0"
            }

        Data = requests.post(self.BaseUrl, headers=Host, data=json.dumps(body)).json()
        for dilay in Data['activity_data']:
            for context in dilay['activity_list']:
                if context['title'].find('大战') >= 0:
                    dic = {'dazhan': context['title']}
                    DayList.update(dic)
                if context['title'].find('战场') >= 0:
                    dic = {'zhanchang': context['title']}
                    DayList.update(dic)
                if context['title'].find("小攻防") >= 0:
                    dic = {'small': context['title']}
                    DayList.update(dic)
                if context['title'].find("大攻防") >= 0:
                    dic = {'small': context['title']}
                    DayList.update(dic)
        dic = {
            "datatime": Data['update_time']
        }
        DayList.update(dic)
        return json.dumps(DayList)
