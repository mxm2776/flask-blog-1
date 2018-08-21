# -*- coding:utf-8 -*-

from wsgi import curr_config

bind = "{}:{}".format(curr_config.SERVER_IP, curr_config.SERVER_PORT)
backlog = 1024
workers = 2
worker_class = 'gevent'
worker_connections = 1000
max_requests = 10000
timeout = 20
daemon = False


