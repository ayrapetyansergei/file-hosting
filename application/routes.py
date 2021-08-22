import os
import datetime
from flask import Blueprint
from flask import request, render_template, redirect, url_for
from flask import send_from_directory
from werkzeug.utils import secure_filename
from pymongo import MongoClient
import config

#MongoDB connection
client = MongoClient(host=config.DevelopConfig.MONGO_HOST,
				port=config.DevelopConfig.MONGO_PORT,
				username=config.DevelopConfig.MONGO_USERNAME,
				password=config.DevelopConfig.MONGO_PASSWORD)
db=client['metadata']

main_bp = Blueprint(
    "main_bp", __name__, template_folder="templates"
)

@main_bp.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		return redirect('/upload')
	skip_counter = db.metadata_tb.count() - 10 if db.metadata_tb.count() > 10 else 0
	return render_template('index.html', metadata=list(db.metadata_tb.find().skip(skip_counter)))

@main_bp.route('/upload', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['file']
		filename=secure_filename(f.filename)
		f.save(os.path.join(config.DevelopConfig.APP_STORAGE, filename))
		date_time = str(datetime.datetime.now())
		db.metadata_tb.insert_one({'filename':filename, 'date_time':date_time})
		return redirect(url_for('main_bp.index'))
	return render_template('upload_file.html')

@main_bp.route('/uploads/<filename>')
def save_file(filename):
	return send_from_directory(config.DevelopConfig.APP_STORAGE, filename)