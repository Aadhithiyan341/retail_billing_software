import tkinter as tk
from tkinter import messagebox
from app.database.user_operations import authenticate_user

class LoginScreen(tk.Frame):
    def __init__(self, parent, show_dashboard_callback):
        """Initializes the login screen UI."""
        super().__init__(parent)
        self.show_dashboard_callback = show_dashboard_callback

        # Create widgets for the login screen
        self.create_widgets()

    def create_widgets(self):
        """Sets up the layout and widgets for the login screen."""
        self.title_label = tk.Label(self, text="Retail POS System - Login", font=("Helvetica", 16))
        self.title_label.pack(pady=20)

        # Username field
        self.username_label = tk.Label(self, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=5)

        # Password field
        self.password_label = tk.Label(self, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=5)

        # Login button
        self.login_button = tk.Button(self, text="Login", command=self.handle_login)
        self.login_button.pack(pady=10)

        # Optionally, add a "forgot password" or registration link here (if needed)

    def handle_login(self):
        """Handles the login process."""
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            messagebox.showerror("Input Error", "Please enter both username and password.")
            return

        # Authenticate the user with the provided credentials
        user_data = authenticate_user(username, password)
        if user_data:
            # On successful login, pass user data to dashboard
            self.show_dashboard_callback(user_data)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")
