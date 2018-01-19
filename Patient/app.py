from flask import Flask, render_template, request

import sqlite3 as lite

from form import Form

app = Flask(__name__)

app.secret_key = "My secret key"


@app.route('/', methods=['GET', 'POST'])
def main():

    form = Form(request.form)

    if request.method == 'GET':
        return render_template("interface.html", form=form)

    con = lite.connect('patient.db')

    with con:
        cur = con.cursor()
        id = form.id.data
        name = form.name.data
        age = form.age.data
        cur.execute("INSERT INTO Patient(ID, Name, Age) VALUES(?, ?, ?)", id, name, age)
        return render_template('success.html')


