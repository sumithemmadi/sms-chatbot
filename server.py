from flask import Flask
import subprocess as sp
import json

output = sp.getoutput('termux-notification-list')
jsonOutput = json.dumps(output)
app = Flask(__name__)

@app.route('/')
def hello():
    return print(len(jsonOutput))
if __name__ == "__main__":
    app.run()
