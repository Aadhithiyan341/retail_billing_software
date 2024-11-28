from app.database.db_config import execute_query, fetch_one, fetch_all
from tkinter import messagebox

# Function to add a new product
def add_product(name, description, price, stock_quantity):
    """Adds a new product to the database."""
    query = """
        INSERT INTO products (name, description, price, stock_quantity)
        VALUES (%s, %s, %s, %s)
    """
    params = (name, description, price, stock_quantity)
    
    result = execute_query(query, params)
    if result:
        messagebox.showinfo("Product Added", "Product added successfully")
        return True
    else:
        messagebox.showerror("Product Error", "Failed to add product")
        return False

# Function to get a product by ID
def get_product_by_id(product_id):
    """Fetches product details based on product ID."""
    query = "SELECT * FROM products WHERE id = %s"
    params = (product_id,)
    
    result = fetch_one(query, params)
    if result:
        return result  # Return product data if found
    else:
        messagebox.showerror("Product Not Found", "Product not found")
        return None

# Function to get all products
def get_all_products():
    """Fetches all products from the database."""
    query = "SELECT * FROM products"
    result = fetch_all(query)
    
    if result:
        return result
    else:
        return []

# Function to update a product
def update_product(product_id, name, description, price, stock_quantity):
    """Updates product details in the database."""
    query = """
        UPDATE products 
        SET name = %s, description = %s, price = %s, stock_quantity = %s
        WHERE id = %s
    """
    params = (name, description, price, stock_quantity, product_id)
    
    result = execute_query(query, params)
    if result:
        messagebox.showinfo("Update", "Product updated successfully")
        return True
    else:
        messagebox.showerror("Update Error", "Failed to update product")
        return False

# Function to delete a product
def delete_product(product_id):
    """Deletes a product from the database."""
    query = "DELETE FROM products WHERE id = %s"
    params = (product_id,)
    
    result = execute_query(query, params)
    if result:
        messagebox.showinfo("Delete", "Product deleted successfully")
        return True
    else:
        messagebox.showerror("Delete Error", "Failed to delete product")
        return False

# Function to search products by name
def search_product_by_name(name):
    """Fetches products by name."""
    query = "SELECT * FROM products WHERE name LIKE %s"
    params = ('%' + name + '%',)
    
    result = fetch_all(query, params)
    if result:
        return result
    else:
        return []

