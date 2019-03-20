import os, sys

# make sure src folder is added into sys path.
from flask import Flask
from flask import request, jsonify
from flask import Blueprint
from celery import Celery
from src.routes import *
from threading import Thread
import time
from urllib import request
from twisted.internet import reactor

import json


# test_config=None

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('conf.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(routes)

    #reactor.run()

    # run task prior to first flask request: https://networklore.com/start-task-with-flask/

    @app.before_first_request
    def activate_job():
        def run_job():
            #time.sleep(0.5)
            try:
                if not reactor.running:
                    reactor.run()
            except:
                pass

        thread = Thread(target=run_job)
        thread.start()

    return app
