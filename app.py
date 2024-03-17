from flask import Flask, request, jsonify
from flask_cors import CORS
import socket
import subprocess

app = Flask(__name__)
CORS(app)

def get_service_version(ipaddress, port):
    try:
        sock = socket.create_connection((ipaddress, port), timeout=1)  # Increase timeout to 5 seconds
        banner = sock.recv(1024).decode('utf-8').strip()
        sock.close()
        return banner
    except Exception as e:
        return None

def searchsploit(query):
    try:
        result = subprocess.check_output(['searchsploit', query], universal_newlines=True)
        return result.strip()
    except Exception as e:
        return f"Error executing searchsploit: {str(e)}"

@app.route('/scan', methods=['POST'])
def scan():
    data = request.get_json()
    ipaddress = data.get('ipaddress')
    ports = data.get('ports', 1024)
    ports = int(ports)
    response = []

    for port in range(1, ports+1):
        banner = get_service_version(ipaddress, port)
        if banner:
            service_info = {
                'port': port,
                'service': banner,
                'vulnerability': None
            }
            # Add searchsploit to rate vulnerability
            vulnerability_query = f"{banner.split(' ')[0]} {banner.split(' ')[1]}"
            vulnerability_result = searchsploit(vulnerability_query)
            service_info['vulnerability'] = vulnerability_result
            response.append(service_info)

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)