from flask import Flask # Import the Flask class from the flask module

# Create an instance of Flask called app which will be the central object
app = Flask(__name__) 

# We can now start defining our routes 

# @app.route("/") - @app is the decorator.route('this is a url')
# this goes right above the function you want to decorate 

@app.route("/")
def index():
    return 'Hello World!!!'

@app.route('/test')
def test():

    my_dicts = []
    for i in range(5):
        a_dict = {
            'id': i+1,
            'key' : 'value',
            'name' : 'Brian'
    }
        my_dicts.append(a_dict)

    return my_dicts

## return my_dicts, 405 -> would change the status code to 405, can override/change status code on reqs 