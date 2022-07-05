from flask import Flask, request, redirect
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
    with open("data.json", "r") as f:
        database = json.load(f)

    id = generate_id(database)

    key = scrypto.generate_key(data['password'], data['title'].encode())

    enc_title = scrypto.encrypt(key, data['title']).decode()

    enc_text = scrypto.encrypt(key, data['text']).decode()

    del key

    id = generate_id(database)

    database[id] = {}

    database[id]['title'] = enc_title

    database[id]['text'] = enc_text

    with open('data.json', 'w') as outfile:
        json.dump(database, outfile, indent = 4)

    return id
    
    
        
    


def server():
        
    app = Flask(__name__)
    
    @app.route("/r", methods=['POST'])
    def user():
        id = new(request.form)
        return redirect("https://necrownyx.github.io/Notebox/" + id)
    
    app.run(host='0.0.0.0', port=8080)

Thread(target=server, daemon=True).start()

while True:
    sleep(10)