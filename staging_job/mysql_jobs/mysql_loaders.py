import pymysql
import json
from dotenv import load_dotenv
import os

load_dotenv()

class MySQLoaders:

    def __init__(self):
        self.host = os.getenv("HOST")
        self.user = os.getenv("USER")
        self.password = os.getenv("PASSWORD")
        self.database = os.getenv("DATABASE")
        # Conexión a MySQL
        self.conn = pymysql.connect(host=self.host,user=self.user,
                                    password=self.password,database=self.database)
        self.cursor = self.conn.cursor()

    def insert_from_json(self):
        # Leer JSON e insertar a la base de datos
        with open("tmp_files/tmp_file.json", 'r', encoding='utf-8') as json_file:
            for document in json_file:
                row = json.loads(document)
                self.cursor.execute("INSERT INTO raw.orders (name, price, description_product, quantity) VALUES (%s, %s, %s, %s)",
                                    (row['product']['name'], row['product']['price'], row['product']['description'],row['quantity']))
                
        self.conn.commit()
        self.conn.close()
        print("Datos insertados en MySQL")
