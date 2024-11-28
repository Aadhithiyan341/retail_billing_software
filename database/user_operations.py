from app.database.db_config import execute_query, fetch_one, fetch_all
from tkinter import messagebox

# Function to register a new biller (user)
def register_user(username, password, role):
    """Registers a new user in the database."""
    query = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
    params = (username, password, role)
    
    # Execute the query
    result = execute_query(query, params)
    if result:
        messagebox.showinfo("Registration", "User registered successfully")
        return True
    else:
        messagebox.showerror("Registration Error", "Failed to register user")
        return False

# Function to validate user login
def validate_user(username, password):
    """Validates user login credentials."""
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    params = (username, password)
    
    result = fetch_one(query, params)
    if result:
        return result  # Return user data if login is successful
    else:
        messagebox.showerror("Login Error", "Invalid username or password")
        return None

# Function to get all users (for admin purposes)
def get_all_users():
    """Fetches all users from the database."""
    query = "SELECT * FROM users"
    result = fetch_all(query)
    
    if result:
        return result
    else:
        return []

# Function to update user details (e.g., role)
def update_user(user_id, username, password, role):
    """Updates user details in the database."""
    query = "UPDATE users SET username = %s, password = %s, role = %s WHERE id = %s"
    params = (username, password, role, user_id)
    
    result = execute_query(query, params)
    if result:
        messagebox.showinfo("Update", "User details updated successfully")
        return True
    else:
        messagebox.showerror("Update Error", "Failed to update user details")
        return False

# Function to delete a user
def delete_user(user_id):
    """Deletes a user from the database."""
    query = "DELETE FROM users WHERE id = %s"
    params = (user_id,)
    
    result = execute_query(query, params)
    if result:
        messagebox.showinfo("Delete", "User deleted successfully")
        return True
    else:
        messagebox.showerror("Delete Error", "Failed to delete user")
        return False
