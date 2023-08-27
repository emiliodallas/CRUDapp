from flask import Flask, request, jsonify
import psycopg2


# Database connection details
db_params = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "mysecretpassword",
    "host": "postgres"
}

app = Flask(__name__)

@app.route('/products', methods=['POST'])
def create_product():
    data = request.json
    connection = None  # Initialize connection outside the try block
    try:
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()
        query = '''
            INSERT INTO CRUD.products (id, date, name, code, price, discount)
            VALUES (%s, %s, %s, %s, %s, %s)
        '''
        values = (data['id'], data['date'], data['name'], data['code'], data['price'], data['discount'])
        cursor.execute(query, values)
        connection.commit()
        return jsonify({'message': 'Product created successfully'})
    except psycopg2.Error as e:
        return jsonify({'error': 'An error occurred while inserting data'})
    finally:
        if connection is not None:
            cursor.close()
            connection.close()

@app.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    connection = None  # Initialize connection outside the try block
    try:
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM crud.products WHERE id = %s', (product_id,))
        product = cursor.fetchone()
        if product:
            return jsonify({
                'id': product[0],
                'date': product[3],
                'name': product[2],
                'code': product[1],
                'price': product[4],
                'discount': product[5]
            })
        else:
            return jsonify({'message': 'Product not found'}), 404
    finally:
        if connection is not None:
            cursor.close()
            connection.close()

@app.route('/products/<product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    connection = None  # Initialize connection outside the try block
    try:
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()
        cursor.execute('''
            UPDATE crud.products
            SET price = %s, discount = %s
            WHERE id = %s
        ''', (data['price'], data['discount'], product_id))
        connection.commit()
        return jsonify({'message': 'Product updated successfully'})
    finally:
        if connection is not None:
            cursor.close()
            connection.close()

@app.route('/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    connection = None  # Initialize connection outside the try block
    try:
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()
        cursor.execute('DELETE FROM crud.products WHERE id = %s', (product_id,))
        connection.commit()
        return jsonify({'message': 'Product deleted successfully'})
    finally:
        if connection is not None:
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
