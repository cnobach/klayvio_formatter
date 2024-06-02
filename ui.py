import main
import tkinter as tk
from tkinter import filedialog

def createUI(): 
    window = tk.Tk()
    window.title("Klayvio Formatter")
    window.geometry("600x400")

    def select_files():
        files = tk.filedialog.askopenfilenames()
        success = main.process_csv(files)   
        
        if success:
            success_message = tk.Label(window, text="Files processed successfully!", foreground="green")
            success_message.pack(pady=10)
        else:
            error_message = tk.Label(window, text="An error occurred - contact CoCo for support", foreground="red")
            error_message.pack(pady=10)

    select_button = tk.Button(window, text="Select Files", command=select_files)
    select_button.pack(pady = 100)
    
    def close_window():
        window.destroy()

    close_button = tk.Button(window, text="Close", command=close_window)
    close_button.pack(pady = 25)
    
    window.mainloop()