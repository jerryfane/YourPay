from bottle import request, route, run, template, redirect
from config import *
from functions import *

@route('/<username>/stats/<random_number>.html')
def statistics(username, random_number):

    #controlla se l'utente ha fatto il login
    with open('%s_login.txt' %username) as f:
        content = f.readlines()
    current_number = content[0].strip()
    print(current_number, random_number)
    if int(random_number) == int(current_number):

        #load Account from json file
        account_data = load_account_data(username, False, account_password_cipher[username])
        #print(account_data.get_accounts())
        account_name = account_data.get_all_rows() #get rows from Account

        #get category list
        category_list = account_data.get_category_list()

        category_balance = {}
        first_date = account_data.get_first_date()

        total_spent = account_data.get_total_spent()

        for category in category_list:
            category_balance[category] = {}
            category_balance[category]['balance'] = account_data.get_amount_by_category_date(category, first_date)
            category_balance[category]['percentage'] = str(int(category_balance[category]['balance'] / total_spent)) + '%'

        info = {'account_name': account_name, 'username': username, \
         'category_list': category_list, "category_balance": category_balance, \
         "random_number": random_number, "total_spent": total_spent}

        return template('./Templates/stats', info)

    else:
        return template('./Templates/no_login')
