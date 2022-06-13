from flask import Flask, make_response, jsonify

# creates instance of the application
app = Flask(__name__)

order = {
    # name of the first order
    "order1": {
        # most collections come as key value pairs
        "size": "small",
        "toppings": "cheese",
        "crust": "deep dish"

    }

}

@app.route('/orders')
def display_order():
    response = make_response(jsonify(order), 200)
    return response

# Now HTTP Post will create new data, 
# and more importantly, collections


if __name__ == '__main__':
    # changes in code will show without 
    # reloading everything
    app.run(debug=True)