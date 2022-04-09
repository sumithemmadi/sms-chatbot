import os
import json
import subprocess as sp
from dotenv import load_dotenv
from google.cloud import dialogflow_v2beta1 as dialogflow
import uuid
  
load_dotenv()
projectId = os.getenv("PROJECTID")
sessionId =  uuid.uuid4()


print("loading contacts")
os.system("termux-contact-list > contacts.json")
with open('contacts.json', 'r') as contactListFile:
  contactList = json.load(contactListFile)

for contact in contactList:
    print(len(contact))

print("running")

while 1 == 1:
    output = sp.getoutput('termux-notification-list')
    jsonData = json.load(output)

    for notification in jsonData:
        if notification['packageName'] == "com.termux":
            number = notification['title']
            text = notification['content']
            ID = notification['id']

            #Find Real Number
            if number[0] != '+':
                for contact in contactList:
                    if contact['name'] == number:
                        number = contact['number']

            sessionClient = dialogflow.SessionsClient()
            session = sessionClient.session_path(projectId, sessionId)
            textInput = dialogflow.TextInput(text, language_code="en_US")
            queryInput = dialogflow.QueryInput(text=textInput)
            response = sessionClient.detect_intent(
                request={"session": session, "query_input": queryInput})
            print(" {}".format(response.query_result.fulfillment_text))
            sms_sent_status = sp.getoutput('termux-sms-send -n '+ number + " {}".format(response.query_result.fulfillment_text))
            os.system("termux-notification-remove  {}".format(ID))
            print("SMS sent successfully")
    
    output.close()
