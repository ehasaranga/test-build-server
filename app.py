from flask import Flask, Response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
	output = "Hello World"

	return Response(output,status=200,mimetype='html')

app.run()

