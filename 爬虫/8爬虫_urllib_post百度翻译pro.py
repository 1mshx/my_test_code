import json
import urllib.request
import urllib.parse


url = 'https://fanyi.baidu.com/sug'

headers = {
    # 'Cookie':'BIDUPSID=E98B5FC90B234DF3CE02307E6B086E5A; PSTM=1679145127; BAIDUID=85009BF39C4EB5011C4A3F3ED64233F2:FG=1; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID_BFESS=85009BF39C4EB5011C4A3F3ED64233F2:FG=1; ZFY=zCs5GyKipLFUqP237:Ac8mfjlbDQNVj0gvLinNltTth0:C; H_PS_PSSID=38516_36553_38687_38794_38903_38793_38844_38576_38820_38836_38637_26350; BA_HECTOR=0h0h010lagalag202g8k2l0o1i97fgq1o; PSINO=6; delPer=0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BCLID=10555204893802414634; BCLID_BFESS=10555204893802414634; BDSFRCVID=4f8OJexroG0ZmSbfuztwuOnA5FweG7bTDYrEOwXPsp3LGJLVFakFEG0Pts1-dEu-S2OOogKKLmOTHpKF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BDSFRCVID_BFESS=4f8OJexroG0ZmSbfuztwuOnA5FweG7bTDYrEOwXPsp3LGJLVFakFEG0Pts1-dEu-S2OOogKKLmOTHpKF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRAOoC_-tDvDqTrP-trf5DCShUFstPKOB2Q-XPoO3KJADfOPbRo05b-0XUTCtx5f5mkf3fbgy4op8P3y0bb2DUA1y4vp0toW3eTxoUJ2-KDVeh5Gqq-KXU4ebPRiWPr9QgbjahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHjL-jjOy3f; H_BDCLCKID_SF_BFESS=tRAOoC_-tDvDqTrP-trf5DCShUFstPKOB2Q-XPoO3KJADfOPbRo05b-0XUTCtx5f5mkf3fbgy4op8P3y0bb2DUA1y4vp0toW3eTxoUJ2-KDVeh5Gqq-KXU4ebPRiWPr9QgbjahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHjL-jjOy3f; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1686464216,1686580190,1687142129,1687404076; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1687418138; ab_sr=1.0.1_ZmEyZDRjYmQ0MDI5NzEzMTBmNmM4NDQ2NWQ3Y2RiNzMyYmRmZjQ1ZTBkOWVkZThlMjVmODc4ZjIwY2VmMWRiZDJlMDQ1NzliMzg0NWMwNDM5ZjA5NzlkZmE4ZjIzOWVhMTEwZGI2ZmUxYjk5ZTZlZDlhM2Q5ZjUxZGM3YmJjNzdjYWUyZjA4MWIyNjJkYmViMDZjNzBhYzQxZGNjM2U5Zg==',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

data = {
    'kw': 'love'}
url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers = {
    'Cookie':
        'BIDUPSID=E98B5FC90B234DF3CE02307E6B086E5A; PSTM=1679145127; BAIDUID=85009BF39C4EB5011C4A3F3ED64233F2:FG=1; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID_BFESS=85009BF39C4EB5011C4A3F3ED64233F2:FG=1; ZFY=zCs5GyKipLFUqP237:Ac8mfjlbDQNVj0gvLinNltTth0:C; H_PS_PSSID=38516_36553_38687_38794_38903_38793_38844_38576_38820_38836_38637_26350; BA_HECTOR=0h0h010lagalag202g8k2l0o1i97fgq1o; PSINO=6; delPer=0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BCLID=10555204893802414634; BCLID_BFESS=10555204893802414634; BDSFRCVID=4f8OJexroG0ZmSbfuztwuOnA5FweG7bTDYrEOwXPsp3LGJLVFakFEG0Pts1-dEu-S2OOogKKLmOTHpKF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BDSFRCVID_BFESS=4f8OJexroG0ZmSbfuztwuOnA5FweG7bTDYrEOwXPsp3LGJLVFakFEG0Pts1-dEu-S2OOogKKLmOTHpKF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRAOoC_-tDvDqTrP-trf5DCShUFstPKOB2Q-XPoO3KJADfOPbRo05b-0XUTCtx5f5mkf3fbgy4op8P3y0bb2DUA1y4vp0toW3eTxoUJ2-KDVeh5Gqq-KXU4ebPRiWPr9QgbjahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHjL-jjOy3f; H_BDCLCKID_SF_BFESS=tRAOoC_-tDvDqTrP-trf5DCShUFstPKOB2Q-XPoO3KJADfOPbRo05b-0XUTCtx5f5mkf3fbgy4op8P3y0bb2DUA1y4vp0toW3eTxoUJ2-KDVeh5Gqq-KXU4ebPRiWPr9QgbjahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHjL-jjOy3f; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1686464216,1686580190,1687142129,1687404076; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1687418138; ab_sr=1.0.1_ZmEyZDRjYmQ0MDI5NzEzMTBmNmM4NDQ2NWQ3Y2RiNzMyYmRmZjQ1ZTBkOWVkZThlMjVmODc4ZjIwY2VmMWRiZDJlMDQ1NzliMzg0NWMwNDM5ZjA5NzlkZmE4ZjIzOWVhMTEwZGI2ZmUxYjk5ZTZlZDlhM2Q5ZjUxZGM3YmJjNzdjYWUyZjA4MWIyNjJkYmViMDZjNzBhYzQxZGNjM2U5Zg==',
    'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Acs-Token': '1687418138947_1687418150752_f7uakEw/2iCyPxwZLyo87nMZA/1qKqw89rPbePXVphXeFoNufYGn9+VAMK4rP3vpIOEY5u0yvn6j1+Yim2GeCjgN72zFNYMB3GrXjG3LQo7RI8tuUVR22hmab5U48p6GmcI6oYAvuxmwLUJfI4lOlx2JyGyBZN/lNvamkPB6OBfvhsBNylH2w6mZlp55dRnGZcHPzaBwrQzooauxLdGW8DpwLuQHdwrw5C1KCpNvL7U9K3WMkyVRm3UHUCNsEjgZRJ2ksVvD+6oty1cjlcmKmQXJTAh06d7QEQ4GG1KSzN/l7UBSX7IvrBvyhDYeyfByCTreUdlLNLMMEpRde7N3kdetwuJxkzupbC5O4dh+dUiW4jsJlkxq16qj8FF/H7JuIHeupxayC/mZo79arPrFRsaFBwxs4xXbFjEqi+c+Mr5nO5YGLnPW7L9uVb4ZexwafwwqR0j0MvR/He2k9cEOjArGBjgxgPuZDtGhT8kaj3ToJDOS+0JB0G+ogedsNJyF',
    'Connection': 'keep-alive',
    'Content-Length': '152',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'fanyi.baidu.com',
    'Origin': 'Https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh',
    'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

data = {
    'from:': 'en',
    'to:': 'zh',
    'query:': 'love',
    'transtype:': 'enter',
    'simple_means_flag:': '3',
    'sign:': '198772.518981',
    'token:': '1544b51f55c73f3656503f4e8ef79d06',
    'domain:': 'common',
}

# post请求的参数，必须进行编码，并且要调用encode方法
data = urllib.parse.urlencode(data).encode('utf-8')

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers, data=data)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应的内容
content = response.read().decode('utf-8')
obj = json.loads(content)

print(content)
print(obj)
