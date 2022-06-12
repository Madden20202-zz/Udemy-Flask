from flask import Flask, render_template
# still need to import file

# creates instance of the application
app = Flask(__name__)

# all routes need their own unique url
# lets practice
@app.route('/')
def hello_world():
    return "Hello World!"

# routes can also point to files within the app
# making it effective on its own if need be
@app.route('/html')
def get_html_page():
    return render_template('web-page.html')

if __name__ == '__main__':
    # changes in code will show without 
    # reloading everything
    app.run(debug=True)