from flask import Flask, request
from threading import Thread
from time import sleep
from SimplifyPython import scrypto
import json
import random
import string

def generate_id(data):
    id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(30))
    if id in data:
        generate_id()
    return id

def new(data):
    with open("database.json", "r") as f:
        database = json.load(f)

    id = generate_id(database)

    key = scrypto.generate_key(data['password'], data['title'])

    enc_title = scrypto.encrypt(key, data['title'])

    enc_text = scrypto.encrypt(key, data['text'])

    
    
    
        
    


def server():
        
    app = Flask(__name__)
    
    @app.route("/r", methods=['POST'])
    def user():
        new(request.form)
        return f"!"
    
    app.run(host='0.0.0.0', port=8080)

Thread(target=server, daemon=True).start()

while True:
    sleep(10)