from flask import Flask

# main variable to use 
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello There"

@app.route("/ping")
def anything():
    return {"Message": "Pong!"}


@app.route("/ping",methods = ['POST'])
def ping_post():
    return {"Message": "Pong from POST!"}