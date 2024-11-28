import mysql.connector
from mysql.connector import Error
from tkinter import messagebox

# Database configuration
DB_HOST = 'localhost'      # Replace with your MySQL host
DB_USER = 'root'           # Replace with your MySQL user
DB_PASSWORD = ''           # Replace with your MySQL password
DB_DATABASE = 'retail_billing'  # Replace with your database name

def create_connection():
    """Establishes a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_DATABASE
        )
        if connection.is_connected():
            print("Successfully connected to the database")
            return connection
    except Error as e:
        messagebox.showerror("Database Connection Error", f"Error: {e}")
        return None

def close_connection(connection):
    """Closes the MySQL database connection."""
    if connection:
        connection.close()
        print("Database connection closed")

def execute_query(query, params=None):
    """Executes a SQL query that doesn't return results."""
    connection = create_connection()
    if connection is None:
        return None

    try:
        cursor = connection.cursor()
        cursor.execute(query, params) if params else cursor.execute(query)
        connection.commit()
        return cursor
    except Error as e:
        messagebox.showerror("Query Error", f"Error: {e}")
        return None
    finally:
        close_connection(connection)

def fetch_all(query, params=None):
    """Fetches all results from a SQL query."""
    connection = create_connection()
    if connection is None:
        return None

    try:
        cursor = connection.cursor(dictionary=True)  # Fetch as dictionary for easier access
        cursor.execute(query, params) if params else cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        messagebox.showerror("Query Error", f"Error: {e}")
        return None
    finally:
        close_connection(connection)

def fetch_one(query, params=None):
    """Fetches a single result from a SQL query."""
    connection = create_connection()
    if connection is None:
        return None

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, params) if params else cursor.execute(query)
        result = cursor.fetchone()
        return result
    except Error as e:
        messagebox.showerror("Query Error", f"Error: {e}")
        return None
    finally:
        close_connection(connection)
