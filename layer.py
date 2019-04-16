from bottle import request, route, run, template, redirect, static_file
import json
import os
from pprint import pprint
import create_account
import manage_account
from functions import encrypt_string
from random import randint
from config import account_password, account_dict


@route('/')
def homepage():
    return template('./Templates/homepage')


@route('/login', method='POST')
def check_login():
    username = request.forms.get('username')
    password = str(request.forms.get('password'))
    password = encrypt_string(password)
    #open json with passwords
    with open('password.json') as f:
        password_dict = json.load(f)

    random_number = randint(0, 9)
    try:
        os.remove('%s_login.txt' %username)
    except:
        pass
    with open('%s_login.txt' %username, 'a') as file:
        file.write(str(random_number))

    if password_dict[username] == password:
        redirect('/%s/%d.html' % (username, random_number), 301)
    else:
        return "<br><center><h1>FAILED TO LOG IN</h1></center>"


@route('/login/<username>')
def login(username):
    return "<h1> %s SUCCESFULLY LOGGED IN</h1>" % username


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static/')

@route('/datas/<filename:path>')
def send_static(filename):
    return static_file(filename, root='Accounts/')


run(host='localhost', port=8080)
