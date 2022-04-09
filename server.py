from flask import Flask
import subprocess as sp
import json


output = sp.getoutput('termux-notification-list')
jsonOutput = json.loads(output)

app = Flask(__name__)

@app.route('/')
def hello():

    return output[0]


if __name__ == "__main__":
    app.run()
