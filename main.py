# from flask import Flask, jsonify, request

# app = Flask(__name__)


# @app.route('/hello', methods=['GET'])
# def helloworld():
# 	if(request.method == 'GET'):
# 		data = {"data": "HELLO KENDU"}
# 		return jsonify(data)


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=9001)

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Healthy!", 200

@app.route('/hello', methods=['GET'])
def helloworld():
	if(request.method == 'GET'):
		data = {"data": "HELLO KENDU"}
		return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001)
