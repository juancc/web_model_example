"""Download model from server"""
import requests

API_KEY = ''  # Leer archivo de credentials.ods
API = 'https://j8wmps8gr0.execute-api.us-east-2.amazonaws.com/testing'  # Leer archivo de credentials.ods

url = API+'/models/download'
param = {'model': 'detector-free'}
headers = {"x-api-key": API_KEY}

response = requests.get(url, params=param, headers=headers)
response_payload = response.json()

"""
El servidor retorna un json con las direcciones de la arquitectura 
Se procede a descargar cada uno de sus respectivas URLs
{
'detector-free': 
    {'architecture': 'https://vaico-repo.s3....', 
    'model': 'https://vaico-repo.s3.amazonaws...'}
}


"""