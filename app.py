from flask import Flask # Import the Flask class from the flask module

# Create an instance of Flask called app which will be the central object
app = Flask(__name__) 

# We can now start defining our routes 

# @app.route("/") - @app is the decorator.route('this is a url')
# this goes right above the function you want to decorate 

@app.route("/")
def index():
    return 'Hello World!!!'

