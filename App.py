from flask import Flask, render_template, jsonify, request, redirect, url_for, session
import json
from request import Users
from generate_img.app import generate  # Importando a função generate
import logging
from dotenv import load_dotenv
import os
#from generate_img.app import load_config, save_config  # Importando as funções de configuração




load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('secret_key')


logging.basicConfig(
    level=logging.INFO,  # Altere para DEBUG para mais informações
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),  # Salva os logs em app.log
        logging.StreamHandler()  
    ]
)


def get_users():
    try:
        logging.info("Tentando obter usuários...")
        users = Users() 
        return users
    except Exception as e:
        logging.error(f"Erro ao obter usuários: {e}")
        return []


@app.route('/api/users/search', methods=['GET'])
def search_users():
    name_query = request.args.get('name', '').lower()
    logging.info(f"Buscando usuários com o nome: {name_query}")
    
    users = get_users()
    if not users:
        logging.warning("Nenhum usuário encontrado ou erro ao buscar usuários.")
        filtered_users = [user for user in users if name_query in user.get('display_name', '').lower()]
    return jsonify(filtered_users)


@app.route('/api/users', methods=['GET'])
def users_json():
    logging.info("Obtendo todos os usuários...")
    users = get_users()
    return jsonify(users)

@app.route('/users', methods=['GET'])
def users_html():
    if not session.get('logged_in'):
        return redirect(url_for('login'))  # Redireciona para a página de login se o usuário não estiver logado
    
    logging.info("Renderizando a página HTML com a lista de usuários...")
    users = get_users()
    return render_template('users.html', users=users)

@app.route('/generate_image', methods=['POST'])
def generate_image():
    data = request.get_json()
    name = data.get('name')
    sector = data.get('sector')
    email = data.get('email')

    logging.info(f"Gerando imagem com os dados: Nome={name}, Setor={sector}, Email={email}")

    if not name or not sector or not email:
        return jsonify({"error": "Nome, setor e e-mail são obrigatórios."}), 400

    try:
        response, status_code = generate(name, sector, email)
        logging.info(f"Imagem gerada com sucesso. Resposta: {response}, Código de status: {status_code}")
        return jsonify(response), status_code
    except Exception as e:
        logging.error(f"Erro ao gerar a imagem: {e}")
        return jsonify({"error": f"Erro ao gerar a imagem: {str(e)}"}), 500

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == os.getenv('user') and password == os.getenv('senha'): 
            session['logged_in'] = True
            return redirect(url_for('users_html')) 

        return "Usuário ou senha inválidos.", 401  

    return render_template('login.html') 

@app.route('/api/config', methods=['POST'])
def save_config():
    data = request.get_json()
    logging.info(f"Recebendo configurações: {data}")

    # Aqui você pode processar as configurações conforme necessário
    # Por exemplo, você pode salvar as coordenadas em um arquivo ou banco de dados
    # Exemplo de salvar em um arquivo JSON:
    try:
        with open('config.json', 'w') as config_file:
            json.dump(data, config_file)
        logging.info("Configurações salvas com sucesso.")
        return jsonify({"message": "Configurações salvas com sucesso!"}), 200
    except Exception as e:
        logging.error(f"Erro ao salvar configurações: {e}")
        return jsonify({"error": "Erro ao salvar configurações."}), 500


if __name__ == '__main__':
    logging.info("Iniciando o servidor Flask...")
    app.run(host='0.0.0.0', port=5000, debug=True)
