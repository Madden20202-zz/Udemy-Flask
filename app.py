from flask import Flask, request

# creates instance of the application
app = Flask(__name__)

# Let's learn how to query
# a string
@app.route('/query')
def get_string():
    # this sets up the start of the request
    if request.args:
        # defines variable so the arguments can be set up
        req=request.args
        # so to get anything to happen, the url HAS to look like so:
        # /query? then the information, such as John Doe
        # so the ? starts where the string is being received
        return " ".join(f"{k} {v}" for k,v in req.items())

    # this is the return error 
    return "I made a Query but all I got was this lousy string"

if __name__ == '__main__':
    # changes in code will show without 
    # reloading everything
    app.run(debug=True)