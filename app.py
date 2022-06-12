from flask import Flask

# creates instance of the application
app = Flask(__name__)

# this is a decorator that shows the
# url for this specific app

# all routes need their own unique url
@app.route('/')

# Function that will be ran once 
# the url is called
def hello_world():
    return "Hello World!"

if __name__ == '__main__':
    app.run()