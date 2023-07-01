from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "im awake :pepeblush:"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
#dn exw idea pws douleuei, alla me auto kanoume ping to server kathe 5 lepta gia na mh kleisei 
# kalh fash 
#brb
