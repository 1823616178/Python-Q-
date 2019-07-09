import requests
import random
from pyquery import PyQuery as pq


class GetYellowNumber:
    def __init__(self):
        self.baseUrl = "https://tongbird.ru/explore/trending/?list=images&sort=views_desc&page="
        self.GetPageUrl()
    def GetPageUrl(self):
        imgList = []
        data = requests.get(self.baseUrl + str(int(random.uniform(1, 10))))
        html = pq(data.text)
        imgpage = html(".list-item-image.fixed-size a img").items()
        for i in imgpage:
            imgList.append(i.attr("src"))
        print(imgList[int(random.uniform(0, len(imgList)))])
        return imgList[int(random.uniform(0, len(imgList)))]

