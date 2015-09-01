import os

# default config
class BaseConfig(object):
	DEBUG = False
	app.secret_key = "hari-om-tat-sat"
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False