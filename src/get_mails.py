import os
import pickle
from googleapiclient.discovery import build
from pprint import pprint



def build_service():
    creds = None
    if os.path.exists("token.pickle"):
       creds = pickle.load(open("token.pickle", 'rb'))

    if(creds):
        service = build('gmail', 'v1', credentials = creds)
        return service
    else:
        raise Exception("Token.Pickle not Found!")


def example_endpoint():
    # Call the Gmail API
    service = build_service()
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])


    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])


# Return the Google Mail using Thread-Id 
def get_thread(id : str):
    service = build_service()
    mail = service.users().threads().get(userId = "me", id = id).execute()

    return mail


def get_placement_mail_thread_ids():
    service = build_service()
    '''
    Possible Params:
    1. maxResults(uint32) : Max Possible Mail Ids from 0 to pow(2, 32) - 1. 
    2. pageToken (string): Current Page Token to Scrap 
    3. q(string) : Query to perform. Example : from:someuser@example.com
    4. labelIds : Will not use this
    5. includeSpamTrash : Will not use this
    '''
    param_query = "category:primary +(Recruitment) +(Drive) +(recruitment) +(drive)"
    param_page_token = None
    # Lets just get the 500 messages 
    param_max_len = 500000 
    param_max_results = param_max_len

    ids_objects = []
    found = 0
    while(found < param_max_len):
        param_max_results = param_max_len - found
        results = service.users().messages().list(userId = "me", 
                                                pageToken = param_page_token, 
                                                maxResults = param_max_results, 
                                                q = param_query).execute()
        ids_objects += results["messages"]
        found += results["resultSizeEstimate"]
        try :
            param_page_token = results["nextPageToken"]
        except KeyError:
            break

    pprint(ids_objects[0])
    pprint(type(ids_objects))

    # Find all the possible different Thread Ids 
    s = set()
    for x in ids_objects:
        s.add(x["threadId"])
    pprint(len(s))
    
    return list(s)

'''
Possible Categories : 
CHAT
SENT
INBOX
IMPORTANT
TRASH
DRAFT
SPAM
CATEGORY_FORUMS
CATEGORY_UPDATES
CATEGORY_PERSONAL
CATEGORY_PROMOTIONS
CATEGORY_SOCIAL
STARRED
UNREAD
'''


if __name__ == "__main__":
    threads = get_placement_mail_thread_ids()
    mail = get_thread(threads[0])
    pprint(mail)