from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# Function to format dates in a consistent format (e.g., DD/MM/YYYY)
def format_date(date_obj):
    """Formats a date object into a string of format DD/MM/YYYY."""
    if isinstance(date_obj, datetime):
        return date_obj.strftime("%d/%m/%Y")
    else:
        messagebox.showerror("Date Format Error", "Invalid date object passed.")
        return None

# Function to show an error message in a popup
def show_error_message(message, title="Error"):
    """Displays an error message in a popup."""
    messagebox.showerror(title, message)

# Function to show a success message in a popup
def show_success_message(message, title="Success"):
    """Displays a success message in a popup."""
    messagebox.showinfo(title, message)

# Function to validate if a string is a valid number
def is_valid_number(value):
    """Validates if a string can be converted to a float."""
    try:
        float(value)
        return True
    except ValueError:
        return False

# Function to validate if a string is a valid integer
def is_valid_integer(value):
    """Validates if a string can be converted to an integer."""
    try:
        int(value)
        return True
    except ValueError:
        return False

# Function to validate if a string is not empty
def is_not_empty(value):
    """Checks if a string is not empty."""
    return bool(value.strip())

# Function to convert a float or integer to a currency format
def format_currency(amount):
    """Formats a number into currency format (e.g., 1234.56 becomes '₹1,234.56')."""
    try:
        return f"₹{amount:,.2f}"
    except Exception as e:
        show_error_message(f"Error formatting currency: {str(e)}")
        return None

# Function to generate a unique transaction ID
def generate_transaction_id():
    """Generates a unique transaction ID based on the current timestamp."""
    return datetime.now().strftime("%Y%m%d%H%M%S")
