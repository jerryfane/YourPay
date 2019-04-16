import hashlib
from test import *

#encrypt a string in SHA256
def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

#load account datas from JSON file
def load_account_data(username, change_balance):
    #load account_name class
    with open('./Accounts/%s.json' %username) as f:
        json_datas = json.load(f)

    account_name = Account(username, 0) #recreate the account
    object_data = json.loads(json_datas) #create an object with json datas
    account_name.loadJSON(object_data, change_balance) #load all datas to the Account class
    return account_name

#get a list of keys in dictionary
def dkeys2list(dict):
    list = []
    for i in dict:
        list.append(i)
    return list
