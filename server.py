from flask import Flask
import subprocess as sp
import json

contacts = sp.getoutput('termux-contact-list')


output = sp.getoutput('termux-notification-list')

app = Flask(__name__)

@app.route('/')
def hello():
    return contacts
if __name__ == "__main__":
    app.run()
