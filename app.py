import os
from flask import Flask, request, render_template, redirect, url_for
from flask import send_from_directory
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
	return 'First commit'

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['file']
		filename=secure_filename(f.filename)
		f.save(os.path.join('/home/serj/Desktop/file-hosting/storage', filename))
		return redirect(url_for('save_file', filename=filename))
	else:
		return render_template('upload_file.html')

@app.route('/uploads/<filename>')
def save_file(filename):
	return send_from_directory('/home/serj/Desktop/file-hosting/storage', filename)


if __name__ == '__main__':
	app.run()