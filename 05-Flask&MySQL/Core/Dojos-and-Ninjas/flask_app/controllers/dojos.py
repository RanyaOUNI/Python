
from flask_app import app
from flask import render_template , request, redirect
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    all_dojos = Dojo.get_all()
    return render_template("index.html", dojos = all_dojos)

@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    Dojo.create(request.form)
    return redirect('/')

@app.route('/dojos/<int:dojo_id>')
def show_one_dojo(dojo_id):
    dojo = Dojo.get_one_by_id_with_ninjas({'id': dojo_id})
    return render_template('one_dojo.html', dojo = dojo)