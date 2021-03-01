import os 
import pickle
import base64

from googleapiclient.discovery import build
from pprint import pprint
from get_mails import build_service, get_thread, get_placement_mail_thread_ids
from collections import OrderedDict


class Decoder(object):
    def __init__(self, thread_id):
        self.thread_id = thread_id
        self.thread = get_thread(self.thread_id)
        # self.thread_id = "1772637d97b43bda"
        self.possible = []

    def get_messages(self):
        return OrderedDict({"threadId" : self.thread_id, "messages" : self.thread["messages"]})

    def get_mails(self, messages_dict):
        messages = []
        for message in messages_dict["messages"]:
            messages.append(message["payload"])
        return messages
    
    # Recursive Function to find data of type MimeType -> "text/plain"
    def dfs(self, payload):
        # print(payload['body'], payload['parts'])
        try :
            if(payload['mimeType'] == "text/plain"):
                self.possible.append(payload['body']['data'])
        except :
            pass
        
        try:
            for parts_payload in payload['parts']:
                self.dfs(parts_payload)
        except : 
            pass
        
        return self.possible

    # Uses Recursive Approach to get all the data that is of MimeType -> "text/plain" 
    def decode_payload(self, messages):
        cnt = 0
        for message_part in messages:
            self.dfs(message_part)
            cnt += 1
        to_return = self.possible
        self.possible = []

        # Decode the data before return
        for i in range(len(to_return)):
            to_return[i] = base64.b64decode(to_return[i] + '=' * (4 - len(to_return[i])%4))
        return to_return
    
    # Convert the Base64 decoded Payload to normal readble text data
    def make_readable(self, messages):
        dict = OrderedDict()
        cnt = 0
        for i in range(len(messages)):
            messages[i].splitlines 
        
if __name__ == "__main__":
    # possible_thread_ids = get_placement_mail_thread_ids()
    decoder = Decoder("1772637d97b43bda")

    dict = decoder.get_messages()
    messages = decoder.get_mails(dict)

    final_payload = decoder.decode_payload(messages)
    pprint(len(final_payload))
    pprint(final_payload)
