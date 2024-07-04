import urllib.request

# 下载网页
url_page = 'http://www.baidu.com'

# url代表下载的路径 filename文件的名字
# 在python中 可以写变量的名字，也可以直接写值
urllib.request.urlretrieve(url_page, '../爬取内容/baidu.html')

# 下载图片
url_img = 'https://img0.baidu.com/it/u=2191968071,4247550473&fm=253&fmt=auto&app=138&f=JPEG?w=889&h=500'

urllib.request.urlretrieve(url_img, '../爬取内容/jks.jpg')

# 下载视频
url_video = 'https://video.pearvideo.com/mp4/short/20221215/cont-1775975-15946992-hd.mp4'

urllib.request.urlretrieve(url_video, '../爬取内容/1.mp4')


