from flask import Flask, request, render_template

app = Flask(__name__)

def calculate_iva(price, iva_rate=0.16):
    iva = price * iva_rate
    total = price + iva
    return iva, total

@app.route('/', methods=['GET', 'POST'])
def index():
    products = []
    if request.method == 'POST':
        input_text = request.form['input_text']
        lines = input_text.split('\n')
        for line in lines:
            parts = line.split()
            if len(parts) >= 2:
                product_name = parts[0]
                try:
                    price = float(parts[1])
                except ValueError:
                    continue  # Skip if price is not a valid float
                iva, total = calculate_iva(price)
                product = {
                    'product': product_name,
                    'price': f"{price:.2f}",
                    'iva': f"{iva:.2f}",
                    'total': f"{total:.2f}"
                }
                products.append(product)

    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
