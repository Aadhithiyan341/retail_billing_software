import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from app.database.product_operations import get_all_products
from app.database.transaction_operations import create_transaction

class BillingScreen(tk.Frame):
    def __init__(self, parent):
        """Initializes the billing screen UI."""
        super().__init__(parent)

        # Create widgets for the billing screen
        self.create_widgets()

    def create_widgets(self):
        """Sets up the layout and widgets for the billing screen."""
        self.title_label = tk.Label(self, text="Billing Screen", font=("Helvetica", 16))
        self.title_label.pack(pady=20)

        # Customer details section
        self.customer_label = tk.Label(self, text="Customer Name")
        self.customer_label.pack()
        self.customer_entry = tk.Entry(self)
        self.customer_entry.pack(pady=5)

        # Product selection section
        self.product_label = tk.Label(self, text="Select Product")
        self.product_label.pack()

        self.product_combobox = ttk.Combobox(self)
        self.product_combobox['values'] = self.load_products()
        self.product_combobox.pack(pady=5)

        # Quantity input
        self.quantity_label = tk.Label(self, text="Quantity")
        self.quantity_label.pack()
        self.quantity_entry = tk.Entry(self)
        self.quantity_entry.pack(pady=5)

        # Add product to bill button
        self.add_product_button = tk.Button(self, text="Add Product to Bill", command=self.add_product_to_bill)
        self.add_product_button.pack(pady=10)

        # Bill summary
        self.bill_summary_label = tk.Label(self, text="Bill Summary", font=("Helvetica", 14))
        self.bill_summary_label.pack(pady=20)

        self.bill_text = tk.Text(self, height=10, width=40)
        self.bill_text.pack(pady=5)
        self.bill_text.config(state=tk.DISABLED)  # Disable editing for this area

        # Total amount label
        self.total_label = tk.Label(self, text="Total Amount: $0.00")
        self.total_label.pack(pady=5)

        # Complete transaction button
        self.complete_button = tk.Button(self, text="Complete Transaction", command=self.complete_transaction)
        self.complete_button.pack(pady=20)

    def load_products(self):
        """Fetches products from the database and returns them as a list of product names."""
        products = get_all_products()
        product_names = [product['name'] for product in products]  # Assuming product has 'name' field
        return product_names

    def add_product_to_bill(self):
        """Adds selected product and quantity to the bill summary."""
        product_name = self.product_combobox.get()
        quantity = self.quantity_entry.get()

        if not product_name or not quantity.isdigit():
            messagebox.showerror("Input Error", "Please select a product and enter a valid quantity.")
            return

        quantity = int(quantity)
        product = next((product for product in get_all_products() if product['name'] == product_name), None)

        if product:
            product_total = product['price'] * quantity
            self.update_bill_summary(product_name, quantity, product_total)
            self.update_total_amount(product_total)
        else:
            messagebox.showerror("Product Not Found", "Selected product not found in the database.")

    def update_bill_summary(self, product_name, quantity, product_total):
        """Updates the bill summary text area with the newly added product."""
        self.bill_text.config(state=tk.NORMAL)  # Allow editing
        self.bill_text.insert(tk.END, f"{product_name} (x{quantity}) - ${product_total:.2f}\n")
        self.bill_text.config(state=tk.DISABLED)  # Disable editing

    def update_total_amount(self, product_total):
        """Updates the total amount label."""
        current_total = float(self.total_label.cget("text").split(": $")[1])
        new_total = current_total + product_total
        self.total_label.config(text=f"Total Amount: ${new_total:.2f}")

    def complete_transaction(self):
        """Completes the transaction and stores it in the database."""
        customer_name = self.customer_entry.get().strip()
        if not customer_name:
            messagebox.showerror("Input Error", "Please enter a customer name.")
            return

        total_amount = float(self.total_label.cget("text").split(": $")[1])
        if total_amount == 0:
            messagebox.showerror("Error", "The bill is empty. Please add products to the bill.")
            return

        # Create the transaction record in the database
        transaction_id = create_transaction(customer_name, total_amount)

        if transaction_id:
            messagebox.showinfo("Transaction Complete", f"Transaction successful! Transaction ID: {transaction_id}")
            self.clear_bill()
        else:
            messagebox.showerror("Error", "Failed to complete the transaction. Please try again.")

    def clear_bill(self):
        """Clears the current bill after a successful transaction."""
        self.customer_entry.delete(0, tk.END)
        self.product_combobox.set('')
        self.quantity_entry.delete(0, tk.END)
        self.bill_text.config(state=tk.NORMAL)
        self.bill_text.delete(1.0, tk.END)
        self.bill_text.config(state=tk.DISABLED)
        self.total_label.config(text="Total Amount: $0.00")

