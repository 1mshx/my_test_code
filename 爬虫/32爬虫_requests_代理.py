import requests
from fake_useragent import UserAgent

url = 'https://www.jd.com'
# url = 'http://www.baidu.com/s?'

UserAgent = UserAgent().random
print(UserAgent)

headers = {
    'User-Agent': UserAgent,
    # 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
    #               'Chrome/115.0.0.0 Mobile Safari/537.36 Edg/115.0.1901.188'

}

data = {
    'wd': 'ip'
}

# tunnel = 'q891.kdltps.com:15818'
# username = 't10225995877362'
# password = 'mjo74i87'
# proxies = {
#     "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel},
#     "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel}
# }
#
response = requests.get(url=url, headers=headers)

content = response.content
print(content)
print(response.status_code)
