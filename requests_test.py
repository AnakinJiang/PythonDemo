'''
@Author: AnakinJiang
@Email: jiangjinpeng319 AT gmail.com
@Descripttion: requests测试demo
@Date: 2019-08-27 15:37:14
@LastEditors: AnakinJiang
@LastEditTime: 2019-08-27 16:55:06
'''
import requests

def get_test():
    url1 = 'https://www.douban.com/'
    r1 = requests.get(url1)
    print(r1.status_code)
    print(r1.text)
    print(r1.content)

    url2 = 'https://www.douban.com/search'
    params = {'q': 'python', 'cat': '1001'}
    r2 = requests.get(url2,params=params)
    print(r2.url)
    print(r2.encoding)
    print(type(r2.content))
    print(r2.headers)



get_test()

