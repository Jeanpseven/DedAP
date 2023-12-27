from flask import Flask, render_template, request, jsonify
import socket

app = Flask(__name__)

def get_network_interfaces():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    netmask = get_netmask(ip_address)
    return [{"hostname": hostname, "ip_address": ip_address, "netmask": netmask}]

def get_netmask(ip_address):
    # Este é um exemplo simples de como obter a máscara de rede. 
    # Você pode precisar implementar sua própria lógica para obter a máscara de rede correta.
    return "255.255.255.0"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        net = request.form['net']
        channel = request.form['channel']
        interfaces = get_network_interfaces()
        return render_template('result.html', net=net, channel=channel, interfaces=interfaces)
    return render_template('index.html')

@app.route('/get-network-interfaces', methods=['GET'])
def get_network_interfaces_endpoint():
    interfaces = get_network_interfaces()
    return jsonify(interfaces)

if __name__ == '__main__':
    app.run(debug=True)
