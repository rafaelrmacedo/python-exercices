import mysql.connector

def getConnection():
    connect = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'root',
            database = 'sistema'
    )
    return connect

def insertProduct(product):
    connection = getConnection()
    cursor = connection.cursor()
    sql = "INSERT INTO produto (descricao, estoque) VALUES (%s, %s)"
    cursor.execute(sql, [product["descricao"], product["estoque"]])
    connection.commit()
    connection.close()

def deleteProduct(id):
    connection = getConnection()
    cursor = connection.cursor()
    sql = "DELETE FROM produto WHERE id = %s"
    cursor.execute(sql, [id])
    connection.commit()
    connection.close()

def updateProduct(product, id):
    connection = getConnection()
    cursor = connection.cursor()
    sql = "UPDATE product SET descricao = %s, estoque = %s WHERE id = %s"
    cursor.execute(sql, [product["descricao"], product["estoque"], id])
    connection.commit()
    connection.close()

def getProducts():
    connection = getConnection()
    cursor = connection.cursor(dictionary=True)
    sql = "SELECT * FROM produto"
    cursor.execute(sql)
    products = cursor.fetchall()
    return products

def updateProductWithCategory(product, id, categoria):
    connection = getConnection()
    cursor = connection.cursor()
    sql = "UPDATE produto SET descricao = %s, estoque = %s, categoria = %s WHERE id = %s"
    cursor.execute(sql, [product["descricao"], product["estoque"], categoria, id])
    connection.commit()
    connection.close()

def getProductsByCategory(categoria):
    connection = getConnection()
    cursor = connection.cursor(dictionary=True)
    sql = "SELECT * FROM produto WHERE categoria = %s"
    cursor.execute(sql, [categoria])
    products = cursor.fetchall()
    return products

# New table database functions
def getMovie():
    connection = getConnection()
    cursor = connection.cursor(dictionary=True)
    sql = "SELECT * FROM movies"
    cursor.execute(sql)
    movies = cursor.fetchall()
    return movies

def addFilme(movie):
    connection = getConnection()
    cursor = connection.cursor()
    sql = "INSERT INTO movies (name, year) VALUES (%s, %s)"
    cursor.execute(sql, [movie["name"], movie["year"]])
    connection.commit()
    connection.close()

def updateFilme(movie, id):
    connection = getConnection()
    cursor = connection.cursor()
    sql = "UPDATE movies SET name = %s, year = %s WHERE id = %s"
    cursor.execute(sql, [movie["name"], movie["year"], id])
    connection.commit()
    connection.close()

def deleteFilme(id):
    connection = getConnection()
    cursor = connection.cursor()
    sql = "DELETE FROM movies WHERE id = %s"
    cursor.execute(sql, [id])
    connection.commit()
    connection.close()
