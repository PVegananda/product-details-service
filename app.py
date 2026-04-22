from flask import Flask, jsonify
import os

app = Flask(__name__)

# Sample product data
PRODUCTS = {
    "1": {"id": "1", "name": "Laptop", "price": 999.99, "category": "Electronics"},
    "2": {"id": "2", "name": "Phone", "price": 599.99, "category": "Electronics"},
    "3": {"id": "3", "name": "Tablet", "price": 399.99, "category": "Electronics"},
}

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "Product Details Service is running"}), 200

@app.route('/products', methods=['GET'])
def get_all_products():
    return jsonify(list(PRODUCTS.values())), 200

@app.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    product = PRODUCTS.get(product_id)
    if product:
        return jsonify(product), 200
    return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)
