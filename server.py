from flask import Flask, request
import werkzeug.exceptions
from price_calculator import *
import json

app = Flask(__name__)

@app.route("/calculate_price/<int:district>/<int:squaremeters>")
def calculate_price(district, squaremeters):
    return json.dumps({'price': PriceCalculator.calculate(district, squaremeters)})


if __name__ == "__main__":
    app.run()