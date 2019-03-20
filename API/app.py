# -*- coding: utf-8 -*-
import os
from flask import Flask, url_for, redirect, render_template, request, abort
form annonce import *
# Create Flask application
app = Flask(__name__)

@app.route('/recherche/', methods=['POST'])
def recherche():
    #recupérer les critères de recherche




    #faire la recherche dans notre base de données



    #retourner le résultat au format json







    pass

@app.route('/AuthUser/', methods=['POST'])
def recherche():
    #recupérer les critères de recherche




    #faire la recherche dans notre base de données



    #retourner le résultat au format json







    pass

def GenérerHash(data):
    pass
if __name__ == '__main__':
    # Start app
    app.run(debug=True)
