import flask

app = flask.Flask(__name__)

@app.route("/")
def getHome():
    return "Welcome!\nThis is the home page."

@app.route("/Urish")
def getUrishJob():
    return "Manager"

@app.route("/Nomad")
def getNomadJob():
    return "Selenium"

@app.route("/Hugh")
def getHughJob():
    return "Market"

@app.route("/Carl")
def getCarlJob():
    return "Core"



if __name__ == '__main__':
    # This only runs if you type 'python app.py'
    app.run(port=3000)