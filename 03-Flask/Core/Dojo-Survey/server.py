from flask import Flask,render_template,redirect,request,session
app = Flask(__name__)
app.secret_key = "tattou"

@app.route('/') 
def index():
    return render_template('index.html')

# @app.route('/result',methods=['POST'])
# def info():
#     return render_template('result.html')


@app.route('/result',methods=['POST'])
def result():
    session['name'] = request.form['name']
    session['dojo_location'] = request.form['dojo_location']
    session['favorite_language'] = request.form['favorite_language']
    session['comment'] = request.form['comment']
    return render_template('result.html')



if __name__ == '__main__':
    app.run(debug=True,port=5000)