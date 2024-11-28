from app.database.db_config import execute_query, fetch_one, fetch_all
from tkinter import messagebox
import datetime

# Function to add a new transaction
def add_transaction(customer_id, product_id, quantity, price, total_amount):
    """Adds a new transaction to the database."""
    transaction_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    query = """
        INSERT INTO transactions (customer_id, product_id, quantity, price, total_amount, transaction_date)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    params = (customer_id, product_id, quantity, price, total_amount, transaction_date)
    
    result = execute_query(query, params)
    if result:
        messagebox.showinfo("Transaction Added", "Transaction added successfully")
        return True
    else:
        messagebox.showerror("Transaction Error", "Failed to add transaction")
        return False

# Function to get a transaction by ID
def get_transaction_by_id(transaction_id):
    """Fetches transaction details based on transaction ID."""
    query = "SELECT * FROM transactions WHERE id = %s"
    params = (transaction_id,)
    
    result = fetch_one(query, params)
    if result:
        return result  # Return transaction data if found
    else:
        messagebox.showerror("Transaction Not Found", "Transaction not found")
        return None

# Function to get all transactions
def get_all_transactions():
    """Fetches all transactions from the database."""
    query = "SELECT * FROM transactions"
    result = fetch_all(query)
    
    if result:
        return result
    else:
        return []

# Function to update a transaction
def update_transaction(transaction_id, customer_id, product_id, quantity, price, total_amount):
    """Updates transaction details in the database."""
    query = """
        UPDATE transactions 
        SET customer_id = %s, product_id = %s, quantity = %s, price = %s, total_amount = %s
        WHERE id = %s
    """
    params = (customer_id, product_id, quantity, price, total_amount, transaction_id)
    
    result = execute_query(query, params)
    if result:
        messagebox.showinfo("Update", "Transaction updated successfully")
        return True
    else:
        messagebox.showerror("Update Error", "Failed to update transaction")
        return False

# Function to delete a transaction
def delete_transaction(transaction_id):
    """Deletes a transaction from the database."""
    query = "DELETE FROM transactions WHERE id = %s"
    params = (transaction_id,)
    
    result = execute_query(query, params)
    if result:
        messagebox.showinfo("Delete", "Transaction deleted successfully")
        return True
    else:
        messagebox.showerror("Delete Error", "Failed to delete transaction")
        return False

# Function to get transactions by customer ID
def get_transactions_by_customer(customer_id):
    """Fetches all transactions for a specific customer."""
    query = "SELECT * FROM transactions WHERE customer_id = %s"
    params = (customer_id,)
    
    result = fetch_all(query, params)
    if result:
        return result
    else:
        return []

# Function to get transactions by date range
def get_transactions_by_date(start_date, end_date):
    """Fetches transactions within a specific date range."""
    query = "SELECT * FROM transactions WHERE transaction_date BETWEEN %s AND %s"
    params = (start_date, end_date)
    
    result = fetch_all(query, params)
    if result:
        return result
    else:
        return []
s