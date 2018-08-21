# -*- coding:utf-8 -*-
# 初始化文件
import os
import sys
import logging

# TODO 中间件的实现
from werkzeug.wsgi import DispatcherMiddleware

from werkzeug.serving import run_simple
from app.application import create_app
from app.settings import config

curr_config  = config['development']
app = create_app(curr_config)



if __name__ == '__main__':
    run_simple(curr_config.SERVER_IP, curr_config.SERVER_PORT, app, use_reloader = curr_config.DEBUG,  use_debugger = curr_config.DEBUG)




