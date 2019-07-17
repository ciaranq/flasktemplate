#! /usr/local/bin/python3
# Ciarans template on flask

import json
import os


from flask import Flask, render_template, request, flash
from pathlib import Path
mypath = Path().absolute()
# print(mypath) -- checking path

app = Flask(__name__)
app.secret_key = 'some_secret'


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html", page_title="Heh Welcome Y'all", page_heading="We are team of awesome designers making websites with Full Stack stuff", list_stuff_wedo=["Bootstrap", "Django", "Flask", "Python", "Javascript"])


@app.route('/about')
def about():
    return render_template("about.html")

# seperate contact page for this , taken from bottom of page
@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        print(request.form["name"])
        flash("Thats cool {},we got your note!" .format(request.form["name"]))
        # flash("Thanks {}, we have received your message".format(request.form["name"]))
    return render_template("contact.html")

# must use the url_for('magento') tag to refere to these
@app.route('/magento')
def magento():
    data = []
    with open("data/static.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("magento.html", page_title="Magento data via API's", staticMage=data)


@app.route('/magento/<member_name>', methods=["GET", "POST"])
def about_member(member_name):
    member = {}
    with open("data/static.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
   # return "<h1>"+member["name"]+"</h1>"
    return render_template("member.html", member=member)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT', 5000),
            # add a default for the port number
            debug=True)
