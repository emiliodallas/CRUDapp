from flask import Flask, request, jsonify
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True)
    code : Mapped[int]
    name: Mapped[str] = mapped_column(String(30))
    date : Mapped[str]
    price : Mapped[float]
    discount : Mapped[float]

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, code={self.code!r}, name={self.name!r})"

load_dotenv()

dbname = os.getenv('dbname')
user=os.getenv('user')
password=os.getenv('password')
host =os.getenv('host')
port = os.getenv('port')

# Configure the database connection
db_url = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}'
engine = create_engine(db_url, echo=True)

# Create products table according to schema on Product class
Base.metadata.create_all(engine)

#Open query session
session = Session(engine)

app = Flask(__name__)
@app.route('/products', methods=['POST'])
def create_product():
    data = request.json
    try:
        new_product = Product(
            id=data['id'], code=data['code'], name=data['name'],
            date=data['date'], price=data['price'], discount=data['discount']
        )
        session.add(new_product)
        session.commit()
        return jsonify({'message': 'Product created successfully'})
    except:
        raise Exception('An error occurred while inserting data')

@app.route('/products/<product_id>', methods=['GET'])
def read_product(product_id):
    try:
        product = session.get(Product, product_id)
        if product:
            return jsonify({
                'id': product.id,
                'code': product.code,
                'name': product.name,
                'price': product.price,
                'discount': product.discount,
                'date': product.date
            })
        else:
            return jsonify({'message': 'Product not found'}), 404
    except:
        raise Exception('An error occurred while fetching data')
    
@app.route('/products/<product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    try:
        product = session.get(Product, product_id)
        if product:
            product.price = data['price']
            product.discount = data['discount']
            session.commit()
            return jsonify({'message': 'Product updated successfully'})
        else:
            return jsonify({'message': 'Product not found'}), 404
    except:
        raise Exception('An error occurred while updating data')

@app.route('/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        product = session.get(Product, product_id)
        if product:
            session.delete(product)
            session.commit()
            return jsonify({'message': 'Product deleted successfully'})
        else:
            return jsonify({'message': 'Product not found'}), 404
    except:
        raise Exception('An error occurred while deleting data')
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)