# 使用的场景:数据采集的时候，需要绕过登录 然后进入到某个页面

import urllib.request

url = 'https://mobile.qzone.qq.com/infocenter?sid=&g_f=2000000209&srctype=10&stat=&qqmailstat=&ticket='

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/115.0.0.0 Mobile Safari/537.36 Edg/115.0.1901.188',
    'Cookie': 'pgv_pvid=1062371088; pac_uid=0_72a5dfc4eef3d; iip=0; RK=FAfloWuUt7; '
              'ptcz=85e771b78cfb1797092cb7e1be3e4d8b77151d11b9c2cbf2203f798e7b338a2a; '
              'fqm_pvqid=0f2a8a94-7fff-42e7-9371-dc98c18da553; eas_sid=R19617S0P6B6B6s4F4L6D5Z9d0; '
              'QZ_FE_WEBP_SUPPORT=1; tvfe_boss_uuid=8c5dd3fd17420bc0; __Q_w_s_hat_seed=1; it_c=1698515884; '
              'qq_domain_video_guid_verify=2328b14e2da2f1c4; uin=o2801417588; skey=@YyCcugFrK; '
              '_qpsvr_localtk=0.8672140705928806; p_uin=o2801417588; Loading=Yes; pgv_info=ssid=s4184619946; '
              'pt4_token=qzs-prtlDB*OaraRchV7Z9YQqeDhHFMZrgD0XbxMJqE_; '
              'p_skey=8G0IzUf81sqx7u2Ki9t5daqVnuppK79OAXMGdpFYntc_; cpu_performance_v8=8',
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)

with open('../爬取内容/QQ.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
