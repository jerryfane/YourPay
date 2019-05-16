from bottle import request, route, run, template, redirect
from config import *
from functions import *
from collections import OrderedDict
from Stats import Stats
import os
import random

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
        #account_name = account_data.get_all_rows() #get rows from Account

        #get category list
        #category_list = account_data.get_category_list()

        #category_balance = {}
        #first_date = account_data.get_first_date()

        #total_spent = round(float(account_data.get_total_spent()),2)

        #for category in category_list:
        #    category_balance[category] = {}
        #    category_balance[category]['balance'] = round(float(account_data.get_amount_by_category_date(category, first_date)),2)
        #    category_balance[category]['percentage'] = str(round(float(category_balance[category]['balance'] / total_spent)*100, 2)) + '%'

        #category_balance_ordered = OrderedDict(sorted(category_balance.items(), key=lambda x: x[1]['balance']))

        #update category list
        #category_list = []
        #or category in category_balance_ordered:
        #    category_list.append(category)

        account_stats = Stats(account_data)

        balance_per_day = account_stats.chart_balance_perday()
        balance_per_month = account_stats.chart_balance_permonth()
        amount_spent_per_day = account_stats.chart_total_amount_spent_perday()
        amount_spent_per_month = account_stats.chart_total_amount_spent_permonth()

        try:
            os.makedirs("./static/"+username) #create a directory if it does not exist
        except:
            pass

        try:
            os.remove("./static/"+username+"/balance_per_day.png")
        except:
            pass
        try:
            os.remove("./static/"+username+"/balance_per_month.png")
        except:
            pass
        try:
            os.remove("./static/"+username+"/amount_spent_per_day.png")
        except:
            pass
        try:
            os.remove("./static/"+username+"/amount_spent_per_month.png")
        except:
            pass



        balance_per_day.savefig("./static/"+username+"/balance_per_day.png")
        balance_per_month.savefig("./static/"+username+"/balance_per_month.png")
        amount_spent_per_day.savefig("./static/"+username+"/amount_spent_per_day.png")
        amount_spent_per_month.savefig("./static/"+username+"/amount_spent_per_month.png")

        accounts_list = account_data.get_accounts_list()
        category_list = account_data.get_category_list()
        print(category_list)

        random_integer = random.randint(0, 9999)
        info = {'username': username, "random_number": random_number, "accounts_list": accounts_list, \
                "category_list": category_list, "random_integer": random_integer}

        return template('./Templates/stats2', info)

    else:
        return template('./Templates/no_login')


@route('/<username>/category', method='POST')
def category(username):
    chart = request.forms.get('chart').lower().capitalize()
    category = str(request.forms.get('category').lower().capitalize())
    print(category)

    account_data = load_account_data(username, False, account_password_cipher[username])
    account_stats = Stats(account_data)

    if chart == 'Amount spent per day':
        chart_file = account_stats.chart_amount_spent_perday_category(category)
    elif chart == 'Amount spent per month':
        chart_file = account_stats.chart_amount_spent_permonth_category(category)

    try:
        os.remove("./static/"+username+"/created_chart.png")
    except:
        pass

    random_integer = random.randint(0, 9999)
    chart_file.savefig("./static/"+username+"/created_chart.png")
    info = {'username': username, "random_integer": random_integer}
    return template('./Templates/created_chart', info)

@route('/<username>/account', method='POST')
def account(username):
    chart = request.forms.get('chart').lower().capitalize()
    account = str(request.forms.get('account').lower().capitalize())
    print(account)

    account_data = load_account_data(username, False, account_password_cipher[username])
    account_stats = Stats(account_data)

    if chart == 'Balance per day':
        chart_file = account_stats.chart_balance_perday_account(account)
    elif chart == 'Balance per month':
        chart_file = account_stats.chart_balance_permonth_account(account)
    elif chart == 'Amount spent per day':
        chart_file = account_stats.chart_amount_spent_perday_account(account)
    elif chart == 'Amount spent per month':
        chart_file = account_stats.chart_amount_spent_permonth_account(account)

    try:
        os.remove("./static/"+username+"/created_chart.png")
    except:
        pass

    random_integer = random.randint(0, 9999)
    chart_file.savefig("./static/"+username+"/created_chart.png")
    info = {'username': username, "random_integer": random_integer}
    return template('./Templates/created_chart', info)

@route('/nochart')
def nochart():
    return template('./Templates/nochart')
