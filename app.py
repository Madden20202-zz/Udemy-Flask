from flask import Flask, make_response, jsonify

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
        # most collections come as key value pairs
        "size": "small",
        "toppings": "cheese",
        "crust": "deep dish"

    }

}

# now lets display this
@app.route('/orders')
def display_order():
    # retrieves the order collection and then 
    # serializes it and then is displayed

    # this also returns a 200 code to show a success
    response = make_response(jsonify(order), 200)
    # this response is now given all of the information needed
    return response

if __name__ == '__main__':
    # changes in code will show without 
    # reloading everything
    app.run(debug=True)