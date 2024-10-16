import customtkinter as ctk
import tkinter as tk
import os
from main import main

# Configure dark mode
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Mapping analysis levels to numeric values
level_mapping = {
    "Level 1 Analysis": 1,
    "Level 2 Analysis": 2,
    "Level 3 Analysis": 3
}

# Initialize the main window
janela = ctk.CTk()
janela.geometry("600x430")
janela.title("Intelligent Network Security System")

# Function executed on circle click (transition to the result screen)
def start_analysis():
    hostname = hostname_entry.get()
    password = password_entry.get()
    analysis_level = level_mapping[options_level.get()]

    # Clear all widgets in the window for screen transition
    for widget in janela.winfo_children():
        widget.pack_forget()
    
    # Process the analysis and wait for the result
    score, log_file_path = main(hostname, password, analysis_level)

    # Show the result screen
    show_result(score, log_file_path)

# Function to check if the click is inside the circle
def click_within_circle(event):
    x, y = event.x, event.y
    # Check if the click is within the circle bounds
    if 30 <= x <= 270 and 30 <= y <= 270:
        start_analysis()

# Function that creates the first screen
def create_first_screen():
    # Welcome text
    welcome_text = ctk.CTkLabel(janela, text="Intelligent Network Security System", font=("Arial", 24))
    welcome_text.pack(pady=20)

    # Canvas for drawing circles
    canvas = tk.Canvas(janela, width=300, height=300, bg=janela.cget("bg"), highlightthickness=0)
    canvas.pack(pady=20)
    canvas.create_oval(30, 30, 270, 270, outline="white", width=5)
    canvas.create_oval(40, 40, 260, 260, outline="white", width=3)
    canvas.create_text(150, 130, text="Start", font=("Arial", 18), fill="white")
    canvas.create_text(150, 160, text="Network Analysis", font=("Arial", 14), fill="white")
    canvas.bind("<Button-1>", click_within_circle)

    # Frame for input fields
    input_frame = ctk.CTkFrame(janela, fg_color=janela.cget("bg"))
    input_frame.pack(pady=20, padx=10)

    # Hostname field
    global hostname_entry  # Declare globally to access later
    ctk.CTkLabel(input_frame, text="Hostname", font=("Arial", 14)).grid(row=0, column=0, padx=10)
    hostname_entry = ctk.CTkEntry(input_frame, placeholder_text="Hostname")
    hostname_entry.grid(row=1, column=0, padx=10)

    # Password field
    global password_entry  # Declare globally to access later
    ctk.CTkLabel(input_frame, text="Password", font=("Arial", 14)).grid(row=0, column=1, padx=10)
    password_entry = ctk.CTkEntry(input_frame, placeholder_text="Password", show="*")
    password_entry.grid(row=1, column=1, padx=10)

    # Level selection
    global options_level  # Declare globally to access later
    ctk.CTkLabel(input_frame, text="Analysis Level", font=("Arial", 14)).grid(row=0, column=2, padx=10)
    options_level = ctk.CTkOptionMenu(input_frame, values=list(level_mapping.keys()))
    options_level.set("Level 2 Analysis")  # Set default value
    options_level.grid(row=1, column=2, padx=10)

# Function that creates the second screen (result of the analysis)
def show_result(score, log_file_path):
    # Result text
    result_text = ctk.CTkLabel(janela, text="Analysis Result", font=("Arial", 24))
    result_text.pack(pady=20)

    # Canvas for displaying result score
    canvas = tk.Canvas(janela, width=300, height=300, bg=janela.cget("bg"), highlightthickness=0)
    canvas.pack(pady=20)
    canvas.create_oval(30, 30, 270, 270, outline="white", width=5)
    canvas.create_oval(40, 40, 260, 260, outline="white", width=3)
    canvas.create_text(120, 120, text=str(score), font=("Arial", 30), fill="white")
    canvas.create_text(160, 127, text="/1000", font=("Arial", 16), fill="white", anchor="w")
    canvas.create_text(150, 180, text="Score", font=("Arial", 22), fill="white")

    # Button to download the detailed report
    report_button = ctk.CTkButton(janela, text="Download Detailed Report", font=("Arial", 12), width=220,
                                   command=lambda: download_log_file(log_file_path))
    report_button.pack(pady=40)

def download_log_file(log_file_path):
    # Open the log file using the default text editor
    os.startfile(log_file_path)

# Create the first screen when starting the application
create_first_screen()

# Start the main window
janela.mainloop()
