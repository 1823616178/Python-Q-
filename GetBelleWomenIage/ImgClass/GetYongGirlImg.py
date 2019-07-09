import requests
from pyquery import PyQuery as pq
import urllib
import random

class GetYongYellowImg():
    def __init__(self):
        self.BaseUrl = 'https://konachan.com/post/'

    def MaxPage(self):
        countArr = []
        Data = requests.get(self.BaseUrl)
        Html = pq(Data.content)
        pagemax = Html('#paginator .pagination a')
        for i in pagemax.items():
            if i.text().find('Next') >= 0:
                continue
            countArr.append(int(i.text()))
        return max(countArr)

    def GetMaxAndMinPageUrl(self):
        ImgUrl = []
        Data = requests.get(self.BaseUrl + '?' + 'page=' + str(random.uniform(1,self.MaxPage())) + '&' + 'tags=')
        Html = pq(Data.content)
        Doc = Html('#post-list-posts li a')
        for i in Doc.items():
           ImgUrl.append(i.attr('href'))
        return (ImgUrl[int(random.uniform(0,len(ImgUrl)))])


