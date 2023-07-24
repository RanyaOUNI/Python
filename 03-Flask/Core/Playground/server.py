from flask import flask

app = Flask(__name__)

# http://localhost:5000/play
# localhost:5000/play/(x)

@app route('/')
def index():
    return "Hello From Flask"




if __name__ == '__main__':
    app.run()