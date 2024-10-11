import requests
from dotenv import load_dotenv
import os 

load_dotenv()
def token():
    TENANT_ID = os.gotenv('TENANT_ID')
    CLIENT_ID = os.gotenv('CLIENT_ID')
    CLIENT_SECRET = os.gotenv('CLIENT_SECRET')

    token_url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"

    token_data = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'scope': 'https://graph.microsoft.com/.default'
    }

    token_response = requests.post(token_url, data=token_data)
    token_json = token_response.json()
    print(f"Token Gerado com Sucesso: {token_json}")
    return token_json

def get_all_users(access_token):
    """Obtém todos os usuários."""
    users_url = 'https://graph.microsoft.com/v1.0/users?$select=id,displayName,department,givenName,jobTitle,mail,officeLocation,surname'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    users = []
    while users_url:
        response = requests.get(users_url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            users.extend(data.get('value', []))  
            users_url = data.get('@odata.nextLink')
        else:
            print(f"Erro ao buscar usuários: {response.status_code}")
           
            return []

    return users

def Users():
    token_json = token()
    if 'access_token' in token_json:
        access_token = token_json['access_token']

        users = get_all_users(access_token)

        return users
    else:
        print("Erro ao obter token de acesso:")
        return []

