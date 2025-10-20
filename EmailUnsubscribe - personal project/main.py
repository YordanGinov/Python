import customtkinter as ctk
from GUI import EmailApp  # Import the EmailApp class

# Set appearance mode and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Create the main application window
root = ctk.CTk()

# Initialize the EmailApp
app = EmailApp(root)

# Run the application
root.mainloop()