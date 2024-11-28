import tkinter as tk
from tkinter import messagebox
from app.ui.billing import BillingScreen
from app.ui.reports import ReportsScreen

class DashboardScreen(tk.Frame):
    def __init__(self, parent, user_data):
        """Initializes the dashboard UI with the logged-in user's data."""
        super().__init__(parent)
        self.user_data = user_data  # Store user data for further use (e.g., name, role)
        
        # Create widgets for the dashboard
        self.create_widgets()

    def create_widgets(self):
        """Sets up the layout and widgets for the dashboard screen."""
        self.title_label = tk.Label(self, text=f"Welcome, {self.user_data['username']}!", font=("Helvetica", 16))
        self.title_label.pack(pady=20)

        # Navigation buttons
        self.billing_button = tk.Button(self, text="Go to Billing", command=self.open_billing)
        self.billing_button.pack(pady=10)

        self.reports_button = tk.Button(self, text="View Reports", command=self.view_reports)
        self.reports_button.pack(pady=10)

        # Add any other dashboard features, such as user profile, logout button, etc.
        self.logout_button = tk.Button(self, text="Logout", command=self.logout)
        self.logout_button.pack(pady=20)

    def open_billing(self):
        """Opens the billing screen."""
        self.clear_window()
        self.billing_screen = BillingScreen(self.master)
        self.billing_screen.pack()

    def view_reports(self):
        """Opens the reports screen."""
        self.clear_window()
        self.reports_screen = ReportsScreen(self.master)
        self.reports_screen.pack()

    def logout(self):
        """Logs out the user and returns to the login screen."""
        self.master.show_login_screen()

    def clear_window(self):
        """Clears the window to show the next screen."""
        for widget in self.master.winfo_children():
            widget.destroy()
