from flask import Flask
app = Flask(__name__)

@app.route('/') # e.g., 127.0.0.1:5000
def index():
    return '<h1>Hello Puppy!</h1>'

@app.route('/information') # e.g., 127.0.0.1:5000/information
def info():
    return '<h2>Puppies are cute!</h2>'

if __name__ == '__main__':
    app.run()
