# 1页
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# post
# cname:北京
# pid
# pageIndex:1
# pageSize:10

# 2页
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# post
# cname:北京
# pid
# pageIndex:1
# pageSize:10

import urllib.request
import urllib.parse


def create_request(pages):
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

    data = {
        'cname': '北京',
        'pid': '',
        'pageIndex': pages,
        'pageSize': '10'
    }

    data = urllib.parse.urlencode(data).encode('utf-8')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/113.0.0.0Safari/537.36 '
    }

    request = urllib.request.Request(url=base_url, headers=headers, data=data)

    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(content, page):
    with open('爬取内容/kfc' + str(page) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    start_page = int(input('请输入起始页:'))
    end_page = int(input('请输入结束页:'))
    for page in range(start_page, end_page + 1):
        # 请求对象定制
        request = create_request(page)
        # 获取网页源码
        content = get_content(request)
        # 下载数据
        down_load(content, page)
