import requests
import base64
import time

from dotenv import dotenv_values
config=dotenv_values(".env")
KEY=config['KEY']


# 
upload_url=\
    'https://api.media.io/v2/import/base64'
convert_url=\
    'https://api.media.io/v2/convert'
download_url=\
    'https://api.media.io/v2/export/url'

# Conversion del archivo para enviarlo en Base64
with open("TheFourStations.mp3","rb") as f:
    archivo64=base64.b64encode(f.read())


# Configuracion de envio
headers={
    'Content-Type':'application-json',
    'Authorization':KEY
}
params={
    'content':archivo64,
    'file_name':'test.mp3'
}


# 
response=requests.post(
    upload_url,
    headers=headers,
    params=params
)