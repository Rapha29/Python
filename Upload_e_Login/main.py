import os
from flask import Flask, request, send_from_directory, render_template, jsonify, g
from werkzeug.security import generate_password_hash, check_password_hash
from file_list_utils import get_file_list
from image_gallery_utils import get_image_gallery
from database import UserDatabase
from User import User
import requests

app = Flask(__name__)

def get_user_db():
    if 'user_db' not in g:
        g.user_db = UserDatabase('database/users.db')
    return g.user_db

user_db = UserDatabase('database/users.db')

def get_client_ip():
    client_ip = request.remote_addr
    return client_ip

def get_location_info(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()
    return data

@app.route('/get_temperature')
def get_temperature():
    client_ip = get_client_ip()
    location_info = get_location_info(client_ip)
    print(f"IP coletado: {client_ip}")
    print(f"Localização coletada: {location_info}")

    if "city" in location_info and "regionName" in location_info and "country" in location_info:
        location = f"{location_info['city']}, {location_info['regionName']}, {location_info['country']}"
        temperature = "Temperatura obtida da API de clima"
    else:
        location = "Não disponível"
        temperature = "Não disponível"

    return temperature

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    user = User.login(username, password)
    
    if user:
        file_list = get_file_list()
        image_gallery = get_image_gallery()

        client_ip = get_client_ip()

        # Obtém as informações de localização usando um serviço externo
        location_info = get_location_info(client_ip)
        print(f"Localização coletada: {location_info}")

        if "city" in location_info and "regionName" in location_info and "country" in location_info:
            location = f"{location_info['city']}, {location_info['regionName']}, {location_info['country']}"
        else:
            location = "Não disponível"

        return render_template('index.html', file_list=file_list, image_gallery=image_gallery, client_ip=client_ip, location=location)
    else:
        file_list = get_file_list()
        image_gallery = get_image_gallery()

        client_ip = get_client_ip()

        # Obtém as informações de localização usando um serviço externo
        location_info = get_location_info(client_ip)
        print(f"Localização coletada: {location_info}")

        if "city" in location_info and "regionName" in location_info and "country" in location_info:
            location = f"{location_info['city']}, {location_info['regionName']}, {location_info['country']}"
        else:
            location = "Não disponível"
        return render_template('erro.html')
    
@app.route('/upload_file', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        file.save(os.path.join('./static/uploads', file.filename))
        file_list = get_file_list()  # Atualizada para usar a nova função
        image_gallery = get_image_gallery()
        return render_template('index.html', file_list=file_list, image_gallery=image_gallery)
    else:
        return jsonify({'message': 'Envie um arquivo usando POST.'})

@app.route('/static/uploads/<filename>')
def download(filename):
    return send_from_directory('./static/uploads', filename)

@app.route('/')
def form():
    return render_template('login.html')

@app.route('/cadastro')
def ad():
    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
