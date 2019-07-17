#! /usr/local/bin/python
# Ciarans template on flask

import json
import os
from flask import Flask, render_template, request, flash
from pathlib import Path


app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello Worldz"


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            # port=5500,
            port=int(os.environ.get('PORT')),
            debug=True)
