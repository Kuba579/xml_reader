import data_reader as dr
import base64
import gui
import os
import ctypes

def convert(input_path: str, output_dir: str=""):
    base64_data = dr.get_base64_data(input_path)
    image_data = base64.b64decode(base64_data)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(output_dir + "/output.png", "wb") as f:
        f.write(image_data)

if __name__ == "__main__":
    confirm_data = gui.main()
    input_path = confirm_data["input_path"]
    output_dir = confirm_data["output_dir"]
    if not output_dir and not input_path:
        exit()
    try:
        convert(input_path, output_dir)
        remember_output_dir = "xml_to_png_data/"
        os.makedirs(remember_output_dir) if not os.path.exists(remember_output_dir) else None
        with open("xml_to_png_data/data.txt", "w") as f:
            f.write(output_dir)
    except:
        ctypes.windll.user32.MessageBoxW(0, "Wystąpił błąd przy konwersji!", "Błąd", 0x10)
