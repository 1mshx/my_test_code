import urllib.request
from lxml import etree

# （1）请求对象的定制
# （2）获取网页源 码
# （3）下载

# 需求 下载前十页图片
# https://sc.chinaz.com/tupian/dongman.html
# https://sc.chinaz.com/tupian/dongman_2.html
# https://sc.chinaz.com/tupian/dongman_3.html

def create_request(page):
    '''
    定制页面的请求对象
    :param page: 页码
    :return: 定制的请求对象
    '''
    if page == 1:
        url = 'https://sc.chinaz.com/tupian/dongman.html'
    else:
        url = f'https://sc.chinaz.com/tupian/dongman_{page}.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 '
                      'Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    '''
    获取网页源码
    :param request: 请求对象
    :return: 网页源码
    '''
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(content):
    '''
    下载图片
    :param content: 网页源码
    :return:
    '''
    tree = etree.HTML(content)
    name_list = tree.xpath('//div[@data-waterfall="true"]/div/img/@alt')
    picture_list = tree.xpath('//div[@data-waterfall="true"]/div/img/@data-original')
    # 一般设计图片的网站都会进行懒加载
    # 下载图片
    for i in range(len(name_list)):
        url = 'https:' + picture_list[i]
        filename = f'../爬取内容/站长/{name_list[i]}.jpg'
        print(url)
        print(filename)
        urllib.request.urlretrieve(url=f'https:{picture_list[i]}', filename=f'../爬取内容/站长/{name_list[i]}.jpg')


if __name__ == '__main__':
    start_page = int(input('请输入起始页码:'))
    end_page = int(input('请输入结束页码:'))

    for page in range(start_page, end_page + 1):
        # (1)请求对象的定制
        request = create_request(page)
        # (2)获取网页源码
        content = get_content(request)
        # (3)下载
        down_load(content)
