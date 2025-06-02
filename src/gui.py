import tkinter as tk
from tkinter import filedialog
import os

def create_window() -> tk.Tk:
    window = tk.Tk()
    window.title("XML Reader")
    window.geometry("500x350")
    return window

def enter_directory(window: tk.Tk) -> tuple[str, str, bool]:
    global confirm_data
    confirm_data = {"input_path": "", "output_dir": "", "is_folder": False}
    
    # --- input directory ---
    def input_file_dir_button_command():
        path = tk.filedialog.askopenfilename(title="Wybierz plik xml", filetypes=[("XML files", "*.xml")])
        if path:
            input_dir.delete(0, tk.END)
            input_dir.insert(0, path)

    main_input_info = tk.Label(window, text="Wpisz ścieżkę do pliku XML")
    main_input_info.pack()

    input_div = tk.Frame(window)
    input_div.pack(pady=20)

    input_dir = tk.Entry(input_div, width=50)
    input_dir_button = tk.Button(input_div, text="Przeglądaj", command=input_file_dir_button_command)
    input_dir.pack(side=tk.LEFT)
    input_dir_button.pack(side=tk.RIGHT)

    # --- output directory ---
    def output_dir_button_command():
        path = tk.filedialog.askdirectory(initialdir="C:/", title="Wybierz folder docelowy", mustexist=True)
        if path:
            output_dir.delete(0, tk.END)
            output_dir.insert(0, path)
    main_output_info = tk.Label(window, text="Wpisz ścieżkę do folderu docelowego")
    main_output_info.pack(pady=(50, 0))

    output_div = tk.Frame(window)
    output_div.pack(pady=20)

    output_dir = tk.Entry(output_div, width=50)
    output_dir_button = tk.Button(output_div, text="Przeglądaj", command=output_dir_button_command)
    output_dir.pack(side=tk.LEFT)
    output_dir_button.pack(side=tk.RIGHT)

    if os.path.exists("xml_to_png_data/data.txt"):
        with open("xml_to_png_data/data.txt", "r") as f:
            last_output_dir = f.read()
            if os.path.exists(last_output_dir):
                confirm_data["output_dir"] = last_output_dir
                output_dir.insert(0, last_output_dir)

    # --- confirm button ---
    def confirm_button_command():
        if input_dir.get() == "" or output_dir.get() == "":
            enter_dirs_info.config(text="Prosze wypenić obydwa pola.")
        else:
            confirm_data["input_path"] = input_dir.get()
            confirm_data["output_dir"] = output_dir.get()

            if os.path.exists(confirm_data["input_path"]):
                window.destroy()
            else:
                enter_dirs_info.config(text="Podany plik nie istnieje. Proszę podać poprawną ścieżkę do pliku XML.")
                
    confirm_button = tk.Button(window, text="Potwierdź", command=confirm_button_command)
    confirm_button.pack(pady=10)

    enter_dirs_info = tk.Label(window, text="")
    enter_dirs_info.pack(pady=30)

    # --- close the window ---
    def close_window():
        confirm_data["input_path"] = ""
        confirm_data["output_dir"] = ""
        window.destroy()
    window.protocol("WM_DELETE_WINDOW", close_window)

    window.mainloop()
    return confirm_data

def main() -> dict:
    window = create_window()
    confirm_data = enter_directory(window)
    return confirm_data