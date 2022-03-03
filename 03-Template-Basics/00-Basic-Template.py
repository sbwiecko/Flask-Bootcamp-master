from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # Connecting to a template (html file)
    # directory `template` needs to be at the same level as the python file
    return render_template('00-Basic-Template.html')

    # see also how the HTML template file points to a source in the `static` directory

if __name__ == '__main__':
    app.run(debug=True)
