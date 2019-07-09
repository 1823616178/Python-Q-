import requests
from pyquery import PyQuery as pq
import random


class GetJX3UserImg:
    def __init__(self):
        BaseUrl = ''
        self.list1 = []
        self.imgurl = []
        # self.JxeImageQuery()

    def JxeImageQuery(self):
        data = requests.get("http://jx3.duowan.com/tag/122317626418.html").text
        doc = pq(data)
        for i in doc('#list-page ul li a').items():
            i = "http://jx3.duowan.com" + i.attr('href')
            self.list1.append(i)
        return self.GetImageUrl()

    def GetImageUrl(self):
        url = self.list1[int(random.uniform(1, len(self.list1)))]
        html = requests.get(url).text
        doc = pq(html)
        lft = doc.find("p")
        jsurl = ''
        for i in lft.items():
            if i.attr("align") == "center":
                for j in i('p script').items():
                    if j.attr('src') is not None:
                        jsurl = j.attr('src')

        jsData = requests.get(jsurl)
        jsData = jsData.text.split("showImg")
        for i in range(len(jsData)):
            if (i == len(jsData) - 1):
                continue
            jsonurl = jsData[i + 1].split("url")
            self.imgurl.append(jsonurl[0][3:-3].replace("\/", "/"))
        url = self.imgurl[int(random.uniform(0, len(self.imgurl)))]
        return url

