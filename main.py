from flask import Flask, render_template, request, flash, redirect, request, session, url_for
import os
import sqlite3

currentlocation = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

# login form
@app.route("/", methods=["POST"])
def checklogin():
    UN = request.form['Username']
    PW = request.form['Password']
    sqlconnection = sqlite3.Connection(currentlocation + "\Login")
    cursor = sqlconnection.cursor()
    query1 = "SELECT * FROM Users WHERE Username='{un}' AND Password='{pw}'".format(
        un=UN, pw=PW)
    cursor.execute(query1)
    results = cursor.fetchall()
    if len(results) == 1:
        return render_template("loggedin.html")
    else:
        return redirect("/register")

# registration form
@app.route("/register", methods=["GET", "POST"])
def registerpage():
    if request.method == "POST":
        dUN = request.form['DUsername']
        dPW = request.form['DPassword']
        Uemail = request.form['EmailUser']
        sqlconnection = sqlite3.Connection(currentlocation + "\Login")
        cursor = sqlconnection.cursor()
        query1 = "INSERT INTO Users VALUES('{u}','{p}','{e}')".format(
            u=dUN, p=dPW, e=Uemail)
        cursor.execute(query1)
        sqlconnection.commit()
        return redirect("/")
    return render_template("register.html")


@app.route("/recepies/")
def recepieBook():
    return render_template("recepies.html")


@app.route("/forum/")
def forum():
    return render_template("forum.html")


@app.route("/blog/")
def blog():
    return render_template("blogExample.html")


@app.route("/dog/")
def dog():
    return render_template("dogs.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
