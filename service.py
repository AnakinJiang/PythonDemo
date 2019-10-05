# Author: AnakinJiang
# Email: jiangjinpeng319 AT gmail.com
# Time: 2019-09-29 14:59:10
# Descripttion： 
# coding:utf-8
# tornado服务
# 端口等基础参数配置

import os
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
from tornado.options import options, define
from handler import GetHandler, JsonHandler, FileHandler, MultiHandler

define("port", default=10010, type=int, help="run server on the given port.")
HANDLERS = [
    (r"/", GetHandler),
    (r"/json", JsonHandler),
    (r"/file", FileHandler),
    (r"/multi", MultiHandler),
    (r"/files/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(os.path.dirname(__file__), "files")})
]

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=HANDLERS, static_path=os.path.join(os.path.dirname(__file__), "files"),
                                  debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
