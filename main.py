import tkinter as tk
from tkinter import messagebox
from app.ui.login import LoginScreen
from app.ui.dashboard import DashboardScreen
from app.database.db_config import initialize_db  # Optional: Initialize DB on start

class RetailPOSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Retail POS System")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        # Optionally, initialize the database on app start (if needed)
        initialize_db()

        # Start with the login screen
        self.show_login_screen()

    def show_login_screen(self):
        """Displays the login screen."""
        self.clear_window()
        self.login_screen = LoginScreen(self.root, self.show_dashboard)
        self.login_screen.pack()

    def show_dashboard(self, user_data):
        """Switches to the main dashboard screen after successful login."""
        self.clear_window()
        self.dashboard_screen = DashboardScreen(self.root, user_data)
        self.dashboard_screen.pack()

    def clear_window(self):
        """Clears the window to show the next screen."""
        for widget in self.root.winfo_children():
            widget.destroy()

def main():
    # Create Tkinter window instance
    root = tk.Tk()
    
    # Create the main application instance and start the app
    app = RetailPOSApp(root)
    
    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
