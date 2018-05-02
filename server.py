from flask import Flask, request
import werkzeug.exceptions
from price_calculator import *
import json

app = Flask(__name__)

@app.route("/calculate_price/<int:district>/<int:squaremeters>")
def calculate_price(district, squaremeters):
    try:
        result = json.dumps({'price': PriceCalculator.calculate(district, squaremeters)})
    except ValueError as e:
        result = (json.dumps({'error': str(e)}), 400)
    return result


if __name__ == "__main__":
    app.run()