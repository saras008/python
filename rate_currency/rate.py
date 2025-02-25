
from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    converted_amount = None
    if request.method == 'POST':
        amount = float(request.form['amount'])
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']

        api_key = 'fca_live_0mxqTZxp4daZGGreDQ3tkomWIyGWBsGLKyEY0FNQ'  # Replace with your actual freecurrencyapi key
        url = f'https://api.freecurrencyapi.com/v1/latest?apikey={api_key}&currencies={from_currency},{to_currency}'

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(data)  # Print only the data from the response
            if 'data' in data:
                from_rate = data['data'][from_currency]
                to_rate = data['data'][to_currency]
                conversion_rate = to_rate / from_rate
                converted_amount = amount * conversion_rate

        return render_template('index.html', converted_amount=converted_amount, from_currency=from_currency, to_currency=to_currency)

if __name__ == '__main__':
    app.run(debug=True)

