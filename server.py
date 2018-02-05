from flask import Flask, jsonify, request
import base
app = Flask(__name__)

endpoint = '/innoLibrary/api'


@app.route(endpoint + '/signup', methods=['GET'])
def sign_up():
    private_key = request.args.get('private_key', type=str)
    if not base.identify_request(private_key):
        return 'Wrong private key. Hacking attempt!'
    login = request.args.get('login', type=str)
    password = request.args.get('pass', type=str)
    # name = request.args.get('name', type=str, default='')
    user_type = request.args.get('type', type=str, default='patron')
    return base.create_user(login, password, user_type)


if __name__ == '__main__':
    app.run(debug=True)