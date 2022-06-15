from flask import Flask, make_response, jsonify, request

# creates instance of the application
app = Flask(__name__)

order = {
    # name of the first order
    "order1": {
        # most collections come as key value pairs

        # in postman this must be present, 
        # empty JSON files will create errors
        "size": "small",
        "toppings": "cheese",
        "crust": "deep dish"
    }
}


# Now HTTP Post will create new data, 
# and more importantly, collections

# the default is get, all others must be stated
@app.route('/orders/<orderid>', methods=["POST"])
def make_new_order(orderid): # time to make a new one

    # create a request that can 
    # get the info needed
    req = request.get_json()
    if orderid in order:
        response = make_response(jsonify({"Error: that order could not be processed"}), 400)
    else:
        # gives the order a number and then makes a json 
        # response to tell the user it has been added
        order.update({orderid:req})
        response =  make_response(jsonify({"message": "A new order is made"}), 200)
        return response

# Now let's learn POST
# POST allows the user to update certain data
# in this case, it is their pizza order

@app.route('/orders')
def display_order():
    response = make_response(jsonify(order), 200)
    return response

if __name__ == '__main__':
    # changes in code will show without 
    # reloading everything
    app.run(debug=True, host='localhost')