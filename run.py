#! /usr/local/bin/python3

# Ciarans template on flask

import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", page_title="Heh Welcome Y'all", page_heading="We are team of awesome designers making websites with Full Stack stuff", list_stuff_wedo=["Bootstrap", "Django", "Flask", "Python", "Javascript"])


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/careers')
def careers():
    return render_template("careers.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)
