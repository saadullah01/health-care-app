'''
 This file will define and execute the main flow of our
 app. It will include all modules that will be created separately
 and will use their functionalities accordingly.
'''

from flask import Flask, request
from flask_restful import Resource, Api

from device_module import device_api as d
from chat_module import chat_api as c

app = Flask(__name__)
api = Api(app)

class device_api(Resource):
    def get(self):
        data = request.json
        response = d.get_reading(data)
        return response

    def put(self):
        data = request.json
        response = d.add_reading(data)
        return response

class chat_api(Resource):
    def get(self):
        data = request.json
        response = c.get_reading(data)
        return response

    def put(self):
        data = request.json
        response = c.add_reading(data)
        return response

# Routes
api.add_resource(device_api, '/device')
api.add_resource(chat_api, '/chat')

# Main Page
@app.route('/')
def index():
    return "<h1>Welcome to our Health Care App!!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
