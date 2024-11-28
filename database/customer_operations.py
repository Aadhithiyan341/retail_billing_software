from app.database.db_config import execute_query, fetch_one, fetch_all
from tkinter import messagebox

# Function to add a new customer
def add_customer(name, contact, email, address):
    """Adds a new customer to the database."""
    query = "INSERT INTO customers (name, contact, email, address) VALUES (%s, %s, %s, %s)"
    params = (name, contact, email, address)
    
    # Execute the query
    result = execute_query(query, params)
    if result:
        messagebox.showinfo("Customer Added", "Customer added successfully")
        return True
    else:
        messagebox.showerror("Add Customer Error", "Failed to add customer")
        return False

# Function to get customer by ID
def get_customer_by_id(customer_id):
    """Fetches customer details based on customer ID."""
    query = "SELECT * FROM customers WHERE id = %s"
    params = (customer_id,)
    
    result = fetch_one(query, params)
    if result:
        return result  # Return customer data if found
    else:
        messagebox.showerror("Customer Not Found", "Customer not found")
        return None

# Function to get all customers
def get_all_customers():
    """Fetches all customers from the database."""
    query = "SELECT * FROM customers"
    result = fetch_all(query)
    
    if result:
        return result
    else:
        return []

# Function to update customer details
def update_customer(customer_id, name, contact, email, address):
    """Updates customer details in the database."""
    query = "UPDATE customers SET name = %s, contact = %s, email = %s, address = %s WHERE id = %s"
    params = (name, contact, email, address, customer_id)
    
    result = execute_query(query, params)
    if result:
        messagebox.showinfo("Update", "Customer details updated successfully")
        return True
    else:
        messagebox.showerror("Update Error", "Failed to update customer details")
        return False

# Function to delete a customer
def delete_customer(customer_id):
    """Deletes a customer from the database."""
    query = "DELETE FROM customers WHERE id = %s"
    params = (customer_id,)
    
    result = execute_query(query, params)
    if result:
        messagebox.showinfo("Delete", "Customer deleted successfully")
        return True
    else:
        messagebox.showerror("Delete Error", "Failed to delete customer")
        return False
