# -*- coding: utf-8 -*-

# Python
from os import getenv


class Config:
    SECRET_KEY = getenv('SECRET_KEY') or 'hard to guess string'
    APP_PORT = int(getenv('APP_PORT'))
    DEBUG = eval(getenv('DEBUG').title())
    SENTRY_DSN = getenv('SENTRY_DSN')
    MONGODB_HOST = getenv('MONGODB_URI')
    MONGODB_HOST_TEST = getenv('MONGODB_URI_TEST')
    REDIS_HOST = getenv('REDIS_HOST')
    AMQP_HOST = getenv('AMQP_URI')

    def __init__(self):
        self.secret_key = self.SECRET_KEY
        self.app_port = self.APP_PORT
        self.debug = self.DEBUG
        self.sentry_dsn = self.SENTRY_DSN
        self.mongodb_host = self.MONGODB_HOST
        self.redis_host = self.REDIS_HOST
        self.amqp_host = self.AMQP_HOST

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True


class TestingConfig(Config):
    FLASK_ENV = 'testing'
    TESTING = True
    MONGODB_HOST = getenv('MONGODB_URI_TEST')


class ProductionConfig(Config):
    DEBUG = False


class HerokuConfig(ProductionConfig):
    SSL_REDIRECT = True if getenv('DYNO') else False


class DockerConfig(ProductionConfig):
    pass


class UnixConfig(ProductionConfig):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'heroku': HerokuConfig,
    'docker': DockerConfig,
    'unix': UnixConfig,
    'default': DevelopmentConfig
}
