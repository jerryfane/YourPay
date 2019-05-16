from bottle import request, route, run, template, redirect, static_file
import json
import os
from pprint import pprint
import create_account
import manage_account
import stats_account
from functions import encrypt_string
from random import randint
from config import *
import ssl
from AESCipher import AESCipher


@route('/')
def homepage():
    return template('./Templates/homepage')


@route('/login', method='POST')
def check_login():
    username = request.forms.get('username')
    password = str(request.forms.get('password'))
    password = encrypt_string(password)
    #create an AESCipher class to encrypt and decrypt datas
    password_cipher = AESCipher(password)
    account_password_cipher[username] = password_cipher
    #open json with passwords
    with open('password.json') as f:
        password_dict = json.load(f)

    random_number = randint(0, 99)
    try:
        os.remove('%s_login.txt' %username)
    except:
        pass
    with open('%s_login.txt' %username, 'a') as file:
        file.write(str(random_number))

    if password_dict[username] == password:
        redirect('/%s/%d.html' % (username, random_number), 301)
    else:
        return template('./Templates/no_login')


@route('/login/<username>')
def login(username):
    return "<h1> %s SUCCESFULLY LOGGED IN</h1>" % username


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static/')

@route('/datas/<username>/<random_number>/<filename:path>')
def send_static(username, filename, random_number):
    #controlla se l'utente ha fatto il login
    with open('%s_login.txt' %username) as f:
        content = f.readlines()
    current_number = content[0].strip()
    print(current_number, random_number)
    if int(random_number) == int(current_number):
        file = static_file(filename, root='Accounts/')
        print(file)
        return static_file(filename, root='Accounts/')
    else:
        return template('./Templates/no_login')


run(host='0.0.0.0', port=8080)
