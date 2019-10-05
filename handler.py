# Author: AnakinJiang
# Email: jiangjinpeng319 AT gmail.com
# Time: 2019-09-29 15:01:03
# Descripttion： 

import json
from abc import ABC
import os
from tornado.web import RequestHandler
import numpy as np

root = 'files/'


def save(filename, data):
    if not os.path.exists(root):
        print("创建目录" + root + "成功")
        os.makedirs(root)

    path = root + filename
    # 图片以字节形式
    with open(path, 'wb') as file_object:
        file_object.write(data)


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


class GetHandler(RequestHandler, ABC):
    def get(self):
        self.write('hello world!!!')
        self.finish()


class JsonHandler(RequestHandler, ABC):
    def post(self):
        res = {
            'code': 'success'
        }
        jsons = json.dumps(res, cls=NumpyEncoder)
        self.set_header('Content-Type', 'application/json; charset=UTF-8')
        self.write(jsons)
        self.finish()


class FileHandler(RequestHandler, ABC):

    def post(self):
        files = self.request.files
        data = files['images'][0]["body"]
        filename = files['images'][0]["filename"]
        save(filename, data)
        self.finish()


class MultiHandler(RequestHandler, ABC):

    def post(self):
        files = self.request.files
        data = files['images'][0]["body"]
        filename = files['images'][0]["filename"]
        test = self.get_body_arguments('test')
        print(test)
        save(filename, data)
        self.finish()
