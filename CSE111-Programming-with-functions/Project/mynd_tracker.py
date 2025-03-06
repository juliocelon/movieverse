"""
Author: Julio Celón
Title: W07 Final Project
"""

import tkinter as tk
from tkinter import Frame, Label, Button, Text, Entry
from tkinter import filedialog

def read_file(file_path):
    """Reads the content of a given file."""
    with open(file_path, 'r') as file:
        return file.read()
    

def open_file_ui(text_widget, ent_file):
    """Opens a file and loads its content into the text widget."""
    file_path = filedialog.askopenfilename()
    if file_path:
        ent_file.delete(0, tk.END)
        ent_file.insert(0, file_path)
        content = read_file(file_path)
        text_widget.delete("1.0", tk.END)
        text_widget.insert(tk.END, content)


def save_file(text, file_path):
    """Saves the content to a file without involving the UI components."""
    try:
        with open(file_path, 'w') as file:
            file.write(text)
        return f"File saved successfully: {file_path}"
    except Exception as e:
        return f"Error saving file: {str(e)}"


def save_file_ui(text_widget, ent_file, lbl_information):
    """Saves the content of the text widget to a file with UI interaction."""
    file_path = ent_file.get()
    
    if not file_path:  # If no file is selected, prompt the user to choose a save location.
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt"),
                                                            ("All Files", "*.*")])
        if not file_path:
            lbl_information.config(text="Save canceled.")
            return

    result = save_file(text_widget.get("1.0", tk.END), file_path)
    lbl_information.config(text=result)

def main():
    root = tk.Tk()
    root.title("Mynd Tracker")

    frm_main = Frame(root)
    frm_main.pack(padx=14, pady=3, fill=tk.BOTH, expand=1)

    populate_main_window(frm_main)

    root.mainloop()

def populate_main_window(frm_main):
    """Populate the main window with labels, entry boxes, and buttons."""
    
    lbl_file = Label(frm_main, text="File:")
    ent_file = Entry(frm_main, width=50)

    # Buttons
    btn_open = Button(frm_main, text="Open File")
    btn_save = Button(frm_main, text="Save")

    txt_message = Text(frm_main, wrap="word", height=20, width=100)

    lbl_information = Label(frm_main, text="")
    lbl_message = Label(frm_main, text="MESSAGE:")

    # Layout widgets in a grid
    lbl_file.grid(row=0, column=0, padx=5, pady=5)
    ent_file.grid(row=0, column=1, padx=5, pady=5, columnspan=2)

    btn_open.grid(row=0, column=3, padx=5, pady=5)
    btn_save.grid(row=0, column=4, padx=5, pady=5)

    lbl_information.grid(row=1, column=1, columnspan=3, pady=5)
    lbl_message.grid    (row=2, column=1, columnspan=3, pady=5)

    txt_message.grid    (row=3, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

    # Configure button actions
    btn_open.config(command=lambda: open_file_ui(txt_message, ent_file))
    btn_save.config(command=lambda: save_file_ui(txt_message, ent_file, lbl_information))

    # Grid column configuration for resizing
    frm_main.columnconfigure(1, weight=1)
    frm_main.rowconfigure(3, weight=1)

if __name__ == "__main__":
    main()
