from flask import Flask


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
	return 'First commit'

if __name__ == '__main__':
	app.run()