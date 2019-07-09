import random
import requests
from pyquery import PyQuery as py


class Gocar():
    def __init__(self):
        self.listAdd = []
        self.baseUrlImg = "http://m.teemm.com"
        self.baseUrl = "http://m.teemm.com/guonei/list_1_"
        self.GetCarImg()

    def GetCarImg(self):
        listImgurl = []
        Data = requests.get(self.baseUrl + '1.html').text
        Html = py(Data)
        Doc = Html('.box .newspage.cl ul li span strong')
        for i in Doc.items():
            self.listAdd.append(i.text())
        Data2 = requests.get(self.baseUrl + str(int(random.uniform(0, int(self.listAdd[0])))) + '.html').text
        Html2 = py(Data2)
        Doc2 = Html2('.list_btm ul li a')
        for i in Doc2.items():
            listImgurl.append(i.attr('href'))
        EnumUrl = self.baseUrlImg + listImgurl[int(random.uniform(0, int(len(listImgurl))))]
        Data3 = requests.get(EnumUrl).content
        HTML3 = py(Data3)
        Doc3 = HTML3('.content_page ul li a')
        ImgPage = ""
        for i in Doc3.items():
            if i.text().find('共') >= 0:
                ImgPage = i.text()[1]

        requests.get()



Gocar()
