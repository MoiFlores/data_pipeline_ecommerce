from boxsdk import Client, OAuth2
from dotenv import load_dotenv
from pymongo import MongoClient
import os
import json

load_dotenv()

# Crear una clase que cargue files al datalake (BOX)
class BoxLoaders:
    # Inicializar nuestra clase con las credenciales
    def __init__(self):
        self.client_id = os.getenv("CLIENT_ID")
        self.client_secret = os.getenv("CLIENT_SECRET")
        self.developer_token = os.getenv("DEVELOPER_TOKEN")

    def move_files_to_box(self, file_path:str, folder_id:str):
        """Este metodo sirve para enviar archivos a BOX"""
        oauth2 = OAuth2(self.client_id, self.client_secret,
                 access_token=self.developer_token)
        client = Client(oauth2)
        upload_file = client.folder(folder_id).upload(file_path)
        print("File successfully uploaded")
    
    def get_data_from_mongo(self, MONGO_URI:str, db_name:str,
                             collection_name:str):
        mongo_client = MongoClient(MONGO_URI)
        mongo_db = mongo_client[db_name]
        mongo_collection = mongo_db[collection_name]
        mongo_data = list(mongo_collection.find({}, {"_id":0}))

        with open("tmp_files/tmp_file.json", 'w') as json_file:
            for document in mongo_data:
                json.dump(document, json_file, default=str)
                json_file.write('\n')

        self.move_files_to_box("tmp_files/tmp_file.json", '310776586821')
        print("Data from mongo loaded to Box")
    


