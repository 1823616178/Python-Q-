import random
import requests
from collections import OrderedDict
from urllib3 import encode_multipart_formdata

a = 1
b = 2
c = 24
baseUrl = "http://www.songdujingdian.com/vote/sing"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    "X-Forwarded-For": "118." + str(c) + "." + str(a) + "." + str(b)
}
params = OrderedDict([("id", (None, '73842')),
                      ("name", (None, '我在一颗石榴里看见我的祖国')),
                      ('__hash__', (None, '4c917290fba27247cee2fef2cb3e36b6_9d132f869249482696cbbd184b669794',)),
                      ('type', (None, '6')),
                      ('settoken', (None, ''))])
for i in range(1):
    res = requests.post(baseUrl, headers=headers, files=params)
    b += 1
    if b > 200:
        a += 1
        b = 1
    if a > 200:
        c += 1
        a = 1
        b = 1
    print(res)
