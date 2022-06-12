from flask import Flask

# creates instance of the application
app = Flask(__name__)

# all routes need their own unique url
# lets practice
@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/tutorial')
# when making methods, if the names of methods are the
# same, then a 404 error code will appear, as they both 
# will negate each other
def tutmessage():
    return 'I am a basic tutorial on routes and end points'

if __name__ == '__main__':
    # changes in code will show without 
    # reloading everything
    app.run(debug=True)