from flask import Flask,render_template

app = Flask(__name__)

@app.route('/') 
def index():
    return "Hello From Flask"


@app.route('/play')
def boxes():
    return render_template('index.html')

@app.route('/play/<int:x>')
def play_x(x):
    return render_template('index1.html',box=x)

@app.route('/play/<int:x>/<color>')
def play_color(x, color):
    return render_template('index2.html',box=x, color = color)


if __name__ == '__main__':
    app.run(debug=True,port=5000)