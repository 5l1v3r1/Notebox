from flask import Flask, request, redirect
from threading import Thread
from time import sleep
from SimplifyPython import scrypto
import json
import random
import string
from urllib.parse import quote

def generate_id(data):
    id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(30))
    if id in data:
        generate_id()
    return id

def new(data):
    with open("data.json", "r") as f:
        database = json.load(f)

    id = generate_id(database)

    key = scrypto.generate_key(data['password'], b'')

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

def retrive(data):
    with open("data.json", "r") as f:
        database = json.load(f)

    if data['id'] in database:
        try:
            key = scrypto.generate_key(data['password'], b'')
    
            enc_title = database[data['id']]['title'].encode()
            
            enc_text = database[data['id']]['text'].encode()
    
            title = scrypto.decrypt(key, enc_title)
    
            text = scrypto.decrypt(key, enc_text)
    
            return f'title={quote(title)}&text={quote(text)}'
        except:
            return 'title=404&text=Your%20id%20either%20does%20not%20exist%20or%20your%20passowrd%20is%20not%20valid.'
        
    return 'title=404&text=Your%20id%20either%20does%20not%20exist%20or%20your%20passowrd%20is%20not%20valid.'
        

        

    

    
    
    
        
    


def server():
        
    app = Flask(__name__)

    @app.route('/', methods=['HEAD'])
    def keep_alive():
        return 'Pong'
    
    @app.route("/r", methods=['POST'])
    def index():
        id = new(request.form)
        return redirect("https://rerum-crea.github.io/Notebox/Retrive/index.html?" + id)

    @app.route("/g", methods=['POST'])
    def user():
        id = retrive(request.form)
        return redirect("https://rerum-crea.github.io/Notebox/View/index.html?" + id)
        
    
    app.run(host='0.0.0.0', port=8080)

Thread(target=server, daemon=True).start()

while True:
    sleep(10)