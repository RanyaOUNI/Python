from flask import Flask,render_template,redirect,request

app = Flask(__name__)


@app.route('/')
def dashboard():
    user = User.get_all()
    return render_template('Read.html',user=user)





if __name__ == '__main__':
    app.run(debug=True,port=5001)