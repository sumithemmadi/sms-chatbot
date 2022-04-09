import subprocess as sp
import json


output = sp.getoutput('termux-notification-list')
jsonOutput = json.dumps(output)
# print(output[0])

for i in jsonOutput:
    print(jsonOutput[i])
