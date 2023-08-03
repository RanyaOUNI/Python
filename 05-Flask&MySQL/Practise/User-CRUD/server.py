from flask import Flask,render_template,redirect,request
from user_model import User
app = Flask(__name__)

#---------------- All users ------------------

#? GET route
@app.route('/')
def dashboard():
    all_users = User.get_all()
    return render_template('Read.html',users=all_users)

#------------- Create new user ---------------

#? GET route
@app.route('/users/new')
def new_user():
    return render_template('Create.html')

#? POST route
@app.route('/users/Create',methods=['POST'])
def create_user():
    print(request.form)
    data_dict = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email']    
        }

    user_id = User.create_user(data_dict)

    get_user = User.get_one_by_id(data_dict={'id':user_id})
    return render_template('Read(One).html',user=get_user)

# -------------- Show one user ---------------

#? GET route
@app.route('/users/<int:user_id>')
def show_user(user_id):
    data_dict = {'id':user_id}
    user = User.get_one_by_id(data_dict)
    return render_template('Read(One).html', user = user)

# -------------- Edit a user ----------------


@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    user_to_update = User.get_one_by_id({'id':user_id})
    return render_template("Edit.html", user = user_to_update)



@app.route('/users/<int:user_id>/update', methods=['POST'])
def update_user(user_id):
    data_dict={**request.form}
    data_dict['id']=user_id
    User.update_user(data_dict)
    update_user = User.get_one_by_id({'id':user_id})
    return render_template('Read(One).html',user=update_user)


# --------------- Delete a user ---------------

@app.route('/users/<int:user_id>/destroy', methods=['POST'])
def destroy(user_id):
    User.destroy({'id':user_id})
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True,port=5000)