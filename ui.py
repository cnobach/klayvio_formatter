import main
import tkinter as tk
from tkinter import filedialog

def createUI(): 
    window = tk.Tk()
    window.title("Klayvio Formatter")
    window.geometry("600x400")
    
    message_label = tk.Label(window, text="Select the CSV files you would like to process", font=("Arial", 16))
    message_label.pack(pady=10)

    def select_files():
        files = tk.filedialog.askopenfilenames()
        success = main.process_csv(files)   

        if success == 2:
            message_label.config(text="An error occurred - contact CoCo for support", foreground="red")
        elif success == 1:
            message_label.config(text="Files processed successfully!", foreground="green")
        elif success == 0:
            message_label.config(text="Please select files for processing", foreground="orange")

    select_button = tk.Button(window, text="Select Files", command=select_files)
    select_button.pack(pady = 100)
    
    def close_window():
        window.destroy()

    close_button = tk.Button(window, text="Close", command=close_window)
    close_button.pack(pady = 25)
    
    window.mainloop()