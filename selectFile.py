import tkinter as tk
from tkinter import filedialog

def select_file_and_read():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    root.update()
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    root.destroy()
    return file_path
