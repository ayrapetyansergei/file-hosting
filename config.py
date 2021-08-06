import os 
from dotenv import load_dotenv


base_dir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(base_dir, '.env'))


class BaseConfig:
	#App config
	APP_PORT = os.environ.get('APP_PORT', 8001)
	APP_STORAGE = os.environ.get('APP_STORAGE')

	#MongoDB config
	MONGO_HOST = os.environ.get('MONGO_HOST', 'mongodb')
	MONGO_PORT = os.environ.get('MONGO_PORT', 27017)
	MONGO_USERNAME = os.environ.get('MONGO_USERNAME', 'root')
	MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', 'password')

class DevelopConfig(BaseConfig):
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = False