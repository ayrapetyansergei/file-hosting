from flask import Flask
from pymongo import MongoClient
import config


def init_app():
	app = Flask(__name__, instance_relative_config=False)

	#Add config parameters
	app.config.from_object('config.DevelopConfig')

	with app.app_context():
        # Include our Routes
		from . import routes
		app.register_blueprint(routes.main_bp)

		return app