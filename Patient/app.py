from flask import Flask, render_template, request

import model

from form import Form

app = Flask(__name__)

app.secret_key = "My secret key"


@app.route('/', methods=['GET', 'POST'])
def main():

    form = Form(request.form)

    if request.method == 'GET':
        return render_template("interface.html", form=form)

    form.name.data


