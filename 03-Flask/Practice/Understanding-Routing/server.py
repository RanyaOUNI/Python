from flask import Flask

app = Flask(__name__)


@app.route('/')
def Hello():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def Hi(name):
    return f'Hi {name}!'

@app.route('/repeat/<int:num>/<string:word>')
def repeat(word,num):
    return f'{word*num}'




if __name__ == "__main__" :
    app.run(debug=True,host="localhost", port=5000)