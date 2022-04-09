from flask import Flask
import subprocess as sp
import json


app = Flask(__name__)


@app.route('/')
def hello():
    output = sp.getoutput('termux-notification-list')
    jsonOutput = json.dumps(output)
    return jsonOutput
if __name__ == "__main__":
    app.run()
