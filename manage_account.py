from bottle import request, route, run, template, redirect
import os
import create_account
from config import *
from functions import *
from AESCipher import AESCipher

@route('/<username>/<random_number>.html')
def dashboard(username, random_number):

    #controlla se l'utente ha fatto il login
    with open('%s_login.txt' %username) as f:
        content = f.readlines()
    current_number = content[0].strip()
    print(current_number, random_number)
    if int(random_number) == int(current_number):

        #load Account from json file
        account_data = load_account_data(username, False, account_password_cipher[username])
        print(account_data.get_accounts())
        account_name = account_data.get_all_rows() #get rows from Account

        account_balances = account_data.get_accounts()

        info = {'account_name': account_name, 'username': username, 'account_balances': account_balances, "random_number": random_number}
        return template('./Templates/table', info)

    else:
        return template('./Templates/no_login')

@route('/<username>/pay', method='POST')
def add_row(username):
    payment = {}

    payment['date'] = request.forms.get('date')
    payment['amount'] = float(request.forms.get('amount').replace(',', '.'))
    payment['account'] = request.forms.get('account')
    payment['category'] = request.forms.get('category')
    payment['comment'] = request.forms.get('comment')

    #load and decrypt Account from json file
    account_name = load_account_data(username, False, account_password_cipher[username])

    #add the new row
    account_name.new_row(payment['date'], payment['amount'], payment['account'], payment['category'], payment['comment'], True)

    #save datas to json
    with open('./Accounts/%s.json' %username, 'w') as fp:
        encrypted_data = account_password_cipher[username].encrypt(account_name.toJSON())
        encrypted_data = encrypted_data.decode("utf-8")
        json.dump(encrypted_data, fp)

    return "<h1>ROW ADDED</h1>"

@route('/<username>/new_account', method='POST')
def add_account(username):
    create_account_name = str(request.forms.get('account_name'))
    create_account_balance = float(request.forms.get('balance').replace(',', '.'))

    create_account_list = [[create_account_name, create_account_balance]]

    #load and decrypt Account from json file
    account_name = load_account_data(username, False, account_password_cipher[username])

    #create new account
    account_name.create_account(create_account_list)

    #save datas to json
    with open('./Accounts/%s.json' %username, 'w') as fp:
        encrypted_data = account_password_cipher[username].encrypt(account_name.toJSON())
        encrypted_data = encrypted_data.decode("utf-8")
        json.dump(encrypted_data, fp)

    return "<h1>ACCOUNT ADDED</h1>"

@route('/<username>/remove_row', method='POST')
def remove_row(username):
    row_id = int(request.forms.get('row_id'))

    #load and decrypt Account from json file
    account_name = load_account_data(username, False, account_password_cipher[username])

    #remove row
    account_name.remove_row(row_id)

    #save datas to json
    with open('./Accounts/%s.json' %username, 'w') as fp:
        encrypted_data = account_password_cipher[username].encrypt(account_name.toJSON())
        encrypted_data = encrypted_data.decode("utf-8")
        json.dump(encrypted_data, fp)

    return "<h1>ROW DELETED</h1>"


@route('/<username>/download/<random_number>.html')
def download_data(username, random_number):
    redirect('/datas/%s/%s.json/%d.html' % (username, username, random_number), 301)


@route('/<username>/logout')
def logout(username):
    os.remove('%s_login.txt' %username)
    return template('./Templates/logout')
