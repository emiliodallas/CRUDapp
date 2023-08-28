import streamlit as st
from datetime import datetime
import requests

# Streamlit configuration
st.set_page_config(page_title="Simple CRUD App", page_icon="📝")

# Base URL for the CRUD API
base_url = "http://flaskserver:5000"

# Function to create a new product
def newProduct():
    st.title("Create Product")
    product_id = st.text_input("Product ID:")
    product_name = st.text_input("Product Name:")
    product_code = st.text_input("Product Code:")
    price = st.text_input("Product Price:")
    discount = st.text_input("Product Discount:")
    
    if st.button("Create"):
        if product_name and product_code:
            current_date = datetime.now().strftime("%Y-%m-%d")
            data = {
                "id": product_id, 
                "date": current_date,
                "name": product_name,
                "code": product_code,
                "price": price,
                "discount": discount
            }
            response = requests.post(f"{base_url}/products", json=data)
            st.write(response.json())

# Function to read a product
def readProduct():
    st.title("Read Product")
    product_id = st.text_input("Product Id:")
    if st.button("Read"):
        if product_id:
            response = requests.get(f"{base_url}/products/{product_id}")
            st.write(response.json())

# Function to update a product
def updateProduct():
    st.title("Update Product")
    product_code = st.text_input("Product Code:")
    product_price = st.text_input("New Product Price:")
    product_discount = st.text_input("New Product Discount:")
    
    if st.button("Update"):
        if product_code and product_price and product_discount:
            data = {
                "price": product_price,
                "discount": product_discount
            }
            response = requests.put(f"{base_url}/products/{product_code}", json=data)
            st.write(response.json())

# Function to delete a product
def deleteProduct():
    st.title("Delete Product")
    product_id = st.text_input("Product Id to Delete:")
    
    if st.button("Delete"):
        if product_id:
            response = requests.delete(f"{base_url}/products/{product_id}")
            st.write(response.json())

# Main app logic
def main():
    st.title("Simple CRUD App")
    selected_operation = st.sidebar.radio("Select Operation", ["Create", "Read", "Update", "Delete"])

    if selected_operation == "Create":
        newProduct()
    elif selected_operation == "Read":
        readProduct()
    elif selected_operation == "Update":
        updateProduct()
    elif selected_operation == "Delete":
        deleteProduct()

if __name__ == "__main__":
    main()
