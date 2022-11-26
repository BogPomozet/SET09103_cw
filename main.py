from flask import Flask, render_template, request, flash

app = Flask(__name__)
# encription to sequre cookies and session data
# app.config['SECRET_KEY'] = 'petri_secret_@@'


@app.route("/")
def index(): 
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
