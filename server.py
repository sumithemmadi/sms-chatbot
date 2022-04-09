from flask import Flask
import subprocess as sp

output = sp.getoutput('termux-notification-list')

app = Flask(__name__)

@app.route('/')
def hello():
    return output
