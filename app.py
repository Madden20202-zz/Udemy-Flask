from flask import Flask, render_template
# still need to import file

# creates instance of the application
app = Flask(__name__)

# Let's learn how to query
# a string

if __name__ == '__main__':
    # changes in code will show without 
    # reloading everything
    app.run(debug=True)