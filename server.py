from flask import Flask, jsonify, request, abort
import base

app = Flask(__name__)

endpoint = '/innoLibrary/api'


@app.route(endpoint + '/check', methods=['GET'])
def check_info():
    uid = request.args.get('uid' , type=int)
    data = base.general_info(uid)
    if data:
        return jsonify(data)
    else:
        return 'Incorrect user id'


@app.route(endpoint + '/signup', methods=['POST'])
def sign_up():
    # private_key = request.args.get('private_key', type=str)
    # if not base.identify_request(private_key):
    #     return 'Wrong private key. Hacking attempt!'
    if request.json:
        data = request.json
        # private_key = data.get('private_key')
        # if not base.identify_request(private_key):
        #     return 'Wrong private key. Hacking attempt!'
    # name = request.args.get('name', type=str, default='')
    user_type = request.args.get('type', type=str, default='patron')
    return jsonify(base.create_user(**data))


@app.route(endpoint + '/sign_in', methods=['GET'])
def sign_in():
    # private_key = request.args.get('private_key', type=str)
    # if not base.identify_request(private_key):
    #     return 'Wrong private key. Hacking attempt!'
    login = request.args.get('login', type=str)
    password = request.args.get('password', type=str)
    if base.is_true_data(login, password):
        return jsonify({'Success': 'True', 'errors': 0})

    else:
        return jsonify({'Success': 'False', 'errors' : ['incorrect login or password']})


@app.route(endpoint + '/get_doc', methods=['GET'])
def get_document():
    # private_key = request.args.get('private_key', type=str)
    # if not base.identify_request(private_key):
    # return 'Wrong private key. Hacking attempt!'
    doc_id = request.args.get('doc_id', type=int)
    data = base.get_book_info(doc_id)
    if data:
        return jsonify(data)
    else:
        return 'Incorrect document id'


# @app.route(endpoint + '/take_doc', methods=['POST'])
# def take_document():
    # private_key = request.args.get('private_key', type=str)
    # if not base.identify_request(private_key):
    # return 'Wrong private key. Hacking attempt!'

@app.route(endpoint + '/get_user_info', methods=['GET'])
def get_user():
    # private_key = request.args.get('private_key', type=str)
    # if not base.identify_request(private_key):
    #     return 'Wrong private key. Hacking attempt!'
    uid = request.args.get('id', type=int)
    data = base.get_user(uid)
    if data == 'not found':
        abort(404)
    return jsonify(data)


@app.route(endpoint + '/add_document', methods=['POST'])
def add_document():

    if request.json:
        data = request.json
        # private_key = data.get('private_key')
        # if not base.identify_request(private_key):
        #     return 'Wrong private key. Hacking attempt!'
        base.add_document(**data)
        return 'document added!'
    return 'no json found'


@app.route(endpoint + 'delete_document', methods=['POST'])
def delete_document():

    if request.json:
        data = request.json
        # private_key = data.get('private_key')
        # if not base.identify_request(private_key):
        #     return 'Wrong private key. Hacking attempt!'
        return base.delete_document(data.get('doc_id'), data.get('doc_type'))
    return 'no json found'


@app.route(endpoint + 'take_document', methods=['GET'])
def take_document():
    if request.json:
        data = request.json
    #     private_key = data.get('private_key')
    # if not base.identify_request(private_key):
    #     return 'Wrong private key. Hacking attempt!'
        return base.take_document(**data)



@app.route(endpoint + 'some_method', methods=['GET'])
def some_method():
    pass
    # if request.json:
    #     data = request.json
    #     private_key = data.get('private_key')
        # if not base.identify_request(private_key):
        #     return 'Wrong private key. Hacking attempt!'


@app.route(endpoint + 'search', methods=['GET'])
def search():
    pass


if __name__ == '__main__':
    app.run(debug=True)
