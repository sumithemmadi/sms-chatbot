import subprocess as sp
import json


output = sp.getoutput('termux-notification-list')
jsonOutput = json.dumps(output)
print(jsonOutput[0])

