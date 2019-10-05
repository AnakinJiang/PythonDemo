# Author: AnakinJiang
# Email: jiangjinpeng319 AT gmail.com
# Time: 2019-09-30 13:48:18
# Descripttion： 
import requests

ip = 'http://116.62.246.133:10010/'


def get_test():
    url = ip
    resp = requests.get(url)
    print(resp.url)


def file_test():
    files = {'images': ["Lena.jpg", open(
        "data/Lena.jpg", 'rb'), "image/jpeg"]}
    url = ip + 'file'
    resp = requests.post(url, files=files)
    print(resp.content)


def json_test():
    data = {
        'test': "one"
    }
    url = ip + 'json'
    resp = requests.post(url, json=data)
    print(resp.content)


def multi_test():
    arg = {
        'test1': 1,
        'test2': 2
    }
    filename = 'data/sample.txt'
    files = {'images': ['sample.txt', open(filename, 'rb'), "text/plain"]}
    url = ip + 'multi'
    resp = requests.post(url, data=arg, files=files)
    content = resp.content.decode('utf-8')
    print(content)


if __name__ == "__main__":
    # get_test()
    # # json_test()
    # file_test()
    multi_test()
