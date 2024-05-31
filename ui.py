import main
import tkinter as tk
from tkinter import filedialog

def createUI(): 
    # Create the main window
    window = tk.Tk()

    # Set the window title
    window.title("Klayvio Formatter")

    # Set the window size
    window.geometry("600x400")

    # Start the main event loop
    def select_files():
        # Open a file dialog to let the user select files
        files = tk.filedialog.askopenfilenames()

        # Pass the selected files to the main.py file
        success = main.process_csv(files)
        
        # Display a status message
        if success:
            success_message = tk.Label(window, text="Files processed successfully!", foreground="green")
            success_message.pack(pady=10)
        else:
            error_message = tk.Label(window, text="An error occurred - contact CoCo for support", foreground="red")
            error_message.pack(pady=10)

    # Create a button to trigger file selection
    select_button = tk.Button(window, text="Select Files", command=select_files)
    select_button.pack(pady = 100)
    
    # Function to close the window
    def close_window():
        window.destroy()

    # Create a button to close the window
    close_button = tk.Button(window, text="Close", command=close_window)
    close_button.pack(pady = 25)
    
    window.mainloop()