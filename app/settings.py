# -*- coding: utf-8 -*-
# 配置文件
import os


class Config(object):

    DEBUG = False
    TESTING = False


    # mail settings
    MAIL_SERVER = 'smtp.126.com'
    MAIL_PORT = 25

    # mail authentication
    MAIL_USERNAME = 'bababa'
    MAIL_PASSWORD = 'bababa'


class DevelopmentConfig(Config):

    ENV = 'development'
    DEBUG = True
    SERVER_IP = '127.0.0.1'
    SERVER_PORT = 5555
    # session
    CSRF_ENABLED = True
    SECRET_KEY = "asgSfsf3Xd8ffy]fw8vfd0zbvssqwertsd4sdwe"

    # database
    SQLALCHEMY_DATABASE_URI = "mysql://root:$@localhost:3306/blog"
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):

    ENV = 'testing'
    TESTING = True


class StagingConfig(Config):

    ENV = 'staging'
    TESTING = True


class ProductionConfig(Config):

    ENV = 'production'
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
