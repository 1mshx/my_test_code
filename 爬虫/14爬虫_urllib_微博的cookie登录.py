# 使用的场景:数据采集的时候，需要绕过登录 然后进入到某个页面

import urllib.request

url = 'https://weibo.com/u/page/follow/7848081846'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 '
                  'Safari/537.36',
    'Cookie': 'SINAGLOBAL=9214440961648.527.1687614031638; '
              'ULV=1690943635584:2:1:1:2907061199030.685.1690943635582:1687614031642; '
              'XSRF-TOKEN=3x1R3ibk3bDP1Bv8lHI0ssd5; '
              'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWTxqC15cbhDEecIVdTJLwr5JpX5KMhUgL'
              '.FoMRShn71h2RShq2dJLoIEnLxKqL1KqL1hMLxKqL1KnL12-LxKBLBonL122LxKMLB.BL1K2Eeh5E; ALF=1693619168; '
              'SSOLoginState=1691027169; '
              'SCF=AjWi3iwCLoI3ggjuvtvulTvKkfJHOD3AGgNPHhMX1xDwSmjl8uRyF5r6Z6reVjej1rzOgQKC5tVsL66JMv0hryo.; '
              'SUB=_2A25Jz3axDeRhGeFG71oR-C_EzzqIHXVqve95rDV8PUNbmtANLWfTkW9NeX2XX6HXje31NjPCmW4hMaVOxS00dkLZ; '
              'WBPSESS=cUL_kn_lmoA4A4AGAONHaB9B4rI9y8d8fIZwXohBGyF_wM6WGkBYMbZqgNYIVJAbpN0_bvOGiEmJD8GnoiaV3DQYTKoWHuo37eQ4eNOZiEmhxpXFZNef1suw9veekLDEpfOQQndSzEBi9jiO9L-Obw==',
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)

with open('../爬取内容/微博.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
