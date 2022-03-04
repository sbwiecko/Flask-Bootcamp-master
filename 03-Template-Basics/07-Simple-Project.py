from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("07-My_Simple-Project-INDEX.html")

@app.route('/report')
def report():
    username = request.args.get('username')

    # we first initiate an empty list of unmet requirements
    requirements = []

    # we check all three requirement one-by-one on the username
    if not any(char.isupper() for char in username):
        requirements.append("You didn't use an uppercase letter")

    if not any(char.islower() for char in username):
        requirements.append("You didn't use a lowercase letter")

    if not username[-1].isdigit():
        requirements.append("You didn't use a number")

    # if the requirements is empty, then username is passed
    passed = not requirements

    # we send the `passed` status along with 
    # the list of unmet requirements
    return render_template(
        "07-My_Simple-Project-REPORT.html",
        username=username,
        passed=passed,
        requirements=requirements
    )

if __name__ == '__main__':
    app.run(debug=True)