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
            to_return[i] = base64.urlsafe_b64decode(to_return[i]).decode('utf8') 
        return to_return

if __name__ == "__main__":

    # decoder = Decoder("1772637d97b43bda")
    # dict = decoder.get_messages()
    # messages = decoder.get_mails(dict)

    # final_payload = decoder.decode_payload(messages)
    # print("TOTAL MAILS IN THIS THREAD : ", len(final_payload))
    # for i in range(len(final_payload)):
    #     print(final_payload[i])

    thread_ids = get_placement_mail_thread_ids()
    cnt = 0
    for id in thread_ids:
        decoder = Decoder(id)
        dict = decoder.get_messages()
        messages = decoder.get_mails(dict)

        final_payload = decoder.decode_payload(messages)
        with open(f"../data/{cnt}.out", "w") as f:
            f.write("TOTAL MAILS IN THIS THREAD : " + str(len(final_payload)) + "\n")
            for i in range(len(final_payload)):
                f.write(final_payload[i])
        cnt += 1

