from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

dbname = os.getenv('dbname')
user=os.getenv('user')
password=os.getenv('password')
host =os.getenv('host')
port = os.getenv('port')

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}:{port}/{dbname}'
db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    name = db.Column(db.String)
    code = db.Column(db.String)
    price = db.Column(db.Float)
    discount = db.Column(db.Float)

@app.route('/products', methods=['POST'])
def create_product():
    data = request.json
    try:
        new_product = Product(
            id=data['id'], date=data['date'], name=data['name'],
            code=data['code'], price=data['price'], discount=data['discount']
        )
        db.session.add(new_product)
        db.session.commit()
        return jsonify({'message': 'Product created successfully'})
    except:
        db.session.rollback()
        return jsonify({'error': 'An error occurred while inserting data'})
    finally:
        db.session.close()

@app.route('/products/<product_id>', methods=['GET'])
def read_product(product_id):
    try:
        product = Product.query.get(product_id)
        if product:
            return jsonify({
                'id': product.id,
                'date': product.date,
                'name': product.name,
                'code': product.code,
                'price': product.price,
                'discount': product.discount
            })
        else:
            return jsonify({'message': 'Product not found'}), 404
    except:
        return jsonify({'error': 'An error occurred while fetching data'})

@app.route('/products/<product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    try:
        product = Product.query.get(product_id)
        if product:
            product.price = data['price']
            product.discount = data['discount']
            db.session.commit()
            return jsonify({'message': 'Product updated successfully'})
        else:
            return jsonify({'message': 'Product not found'}), 404
    except:
        db.session.rollback()
        return jsonify({'error': 'An error occurred while updating data'})
    finally:
        db.session.close()

@app.route('/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        product = Product.query.get(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()
            return jsonify({'message': 'Product deleted successfully'})
        else:
            return jsonify({'message': 'Product not found'}), 404
    except:
        db.session.rollback()
        return jsonify({'error': 'An error occurred while deleting data'})
    finally:
        db.session.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
