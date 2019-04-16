from bottle import request, route, run, template, redirect, static_file
from config import *
from functions import *

@route('/.well-known/acme-challenge/<filename:path>')
def send_static(filename):
    return static_file(filename, root='ssl/')
