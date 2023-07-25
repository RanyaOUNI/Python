from flask import Flask,render_template,redirect,request
from user_model import User
app = Flask(__name__)


@app.route('/')
def dashboard():
    all_users = User.get_all()
    return render_template('Read.html',users=all_users)

@app.route('/users/new')
def new_user():
     return render_template('Create.html')

@app.route('/users/Create',methods=['POST'])
def create_user():
    print(request.form)
    data_dict = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email']    
        }
    User.create_user(data_dict)
    return redirect('/')




if __name__ == '__main__':
    app.run(debug=True,port=5000)