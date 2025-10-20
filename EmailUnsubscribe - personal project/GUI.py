import customtkinter as ctk
from email_manager import EmailManager  # Import the EmailManager class
from url_extract import process_urls  # Import the URL processing function
from url_clicker import visit_links  # Import the link-clicking function
import threading
import os
import sys

def get_resource_path(relative_path):
    """Get the absolute path to a resource, works for development and for PyInstaller."""
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller creates a temp folder and stores the executable path in _MEIPASS
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Use this function to get the path to links.txt
LINKS_FILE = get_resource_path("links.txt")

class EmailApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Email Unsubscribe Links")
        self.root.geometry("500x900")

        # Create and place widgets
        self.email_label = ctk.CTkLabel(root, text="Email:")
        self.email_label.pack(pady=10)

        self.email_entry = ctk.CTkEntry(root, width=400)
        self.email_entry.pack()

        self.password_label = ctk.CTkLabel(root, text="Password:")
        self.password_label.pack(pady=10)

        self.password_entry = ctk.CTkEntry(root, width=400, show="*")
        self.password_entry.pack()

        self.fetch_button = ctk.CTkButton(root, text="Fetch Unsubscribe Links", command=self.start_fetch_links)
        self.fetch_button.pack(pady=20)

        self.status_label = ctk.CTkLabel(root, text="Status: Idle")
        self.status_label.pack(pady=10)

        self.result_textbox = ctk.CTkTextbox(root, width=450, height=200)
        self.result_textbox.pack(pady=10)

        self.save_button = ctk.CTkButton(root, text="Save Links to File", command=self.save_links)
        self.save_button.pack(pady=10)

        # Add a button to summarize domains
        self.summarize_button = ctk.CTkButton(root, text="Summarize Domains", command=self.start_summarize)
        self.summarize_button.pack(pady=10)

        # Add a textbox to display summarized domains
        self.domain_textbox = ctk.CTkTextbox(root, width=450, height=100)
        self.domain_textbox.pack(pady=10)

        # Add an entry for selecting domains to unsubscribe from
        self.domain_entry_label = ctk.CTkLabel(root, text="Enter domains to unsubscribe from (comma-separated):")
        self.domain_entry_label.pack(pady=10)

        self.domain_entry = ctk.CTkEntry(root, width=400)
        self.domain_entry.pack()

        # Add a button to unsubscribe from selected domains
        self.unsubscribe_selected_button = ctk.CTkButton(root, text="Unsubscribe from Selected Domains", command=self.start_unsubscribe_selected)
        self.unsubscribe_selected_button.pack(pady=10)

        # Add a button to unsubscribe from all domains
        self.unsubscribe_all_button = ctk.CTkButton(root, text="Unsubscribe from All Domains", command=self.start_unsubscribe_all)
        self.unsubscribe_all_button.pack(pady=10)

        # Disable buttons initially
        self.update_button_states()

    def update_button_states(self):
        """Enable/disable buttons based on whether links.txt exists."""
        if os.path.exists(LINKS_FILE):
            self.summarize_button.configure(state="normal")
            self.unsubscribe_selected_button.configure(state="normal")
            self.unsubscribe_all_button.configure(state="normal")
        else:
            self.summarize_button.configure(state="disabled")
            self.unsubscribe_selected_button.configure(state="disabled")
            self.unsubscribe_all_button.configure(state="disabled")

    def start_fetch_links(self):
        """Start the email fetching process in a separate thread."""
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not email or not password:
            self.update_status("Please enter both email and password.")
            return

        # Disable the fetch button to prevent multiple clicks
        self.fetch_button.configure(state="disabled")
        self.update_status("Connecting to server...")

        # Run the email fetching process in a separate thread
        threading.Thread(target=self.fetch_links, args=(email, password), daemon=True).start()

    def fetch_links(self, email, password):
        """Fetch unsubscribe links from the email account."""
        try:
            # Create an instance of EmailManager
            email_manager = EmailManager(email, password)

            # Update status
            self.update_status("Fetching emails...")

            # Fetch links
            links = email_manager.search_for_email()
            if links:
                self.update_status(f"Found {len(links)} unsubscribe links.")
                self.result_textbox.delete("1.0", "end")  # Clear previous results
                for link in links:
                    self.result_textbox.insert("end", f"{link}\n")
            else:
                self.update_status("No unsubscribe links found.")
        except Exception as e:
            self.update_status(f"An error occurred: {e}")
        finally:
            # Re-enable the fetch button
            self.fetch_button.configure(state="normal")
            self.update_button_states()  # Update button states after fetching links

    def save_links(self):
        """Save the fetched links to a file."""
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not email or not password:
            self.update_status("Please enter both email and password.")
            return

        # Run the saving process in a separate thread
        threading.Thread(target=self._save_links, args=(email, password), daemon=True).start()

    def _save_links(self, email, password):
        """Internal method to save links in a separate thread."""
        try:
            # Create an instance of EmailManager
            email_manager = EmailManager(email, password)

            # Update status
            self.update_status("Fetching emails to save...")

            # Fetch links
            links = email_manager.search_for_email()
            if links:
                email_manager.save_links(links)
                self.update_status("Links saved to 'links.txt'.")
            else:
                self.update_status("No links to save.")
        except Exception as e:
            self.update_status(f"An error occurred: {e}")
        finally:
            self.update_button_states()  # Update button states after saving links

    def start_summarize(self):
        """Start the domain summarization process in a separate thread."""
        self.summarize_button.configure(state="disabled")
        self.update_status("Summarizing domains...")

        # Run the summarization process in a separate thread
        threading.Thread(target=self.summarize_domains, daemon=True).start()

    def summarize_domains(self):
        """Summarize domains from the links.txt file."""
        try:
            # Process URLs
            sorted_domains = process_urls(LINKS_FILE)

            # Display summarized domains in the textbox
            self.domain_textbox.delete("1.0", "end")  # Clear previous results
            for domain, count in sorted_domains:
                self.domain_textbox.insert("end", f"{domain}: {count} links\n")

            # Display results in the result textbox
            self.result_textbox.delete("1.0", "end")  # Clear previous results
            for domain, count in sorted_domains:
                self.result_textbox.insert("end", f"{domain}: {count}\n")
            self.update_status("Domain summarization complete.")
        except Exception as e:
            self.update_status(f"An error occurred: {e}")
        finally:
            # Re-enable the summarize button
            self.summarize_button.configure(state="normal")

    def start_unsubscribe_selected(self):
        """Start unsubscribing from selected domains."""
        selected_domains = self.domain_entry.get().strip()
        if not selected_domains:
            self.update_status("Please enter at least one domain.")
            return

        # Split the input into a list of domains
        domains_to_unsubscribe = [domain.strip() for domain in selected_domains.split(",")]

        # Disable the button to prevent multiple clicks
        self.unsubscribe_selected_button.configure(state="disabled")
        self.update_status("Unsubscribing from selected domains...")

        # Run the unsubscribing process in a separate thread
        threading.Thread(target=self.unsubscribe_selected_domains, args=(domains_to_unsubscribe,), daemon=True).start()

    def unsubscribe_selected_domains(self, domains_to_unsubscribe):
        """Unsubscribe from selected domains."""
        try:
            # Visit links
            results = visit_links(LINKS_FILE, domains_to_unsubscribe)

            # Display results
            self.result_textbox.delete("1.0", "end")  # Clear previous results
            for result in results:
                self.result_textbox.insert("end", f"{result}\n")
            self.update_status("Unsubscribing from selected domains complete.")
        except Exception as e:
            self.update_status(f"An error occurred: {e}")
        finally:
            # Re-enable the button
            self.unsubscribe_selected_button.configure(state="normal")

    def start_unsubscribe_all(self):
        """Start unsubscribing from all domains."""
        # Disable the button to prevent multiple clicks
        self.unsubscribe_all_button.configure(state="disabled")
        self.update_status("Unsubscribing from all domains...")

        # Run the unsubscribing process in a separate thread
        threading.Thread(target=self.unsubscribe_all_domains, daemon=True).start()

    def unsubscribe_all_domains(self):
        """Unsubscribe from all domains."""
        try:
            # Visit links
            results = visit_links(LINKS_FILE)

            # Display results
            self.result_textbox.delete("1.0", "end")  # Clear previous results
            for result in results:
                self.result_textbox.insert("end", f"{result}\n")
            self.update_status("Unsubscribing from all domains complete.")
        except Exception as e:
            self.update_status(f"An error occurred: {e}")
        finally:
            # Re-enable the button
            self.unsubscribe_all_button.configure(state="normal")

    def update_status(self, message):
        """Update the status label with a new message."""
        self.status_label.configure(text=f"Status: {message}")