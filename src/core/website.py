import flask

app = flask.Flask(__name__)

@app.route("/")
def getHome():
    return "Welcome!\nThis is the home page."


if __name__ == '__main__':
    # This only runs if you type 'python app.py'
    app.run(port=3000)