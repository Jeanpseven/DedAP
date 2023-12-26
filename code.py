from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return app.send_static_file('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    print(f'Credenciais recebidas: {username}, {password}')
    return jsonify({'message': 'Credenciais recebidas com sucesso!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
