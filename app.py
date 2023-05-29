# -*- coding:utf-8 -*-
from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/getUserInfo')
def user():
    return {
        "code": "200",
        "msg": '获取成功',
        "name": '肖佳明',
        "age": 32
    }


@app.route('/getUserById',methods=['post'])
def user1():
    id = request.json['id']
    if id in [1, 40, 99]:
        return {
            "code": "500",
            "msg": '获取失败'
        }
    else:
        return {
            "code": "200",
            "msg": '获取成功',
            "name": '肖佳明',
            "age": 31,
            "id": id
        }


# 假设已经有一些商品数据
products = [
    {"id": 1, "name": "商品1", "price": 100},
    {"id": 2, "name": "商品2", "price": 200},
    {"id": 3, "name": "商品3", "price": 300},
]

# 获取所有商品列表
@app.route("/api/products")
def get_products():
    return jsonify(products)

# 根据 id 获取单个商品信息
@app.route("/api/products/<int:product_id>")
def get_product(product_id):
    for product in products:
        if product["id"] == product_id:
            return jsonify(product)
    # 如果找不到则返回 404 Not Found 错误
    return jsonify({"error": "Product not found"}), 404

# 添加新的商品
@app.route("/api/products", methods=["POST"])
def add_product():
    data = request.get_json()
    if not data or not data.get("name") or not data.get("price"):
        return jsonify({"error": "Invalid data"})
    new_id = max([product["id"] for product in products]) + 1
    new_product = {"id": new_id, "name": data["name"], "price": data["price"]}
    products.append(new_product)
    return jsonify(new_product)

# 修改一个商品的信息
@app.route("/api/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid data"})
    for product in products:
        if product["id"] == product_id:
            product.update(data)
            return jsonify(product)
    # 如果找不到则返回 404 Not Found 错误
    return jsonify({"error": "Product not found"}), 404

# 删除一个商品
@app.route("/api/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    for i, product in enumerate(products):
        if product["id"] == product_id:
            products.pop(i)
            return jsonify({"message": f"Product {product_id} has been deleted"})
    # 如果找不到则返回 404 Not Found 错误
    return jsonify({"error": "Product not found"}), 404




if __name__ == '__main__':
    app.run(host='0.0.0.0', port="5344")
