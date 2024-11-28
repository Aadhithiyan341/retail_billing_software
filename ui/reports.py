import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from app.database.transaction_operations import get_transactions
from app.database.customer_operations import get_all_customers
from app.utils.data_export import export_to_csv, export_to_excel

class ReportsScreen(tk.Frame):
    def __init__(self, parent):
        """Initializes the reports screen UI."""
        super().__init__(parent)

        # Create widgets for the reports screen
        self.create_widgets()

    def create_widgets(self):
        """Sets up the layout and widgets for the reports screen."""
        self.title_label = tk.Label(self, text="Reports Screen", font=("Helvetica", 16))
        self.title_label.pack(pady=20)

        # Date filter section
        self.date_label = tk.Label(self, text="Select Date Range")
        self.date_label.pack()

        self.start_date_label = tk.Label(self, text="Start Date (YYYY-MM-DD)")
        self.start_date_label.pack()
        self.start_date_entry = tk.Entry(self)
        self.start_date_entry.pack(pady=5)

        self.end_date_label = tk.Label(self, text="End Date (YYYY-MM-DD)")
        self.end_date_label.pack()
        self.end_date_entry = tk.Entry(self)
        self.end_date_entry.pack(pady=5)

        # Buttons to filter and view reports
        self.filter_button = tk.Button(self, text="Filter Reports", command=self.filter_reports)
        self.filter_button.pack(pady=10)

        self.view_transactions_button = tk.Button(self, text="View Transactions", command=self.view_transactions)
        self.view_transactions_button.pack(pady=10)

        self.view_customers_button = tk.Button(self, text="View Customers", command=self.view_customers)
        self.view_customers_button.pack(pady=10)

        # Export options
        self.export_label = tk.Label(self, text="Export Report")
        self.export_label.pack(pady=20)

        self.export_csv_button = tk.Button(self, text="Export to CSV", command=self.export_to_csv)
        self.export_csv_button.pack(pady=5)

        self.export_excel_button = tk.Button(self, text="Export to Excel", command=self.export_to_excel)
        self.export_excel_button.pack(pady=5)

        # Results display area (list of transactions or customers)
        self.results_text = tk.Text(self, height=15, width=60)
        self.results_text.pack(pady=5)
        self.results_text.config(state=tk.DISABLED)  # Disable editing for this area

    def filter_reports(self):
        """Filters reports by date range."""
        start_date = self.start_date_entry.get().strip()
        end_date = s
