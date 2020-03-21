import random
import threading
import time
import json

import flask
from flask import Flask
from flask import render_template
from flask import request
from flask import Response

app = Flask(__name__)


def get_message():
    """this could be any function that blocks until data is ready"""
    time.sleep(0.3)
    random_event = random.choice(["blink", "jaw"])
    return random_event


@app.route("/events")
def events():
    def eventStream():
        while True:
            # wait for source data to be available, then push it
            yield "data: {}\n\n".format(get_message())

    return Response(eventStream(), mimetype="text/event-stream")


@app.after_request
def add_headers(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    return response
