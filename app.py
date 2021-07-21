import os
import datetime
from flask import Flask, request, render_template, redirect, url_for
from flask import send_from_directory
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['DEBUG'] = True
metadata = list()

@app.route('/', methods=['GET', 'POST'])
def index(filename=None, date_time=None):
	global metadata
	if request.method == 'POST':
		filename = request.args.get('filename', None)
		date_time = request.args.get('date_time', None)
		if not(filename is None) and not(date_time is None):
			metadata.append({'filename':filename, 'date_time':date_time})
		return redirect('/upload')
	return render_template('index.html', metadata=metadata)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['file']
		filename=secure_filename(f.filename)
		f.save(os.path.join(os.getenv('APP_STORAGE'), filename))
		return redirect(url_for('index', filename=filename, date_time=str(datetime.datetime.now())))
	else:
		return render_template('upload_file.html')

@app.route('/uploads/<filename>')
def save_file(filename):
	return send_from_directory(os.getenv('APP_STORAGE'), filename)


if __name__ == '__main__':
	app.run(host="0.0.0.0", port=os.getenv('APP_PORT'))
