# get请求
# 获取豆瓣电影的前十页的数据并且存储起来
import json
import urllib.request
import urllib.parse

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'


# 请求对象的定制
def create_request(pages):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'

    data = {
        'start': (pages - 1) * 20,
        'limit': 20
    }

    data = urllib.parse.urlencode(data)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/113.0.0.0Safari/537.36 '
    }

    request = urllib.request.Request(url=base_url + data, headers=headers)

    return request


# 获取响应的数据
def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


# 下载数据
def down_load(page1, obj):
    with open('../爬取内容/douban' + str(page1) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(obj)


# 程序的入口
if __name__ == '__main__':
    start_page = int(input('请输入起始的页码:'))
    end_page = int(input('请输入结束的页码:'))

    for page in range(start_page, end_page + 1):
        # 每一页都有自己请求对象的定制
        url = create_request(page)
        content = get_content(url)
        down_load(page, content)
