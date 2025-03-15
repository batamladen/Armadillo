import tkinter as tk
import constants
from chipers import caesar_cipher

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")


def process_text(mode):
    """
    Handles the encryption or decryption process when a button is clicked.
    :param mode: "encrypt" or "decrypt".
    """
    text = input_field.get()  # Get text from the input field
    cipher_type = cipher_var.get()  # Get selected cipher type

    if cipher_type == "Caesar Cipher":
        result = caesar_cipher(text, mode=mode)  # Encrypt or decrypt the text (shift is defined in the function)
    else:
        result = "Cipher not implemented yet"  # Placeholder for other ciphers

    # Display the result in the output field
    output_field.config(state="normal")  # Temporarily enable the field
    output_field.delete(0, tk.END)  # Clear any existing text
    output_field.insert(0, result)  # Insert the new result
    output_field.config(state="readonly")  # Set back to read-only



# Window
win = tk.Tk()
win.geometry("500x700")
win.title("Armadilo")
win.configure(bg="black")

center_window(win, 500, 700)

# Load images properly
logo_image = tk.PhotoImage(file=constants.logo)  # Load armadillo.png
logo_letters = tk.PhotoImage(file=constants.logo_letters)  # Load armadillo name.png

# Name Label
name_label = tk.Label(win, image=logo_letters, bg="black")
name_label.place(x=0, y=-120)

# Logo Label
logo_label = tk.Label(win, image=logo_image, bg="black")
logo_label.place(x=0, y=-400)

#input feild
input_message = tk.Label(win, text="Input Text:", bg="black", fg="white")
input_message.place(x=100, y=230)

input_field = tk.Entry(win, bg="white", fg="black", font=("Arial", 14), width=30)
input_field.place(x=100, y=250)

# Output Field
input_message = tk.Label(win, text="Output:", bg="black", fg="white")
input_message.place(x=100, y=330)

output_field = tk.Entry(win, bg="white", fg="black", font=("Arial", 14), width=30, state="readonly")
output_field.place(x=100, y=350)

# Cipher Selection
cipher_var = tk.StringVar(value="Choose Chiper")  # Default cipher
cipher_menu = tk.OptionMenu(win, cipher_var, "Caesar Cipher", "Vigenère Cipher")
cipher_menu.place(x=100, y=400)

#Encrypt Button
encrypt_button = tk.Button(win, text="Encrypt", bg="gray", fg="black", font=("Arial", 12), command=lambda: process_text("encrypt"))
encrypt_button.place(x=100, y=450)

decrypt_button = tk.Button(win, text="Decrypt", bg="gray", fg="black", font=("Arial", 12), command=lambda: process_text("decrypt"))
decrypt_button.place(x=200, y=450)


win.mainloop()
