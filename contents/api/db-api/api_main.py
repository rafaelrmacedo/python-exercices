from flask import Flask, request, jsonify
from db_functions import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="*")

# Exercises table endpoints
@app.route('/produto', methods=['GET'])
def get_products():
    products = getProducts()
    return jsonify(products)

@app.route('/produto', methods=['POST'])
def add_product():
    new_product = request.json
    insertProduct(new_product)
    return jsonify({'message': 'Product inserted!'}), 201

@app.route('/produto/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    updated_product = request.json
    updateProduct(updated_product, product_id)
    return jsonify({'message': 'Product updated!'}), 200

@app.route('/produto/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    deleteProduct(product_id)
    return jsonify({'message': 'Product deleted'}), 200

@app.route('/produtosSemEstoque', methods=['GET'])
def get_products_without_stock():
    connection = getConnection()
    cursor = connection.cursor(dictionary=True)
    sql = "SELECT * FROM produto WHERE estoque = 0"
    cursor.execute(sql)
    products = cursor.fetchall()
    return jsonify(products)

@app.route('/produtosComEstoqueBaixo', methods=['GET'])
def get_products_with_low_stock():
    connection = getConnection()
    cursor = connection.cursor(dictionary=True)
    sql = "SELECT * FROM produto WHERE estoque < 10"
    cursor.execute(sql)
    products = cursor.fetchall()
    return jsonify(products)

@app.route('/produtosComEstoqueInferior/<int:quantidade>', methods=['GET'])
def get_products_with_stock_less_or_equal(quantidade):
    connection = getConnection()
    cursor = connection.cursor(dictionary=True)
    sql = "SELECT * FROM produto WHERE estoque <= %s"
    cursor.execute(sql, [quantidade])
    products = cursor.fetchall()
    return jsonify(products)

@app.route('/produtosComEstoqueSuperior/<int:quantidade>', methods=['GET'])
def get_products_with_stock_higher(quantidade):
    connection = getConnection()
    cursor = connection.cursor(dictionary=True)
    sql = "SELECT * FROM produto WHERE estoque > %s"
    cursor.execute(sql, [quantidade])
    products = cursor.fetchall()
    return jsonify(products)

@app.route('/produtosPorCategoria/<string:categoria>', methods=['GET'])
def get_products_by_category(categoria):
    products = getProductsByCategory(categoria)
    return jsonify(products)

# SQL for new table 
#   CREATE TABLE movies (
#       id INT AUTO_INCREMENT PRIMARY KEY,
#       name VARCHAR(255),
#       year INT
#   );

# New table endpoints
@app.route('/movies', methods=['GET'])
def getMovies():
    connection = getConnection()
    cursor = connection.cursor(dictionary=True)
    sql = "SELECT * FROM movies"
    cursor.execute(sql)
    movies = cursor.fetchall()
    return movies

@app.route('/movies', methods=['POST'])
def addMovie(movie):
    connection = getConnection()
    cursor = connection.cursor()
    sql = "INSERT INTO movies (name, year) VALUES (%s, %s)"
    cursor.execute(sql, [movie["name"], movie["year"]])
    connection.commit()
    connection.close()

@app.route('/movies/<int:id>', methods=['PUT'])
def updateMovie(movie, id):
    connection = getConnection()
    cursor = connection.cursor()
    sql = "UPDATE movies SET name = %s, year = %s WHERE id = %s"
    cursor.execute(sql, [movie["name"], movie["year"], id])
    connection.commit()
    connection.close()

@app.route('/movies/<int:id>', methods=['DELETE'])
def deleteMovie(id):
    connection = getConnection()
    cursor = connection.cursor()
    sql = "DELETE FROM movies WHERE id = %s"
    cursor.execute(sql, [id])
    connection.commit()
    connection.close()


if __name__ == '__main__':
    app.run()