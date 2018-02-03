from flask import Flask, jsonify, request
import base

app = Flask(__name__)

endpoint = '/innoLibrary/api'


@app.route(endpoint + '/signup', methods=['POST'])
def sign_up():
    private_key = request.args.get('private_key', type=str)
    if not base.identify_request(private_key):
        return 'Wrong private key. Hacking attempt!'
    login = request.args.get('login', type=str)
    password = request.args.get('pass', type=str)
    # name = request.args.get('name', type=str, default='')
    user_type = request.args.get('type', type=str, default='patron')
    return base.create_user(login, password, user_type)


@app.route(endpoint + '/sign_in', methods=['POST'])
def sign_in():
    # private_key = request.args.get('private_key', type=str)
    # if not base.identify_request(private_key):
    #     return 'Wrong private key. Hacking attempt!'
    login = request.args.get('login', type=str)
    password = request.args.get('password', type=str)
    if base.is_true_data(login, password):
        return 'Zaebis , you woshli v account'
    else:
        return 'login or password ne verniy blya'


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


if __name__ == '__main__':
    app.run(debug=True)
