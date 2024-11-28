import pandas as pd
import os
from tkinter import messagebox

# Function to export data to CSV
def export_to_csv(data, filename):
    """Exports the provided data to a CSV file."""
    try:
        # Create a DataFrame from the data (assuming data is a list of dictionaries)
        df = pd.DataFrame(data)
        
        # Define the file path
        file_path = os.path.join("exports", f"{filename}.csv")
        
        # Ensure the 'exports' directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Export to CSV
        df.to_csv(file_path, index=False)
        
        messagebox.showinfo("Export Successful", f"Data successfully exported to {file_path}")
        return file_path
    except Exception as e:
        messagebox.showerror("Export Error", f"Error exporting data to CSV: {str(e)}")
        return None

# Function to export data to Excel
def export_to_excel(data, filename):
    """Exports the provided data to an Excel file."""
    try:
        # Create a DataFrame from the data (assuming data is a list of dictionaries)
        df = pd.DataFrame(data)
        
        # Define the file path
        file_path = os.path.join("exports", f"{filename}.xlsx")
        
        # Ensure the 'exports' directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Export to Excel
        df.to_excel(file_path, index=False)
        
        messagebox.showinfo("Export Successful", f"Data successfully exported to {file_path}")
        return file_path
    except Exception as e:
        messagebox.showerror("Export Error", f"Error exporting data to Excel: {str(e)}")
        return None
