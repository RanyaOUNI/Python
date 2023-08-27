from flask_app import app
from flask import render_template , request, redirect
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def books():
    all_ninjas = Ninja.get_all()
    all_dojos = Dojo.get_all()
    return render_template("ninjas.html", ninjas = all_ninjas, ninjas = all_ninjas)

@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    Ninja.create(request.form)
    return redirect('/ninjas')