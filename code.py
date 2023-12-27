from flask import Flask, request, jsonify, send_from_directory
import json
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    for filename in os.listdir('.'):
        if filename.endswith('.html'):
            return app.send_static_file(filename)
    return 'No HTML files found in this directory', 404

@app.route('/<path:path>', methods=['GET'])
def get_html(path):
    if path.endswith('.html'):
        return send_from_directory('.', path)
    return 'Not an HTML file', 400

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    print(f'Credenciais recebidas: {username}, {password}')
    return jsonify({'message': 'Credenciais recebidas com sucesso!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
