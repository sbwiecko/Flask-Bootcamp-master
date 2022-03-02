from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Puppy!</h1>'

@app.route('/information')
def info():
    return '<h1>Puppies are cute!</h1>'

@app.route('/puppy/<name>')
def puppy(name):
    # Page for an individual puppy.
    # return f"<h1>This is a page for {name}</h1>"

    return f"100th letter: {name[100]}"

if __name__ == '__main__':
    # Never have debug=True for production apps!
    # Help catching errors
    # + access to a console in the browser
    # use the Debugger PIN provided at the starting of the app

    # e.g., generate an error with
    # `return f"100th letter: {name[100]}"`
    app.run(debug=True)
