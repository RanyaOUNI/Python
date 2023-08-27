from flask import render_template, redirect, session, request
from flask_app import app
from flask_app.models.user_model import User

#------ INDEX PAGE : Forms (Register and Login) ------

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/users/create', methods=['POST'])
def create():
    if User.validate(request.form):
        User.create(request.form)
        return redirect('/dashboard')
    return redirect('/')