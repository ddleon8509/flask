 
from flask import Flask

app = Flask(__name__)

PORT = 8080
HOST = '10.0.40.10'

@app.route('/')
def home():
	return 'Home Page 200 OK'

if __name__ == '__main__':
	print('Server running in port %s'%(PORT))
	app.run(host = HOST, port = PORT)
