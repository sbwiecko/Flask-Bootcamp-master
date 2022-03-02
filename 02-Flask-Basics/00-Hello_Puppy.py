from flask import Flask
app = Flask(__name__) # Flask application object with the name of the
                      # module passed to the Flask object --> starting point

@app.route('/') # route to homepage and return the decorate function
def index(): # creation of a webpage with HTML code returned as a string
    return '<h1>Hello Puppy!</h1>'

if __name__ == '__main__':
    app.run()
