from flask import Flask
from threading import Thread
import logging

app = Flask(__name__)

@app.route('/')
def home():
    # startup message for the web server, can be customized or removed
    return 'Bot is running!'

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Suppress Flask and Werkzeug logging to avoid cluttering the console
logging.getLogger('werkzeug').setLevel(logging.ERROR)
logging.getLogger('flask.app').setLevel(logging.ERROR)