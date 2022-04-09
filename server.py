import os
import json
import subprocess as sp
from dotenv import load_dotenv
from google.cloud import dialogflow_v2beta1 as dialogflow

load_dotenv()

print("loading contacts")
os.system("termux-contact-list > contacts.json")
with open('contacts.json', 'r') as contactList:
  data = json.load(contactList)

for contact in contactList:
    print(len(contact))


projectId = "athena-lvsbrh"
sessionId = "123456"


while 1 == 1:
    output = sp.getoutput('termux-notification-list')
    jsonData = json.load(output)
    for notification in jsonData:
        if notification['packageName'] == "com.termux":
            sessionClient = dialogflow.SessionsClient()
            session = sessionClient.session_path(projectId, sessionId)
            textInput = dialogflow.TextInput(text="hi", language_code="en_US")
            queryInput = dialogflow.QueryInput(text=textInput)
            response = sessionClient.detect_intent(
                request={"session": session, "query_input": queryInput})
            print("Fulfillment text: {}\n".format(
                response.query_result.fulfillment_text))
            sms_sent_status = sp.getoutput('termux-sms-send -n ')
            print("SMS sent successfully")
    
    output.close()
