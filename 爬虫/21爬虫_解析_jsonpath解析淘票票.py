import urllib.request
import jsonpath
import json


# 定制请求对象
url = ('https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1692354370965_108&jsoncallback=jsonp109&action'
       '=cityAction&n_s=new&event_submit_doGetAllRegion=true')

headers = {
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 '
    #               'Safari/537.36',
    'Cookie': 't=bc7bacbc13fd126f5da110aa20416e16; cna=haf0HMKBCiICAdpNKFudPws7; xlly_s=1; '
              'cookie2=109bf9560582e8a7d3971af636e6f890; v=0; _tb_token_=e31bd49339a0e; '
              'tfstk=dhke39iemppUEhlLbSwr04okZSyLF'
              '-LXUYa7q0muAy4HyXwraDgUN2iuP8urz4zQZeeIUVyKCX67ReerqqwylE9XhDnLp8YXlT8uH6HMYPGOJKiKv8IFrnGMhuujnYs'
              'OM8_Nq9P9om4idYg-vHC-QPWl3iEUtMmFNTWyakV3o54NQQ78jUVZeX7laWqTbrtwbDQzGIf..; l=fBMuj26nN9-7NK5aBO5BFurz'
              'a77TzIRb8sPzaNbMiIEGa1yF9FZwvNC6KOdHWdtjgTfXQetyVhmX9d3eSGapbgiMW_N-1NKD-xJ6-bpU-L5..; isg=BGpqw3hJ-vpX'
              'jXYXMPBTR5b7u9AM2-41eFFscvQjy71IJwvh3Gh_Rf9Zt1M712bN',
    'Referer': 'https://dianying.taobao.com/'
}

# 获取响应内容
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# 对内容进行切割筛选
content = content.split('(')[1].split(')')[0]

# 保存内容
with open('../爬取内容/淘票票.json', 'w', encoding='utf-8') as fp:
    fp.write(content)

# 读取解析下载文件
obj = json.load(open('../爬取内容/淘票票.json', 'r', encoding='utf-8'))

city_list = jsonpath.jsonpath(obj, '$..regionName')

print(city_list)
