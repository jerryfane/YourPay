from bottle import request, route, run, template, redirect
import os
import create_account
from config import *
from functions import *

@route('/<username>/<random_number>.html')
def dashboard(username, random_number):

    #controlla se l'utente ha fatto il login
    with open('%s_login.txt' %username) as f:
        content = f.readlines()
    current_number = content[0].strip()
    print(current_number, random_number)
    if int(random_number) == int(current_number):

        #load Account from json file
        account_data = load_account_data(username, False)
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
    payment['amount'] = float(request.forms.get('amount'))
    payment['account'] = request.forms.get('account')
    payment['comment'] = request.forms.get('comment')

    #load Account from json file
    account_name = load_account_data(username, False)

    #add the new row
    account_name.new_row(payment['date'], payment['amount'], payment['account'], payment['comment'], True)

    #save datas to json
    with open('./Accounts/%s.json' %username, 'w') as fp:
        json.dump(account_name.toJSON(), fp)

    return "<h1>ROW ADDED</h1>"

@route('/<username>/download/<random_number>.html')
def download_data(username, random_number):
    redirect('/datas/%s/%s.json/%d.html' % (username, username, random_number), 301)


@route('/<username>/logout')
def logout(username):
    os.remove('%s_login.txt' %username)
    return template('./Templates/logout')
