from bottle import request, route, run, template
from test import Account as Account
import json
from config import account_password, account_dict
from functions import encrypt_string


@route('/create_account', method='POST')
def do_account():
    global username
    username = request.forms.get('username')
    password = request.forms.get('password')
    #bisogna salvare il pair username/password
    password = encrypt_string(password)

    #load passwords class
    with open('password.json') as f:
        account_password = json.load(f)

    #bisognerebbe controllare se l'account esiste già
    account_password[username] = password

    with open('password.json', 'w') as fp:
        json.dump(account_password, fp)

    info = {'username': username}

    return template('./Templates/create_account_1', info)


@route('/<username>/create_account')
def get_datas(username):
    global account_number
    account_number = request.query.account_number

    #creo un account con il nome specificato
    account_dict[username] = Account(username, account_number)

    #load usernames list
    with open('usernames.json') as f:
        username_list = json.load(f)

    username_list.append(username)

    #overwrite username_list
    with open('usernames.json', 'w') as fp:
        json.dump(username_list, fp)

    print(1, username)

    info = {'username': username, 'account_number': int(account_number)}

    return template('./Templates/create_account', info)


@route('/<username>/account_created', method='POST')
def create_account(username):
    print(2, username)
    name_balance_pairs_list = []

    for i in range(0, int(account_number)):
        list = []
        string_name = "account_name_%s" % str(i+1)
        string_balance = "account_balance_%s" % str(i+1)
        account_name = request.forms.get(string_name)
        account_balance = int(request.forms.get(string_balance))
        list.append(account_name)
        list.append(account_balance)
        name_balance_pairs_list.append(list)

    print(name_balance_pairs_list)
    account_dict[username].create_account(name_balance_pairs_list)

    #save json with data created for the user
    with open('./Accounts/'+username+'.json', 'w') as fp:
        json.dump(account_dict[username].toJSON(), fp)

    info = {'username': username}

    return template('./Templates/account_created', info)
