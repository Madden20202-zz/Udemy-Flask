from flask import Flask

# creates instance of the application
app = Flask(__name__)

# all routes need their own unique url
# lets practice
@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/tutorial')
def tutmessage():
    return 'I am a basic tutorial on routes and end points'

if __name__ == '__main__':
    # changes in code will show without 
    # reloading everything
    app.run(debug=True)