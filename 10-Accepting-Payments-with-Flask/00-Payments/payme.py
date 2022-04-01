import os
# see more details on https://stripe.com/docs/legacy-checkout/flask
from flask import Flask, render_template, request, redirect, url_for
# pip import stripe
import stripe


app = Flask(__name__)


# example keys below; often keys are set as ENV variables
# stripe_keys = { 'secret_key': os.environ['SECRET_KEY']; 'publishable_key': os.environ['PUBLISHABLE_KEY']}

stripe.api_key = "sk_test_BQokikJOvBiI2HlWgH4olfQ2" # test mode, use the card number 4242 4242 4242 4242
public_key = 'pk_test_6pRNASCoBOKtIshFeQd4XMUh'


@app.route('/')
def index():
    return render_template('index.html', public_key=public_key)


@app.route('/payment', methods=['POST'])
def payment():
    # CUSTOMER INFORMATION
    customer = stripe.Customer.create(
        email=request.form['stripeEmail'],
        source=request.form['stripeToken']
    )

    # CHARGE/PAYMENT INFORMATION
    charge = stripe.Charge.create(
        customer=customer.id,
        amount=1999,
        currency='usd',
        description='Donation'
    )

    return render_template("thankyou.html")


if __name__ == '__main__':
    app.run(debug=True)
