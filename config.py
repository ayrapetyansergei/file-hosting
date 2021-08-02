import os 
from dotenv import load_dotenv


base_dir = os.getcwd()
load_dotenv(os.path.join(base_dir, '.env'))


class BaseConfig:
	#App config
	APP_PORT = os.environ.get('APP_PORT')

	#MongoDB config
	MONGO_HOST = os.environ.get('MONGO_HOST')
	MONGO_PORT = os.environ.get('MONGO_PORT')
	MONGO_USERNAME = os.environ.get('MONGO_USERNAME')
	MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')

class DevelopConfig(BaseConfig):
	APP_DEBUG = True

class ProductionConfig(BaseConfig):
	APP_DEBUG = False