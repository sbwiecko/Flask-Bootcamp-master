#########
# puppy names into puppy latin:
# * if puppy name does not end in a y --> add a `y` to the name
# * if puppy name does end in a y --> replace it with `iful` instead
# using a specific route `/puppy_latin/<name>`
# it will take the name passed and display the puppy latin version on the page (dynamic route)

# Set up your imports here!
# import ...
from flask import Flask
app = Flask(__name__)

@app.route('/') # Fill this in!
def index():
    # Welcome Page
    # Create a generic welcome page.
    return """
    <h1>Welcome!</h1>
    <h2>Go to /puppy_latin/name to see your name in puppy latin.</h2>
    """

@app.route('/puppy_latin/<name>') # Fill this in!
def puppylatin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!
    return f"<h3>Hello {name[:-1]}iful !</h3>" if name.endswith('y') else f"<h3>Hello {name}y !</h3>"
    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"
    pass

if __name__ == '__main__':
    # Fill me in!
    app.run(debug=True)