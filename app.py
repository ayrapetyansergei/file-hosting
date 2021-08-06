import os
import datetime
from flask import Flask, request, render_template, redirect, url_for
from flask import send_from_directory
from pymongo import MongoClient
from werkzeug.utils import secure_filename
import config

app = Flask(__name__)

#Add config parameters
app.config.from_object('config.DevelopConfig')

#MongoDB connection
client = MongoClient(host=config.DevelopConfig.MONGO_HOST,
					 port=int(config.DevelopConfig.MONGO_PORT),
					 username=config.DevelopConfig.MONGO_USERNAME,
					 password=config.DevelopConfig.MONGO_PASSWORD)
db=client['metadata']

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		return redirect('/upload')
	return render_template('index.html', metadata=list(db.metadata_tb.find({})))

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['file']
		filename=secure_filename(f.filename)
		f.save(os.path.join(os.getenv('APP_STORAGE'), filename))
		date_time = str(datetime.datetime.now())
		db.metadata_tb.insert_one({'filename':filename, 'date_time':date_time})
		return redirect(url_for('index'))
	return render_template('upload_file.html')

@app.route('/uploads/<filename>')
def save_file(filename):
	return send_from_directory(os.getenv('APP_STORAGE'), filename)


if __name__ == '__main__':
	app.run(host="0.0.0.0", port=config.DevelopConfig.APP_PORT)
