from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 1299.99},
    {"id": 2, "name": "Mouse", "price": 29.99},
    {"id": 3, "name": "Keyboard", "price": 89.99},
]

@app.route("/products")
def get_products():
    return jsonify({"service": "ProductService", "data": products})

@app.route("/health")
def health():
    return jsonify({"status": "OK", "service": "ProductService"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3002)