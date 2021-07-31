import os 


class BaseConfig:
	#App config
	BASE_DIR = os.getcwd()
	APP_PORT = os.environ.get('APP_PORT', 8001)

	#MongoDB config
	MONGO_HOST = os.environ.get('MONGO_HOST', 'mongodb')
	MONGO_PORT = os.environ.get('MONGO_PORT', 27017)
	MONGO_USERNAME = os.environ.get('MONGO_USERNAME', 'root')
	MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', 'password')

class DevelopConfig(BaseConfig):
	APP_DEBUG = True

class ProductionConfig(BaseConfig):
	APP_DEBUG = False