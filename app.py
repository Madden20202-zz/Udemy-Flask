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


# Now HTTP Post will create new data, 
# and more importantly, collections

# the default is get, all others must be stated
@app.route('/orders', methods=["POST"])
def make_new_order(orderid): # time to make a new one
    req = request.get_json()
    if orderid in order:
        response = make_response(jsonify({"Error: that order could not be processed"}), 400)


@app.route('/orders')
def display_order():
    response = make_response(jsonify(order), 200)
    return response

if __name__ == '__main__':
    # changes in code will show without 
    # reloading everything
    app.run(debug=True)