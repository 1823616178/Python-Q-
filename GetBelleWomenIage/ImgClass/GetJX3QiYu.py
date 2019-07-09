import requests
import random
from pyquery import PyQuery as py
class GetJX3QiYu:
    def __init__(self):
        self.baseUrl = "https://jx3.derzh.com/serendipity/?m=1&test=1&r=03AOLTBLSv3sYv_lrsNQSkB77c2G22HViS7G6_5F_hMPDxwzLPXBcsEYtDAX4pRS09kI-21xEsiwLQpWF5oVGUpAVCoCRBWZfzTiMyZ0CYC3tCtXol0n6OJJzgufvE-TLadKItuA6hUzexfyhLyFLz7uvdAYPyXXz-HTBRVUHxKNDJ3XkbHgZZNLbQ6YEohc4OxhVJLcpPyoL1iKScANLIm09uC1t_V_2hl8Cdb9USIuF-2Yu5AeuaHZExhq3RPIamHxZFDlRi1d1b2vtL2IpcTl0qhrccw7G2YuF_Xcy_E-5W1Zyds3rL5inn59MyCqnGzytyHKKOmFj9&R=%E5%8F%8C%E7%BA%BF%E4%B8%80%E5%8C%BA&S=%E5%A4%A9%E9%B9%85%E5%9D%AA&t=&s=&n=&csrf="
        self.GetQiYuData()
    def GetQiYuData(self):
        data = requests.post(self.baseUrl)
        print(data.json())

GetJX3QiYu()