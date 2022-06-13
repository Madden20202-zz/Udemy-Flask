from flask import Flask, request

# creates instance of the application
app = Flask(__name__)

# Let's learn about GET requests
# First, GET needs a collection where 
# it can "get" the data needed

# let's use a pizza shop as an example

# name of order
order = {
    # name of the first order
    "order1": {

    }

}

if __name__ == '__main__':
    # changes in code will show without 
    # reloading everything
    app.run(debug=True)