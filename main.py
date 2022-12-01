from flask import Flask, render_template, request, flash, redirect, request, session, url_for
import os
import sqlite3

currentlocation = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
# encription to sequre cookies and session data
# app.config['SECRET_KEY'] = 'petri_secret_@@'


@app.route("/")
def index(): 
    return render_template("index.html")

@app.route("/", methods = ["POST"])
def checklogin():
    UN = request.form['Username']
    PW = request.form['Password']

    sqlconnection = sqlite3.Connection(currentlocation + "\Login")
    cursor = sqlconnection.cursor()
    query1 = "SELECT Username, Password From Users WHERE Username = '{un}' AND Password = '{pw}'".format(un = UN, pw = PW)

    rows = cursor.execute(query1)
    rows = rows.fetchall()
    if len(rows) == 1:
        return render_template("loggedin.html")
    else:
        return redirect("/register")

@app.route("/register", methods = ["GET","POST"])
def registerpage():
    if request.method == "POST":
        dUN = request.form['DUsername']
        dPW = request.form['DPassword']
        Uemail = request.form['EmailUser']

        sqlconnection = sqlite3.Connection(currentlocation + "\Login")
        cursor = sqlconnection.cursor()
        query1 = "INSERT INTO Users VALUES('{u}','{p}','{e}')".format( u=dUN, p=dPW, e=Uemail)
        cursor.execute(query1)
        sqlconnection.commit()
        return redirect("/")
    return render_template("register.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
