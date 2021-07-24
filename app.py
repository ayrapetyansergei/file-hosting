import os
import datetime
from flask import Flask, request, render_template, redirect, url_for
from flask import send_from_directory
#from flask_pymongo import PyMongo
from pymongo import MongoClient
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['DEBUG'] = True
#app.config["MONGO_URI"] = "mongodb://root:example@localhost:27017/metadata"
#mongodb_client = PyMongo(app)
#db = mongodb_client.db
metadata = list()
#db.metadata.insert_one({'sdc':123})
client = MongoClient(host='mongodb',
					 port=27017,
					 username='root',
					 password='password')
db=client['metadata']
#collection = db['metadata_tb']
print(dir(db.metadata_tb))#.insert_one({'1':1, '2':2})
print(db.metadata_tb)#.insert_one({'1':1, '2':2})
# db['images'].insert_one({'datetime':str(datetime.datetime.now())})# for _ in range(5)]

# print(db) 
# print(db['images'].find({}))# for _ in range(5)]



@app.route('/', methods=['GET', 'POST'])
def index(filename=None, date_time=None):
	global metadata
	if request.method == 'POST':
		filename = request.args.get('filename', None)
		date_time = request.args.get('date_time', None)
		if not(filename is None) and not(date_time is None):
			#db.metadata.insert_one({'filename':filename, 'date_time':date_time})
			metadata.append({'filename':filename, 'date_time':date_time})
		return redirect('/upload')
	#print(db.metadata.find())
	#metadata = [m for m in db.metadata.find({})]
	#print(metadata)
	db.metadata_tb.insert_one({'datetime':str(datetime.datetime.now())})
	return render_template('index.html', metadata=metadata)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['file']
		filename=secure_filename(f.filename)
		f.save(os.path.join(os.getenv('APP_STORAGE'), filename))
		date_time = str(datetime.datetime.now())
		# db.metadata.insert_one({'filename':filename, 'date_time':date_time})
		return redirect(url_for('index', filename=filename, date_time=date_time))
	else:
		return render_template('upload_file.html')

@app.route('/uploads/<filename>')
def save_file(filename):
	return send_from_directory(os.getenv('APP_STORAGE'), filename)


if __name__ == '__main__':
	app.run(host="0.0.0.0", port=os.getenv('APP_PORT'))
