import subprocess as sp
import json


output = sp.getoutput('termux-notification-list')
jsonOutput = json.loads(output)
print(output[0])
