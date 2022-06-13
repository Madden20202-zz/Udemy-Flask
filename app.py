from flask import Flask, request

# creates instance of the application
app = Flask(__name__)

# Let's learn about GET requests

if __name__ == '__main__':
    # changes in code will show without 
    # reloading everything
    app.run(debug=True)