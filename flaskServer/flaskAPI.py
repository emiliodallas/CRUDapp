from flask import Flask, request, jsonify  # Import necessary modules
from dotenv import load_dotenv
import psycopg2
import os


load_dotenv()

# Database connection details
db_params = {
    'dbname':os.getenv('dbname'),
    'user':os.getenv('user'),
    'password':os.getenv('password'),
    'host':os.getenv('host')
}

app = Flask(__name__)  # Create a Flask app instance

# Define a route to create a new product
@app.route('/products', methods=['POST'])
def createProduct_page():
    data = request.json
    connection = None  # Initialize connection outside the try block
    try:
        connection = psycopg2.connect(**db_params)  # Establish a database connection
        cursor = connection.cursor()  # Create a cursor object for executing SQL queries

        # SQL query to insert product data into the database
        query = '''
            INSERT INTO CRUD.products (id, date, name, code, price, discount)
            VALUES (%s, %s, %s, %s, %s, %s)
        '''
        values = (
            data['id'], data['date'], data['name'],
            data['code'], data['price'], data['discount']
        )
        cursor.execute(query, values)  # Execute the query
        connection.commit()  # Commit changes to the database
        return jsonify({'message': 'Product created successfully'})  # Return success message
    except psycopg2.Error as e:
        return jsonify({'error': 'An error occurred while inserting data'})  # Handle database errors
    finally:
        if connection is not None:
            cursor.close()  # Close the cursor
            connection.close()  # Close the database connection

# Define a route to get product details by ID
@app.route('/products/<product_id>', methods=['GET'])
def readProduct_page(product_id):
    connection = None  # Initialize connection outside the try block
    try:
        connection = psycopg2.connect(**db_params)  # Establish a database connection
        cursor = connection.cursor()  # Create a cursor object for executing SQL queries
        cursor.execute('SELECT * FROM crud.products WHERE id = %s', (product_id,))
        product = cursor.fetchone()  # Fetch the product details
        if product:
            return jsonify({
                'id': product[0],
                'date': product[3],
                'name': product[2],
                'code': product[1],
                'price': product[4],
                'discount': product[5]
            })  # Return the product details as JSON
        else:
            return jsonify({'message': 'Product not found'}), 404  # Return a 404 error if product is not found
    finally:
        if connection is not None:
            cursor.close()  # Close the cursor
            connection.close()  # Close the database connection

# Define a route to update product details by ID
@app.route('/products/<product_id>', methods=['PUT'])
def updateProduct_page(product_id):
    data = request.json
    connection = None  # Initialize connection outside the try block
    try:
        connection = psycopg2.connect(**db_params)  # Establish a database connection
        cursor = connection.cursor()  # Create a cursor object for executing SQL queries
        cursor.execute('''
            UPDATE crud.products
            SET price = %s, discount = %s
            WHERE id = %s
        ''', (data['price'], data['discount'], product_id))  # Update product details
        connection.commit()  # Commit changes to the database
        return jsonify({'message': 'Product updated successfully'})  # Return success message
    finally:
        if connection is not None:
            cursor.close()  # Close the cursor
            connection.close()  # Close the database connection

# Define a route to delete a product by ID
@app.route('/products/<product_id>', methods=['DELETE'])
def deleteProduct_page(product_id):
    connection = None  # Initialize connection outside the try block
    try:
        connection = psycopg2.connect(**db_params)  # Establish a database connection
        cursor = connection.cursor()  # Create a cursor object for executing SQL queries
        cursor.execute('DELETE FROM crud.products WHERE id = %s', (product_id,))
        connection.commit()  # Commit changes to the database
        return jsonify({'message': 'Product deleted successfully'})  # Return success message
    finally:
        if connection is not None:
            cursor.close()  # Close the cursor
            connection.close()  # Close the database connection

# Run the Flask app if this script is executed directly
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
