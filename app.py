import os
import africastalking
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

username = "sandbox"
api_key = "2ecd71cd5457bd92c1ba4d33a69939453545c5bb590fb4a3c4641e393c23bdf9"

africastalking.initialize(username, api_key)

pay = africastalking.Payment
sms = africastalking.SMS

@app.route("/", methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/checkout", methods=["GET","POST"])
def check_out():
    
    if request.method == "POST":
        global phone_number
        product_name = "DUKA"
        phone_number = request.form["phoneNumber"]
        currency_code = "KES"
        amount = 250

        try:
            response = pay.mobile_checkout(product_name, phone_number,currency_code, amount)
            print(response)
        except Exception as e:
            print(e)
        

    return render_template("checkout.html")

@app.route("/paymentnotification", methods=["POST"])
def payment_notification():
    print(request.status)

    if request.status is "Success":
        sms.send(
            "Thank you for shopping with us! Your payment has been confirmed",
            [phone_number]
        )
    else:
        print("An error occured")



if __name__ == "__main__":
    app.run(debug=True)