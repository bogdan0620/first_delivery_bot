import sqlite3

connection = sqlite3.connect('products.db')
sql = connection.cursor()

# sql.execute('CREATE TABLE products (product_name TEXT, cost REAL, description TEXT, photo BLOB);')

def add_product(product_name, cost, description, photo):
    connection = sqlite3.connect('products.db')
    sql = connection.cursor()

    sql.execute('INSERT INTO products VALUES (?, ?, ?, ?);' (str(product_name), cost, str(description), photo))

    connection.commit()

def get_product_name():
    connection = sqlite3.connect('products.db')
    sql = connection.cursor()

    product_names = sql.execute('SELECT product_name FROM products;')

    return product_names.fetchall()

def get_all_products():
    connection = sqlite3.connect('products.db')
    sql = connection.cursor()

    all_products = sql.execute('SELECT * FROM products;')

    return all_products.fetchall()