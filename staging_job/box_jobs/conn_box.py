from boxsdk import Client, OAuth2
from dotenv import load_dotenv
import os

load_dotenv()
# Definimos las variables de entorno
developer_token = os.getenv("DEVELOPER_TOKEN")
client_id = os.getenv("CLIENT_ID")
cliente_secret = os.getenv("CLIENT_SECRET")

# Autenticación
oauth2 = OAuth2(client_id, cliente_secret,
                 access_token=developer_token)

# Crear un client para interacturar con BOX
client = Client(oauth2)
items = client.folder('0').get_items()

if __name__ == '__main__':
    for item in items:
        print(f"Folder name {item.name} and Folder ID {item.id}")

