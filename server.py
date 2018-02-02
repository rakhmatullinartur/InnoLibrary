from flask import Flask, jsonify
import base
app = Flask(__name__)

endpoint = '/innoLibrary/api'


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route(endpoint, methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route(endpoint + '/create_user', methods=['GET'])
def check_login():
    pass

if __name__ == '__main__':
    app.run(debug=True)