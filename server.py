#!/usr/bin/env python

from flask import Flask, render_template, request, redirect
import os
import csv

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_database(data):
    with open("database.txt", 'a') as d:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        d.write(f"\n{email},{subject},{message}")


def write_to_csv(data):
    with open("database.csv", 'a', newline='') as d2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(d2, delimiter=",")
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thankyou.html")
        except:
            return "Could not save to database"
    else:
        return "somthing went wrong"


