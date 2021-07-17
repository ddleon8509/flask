from flask import Flask, render_template, make_response, jsonify, request, url_for

app = Flask(__name__)

PORT = 8080
HOST = '10.0.40.10'

@app.route('/')
def home():
	return render_template('home.html', title = 'Home Page')

if __name__ == '__main__':
	print('Server running in port %s'%(PORT))
	app.run(debug = True, host = HOST, port = PORT)
