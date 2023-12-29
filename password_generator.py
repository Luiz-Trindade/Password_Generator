# Simple Password Generator Written In Python!
# Created By: Luiz Gabriel Magalhães Trindade.
# Distributed Under The GPL3 License.
# GPL3 License: https://www.gnu.org/licenses/gpl-3.0.en.html#license-text

from random import choice
from customtkinter import *
from pyperclip import copy

def Main():
    def Generate_Password():
        chars = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890!@#$%&*_"
        password = ""
        for i in range(password_size):
            password += choice(chars)
        password_label.configure(text=password)
        copy(password)

    def Set_Password_Size(value):
        nonlocal password_size
        password_size = int(value)
        text.configure(text=f"Password Size: {password_size}")

    default_minimum = 16
    default_maximum = 64

    #Password Size or Length
    password_size = default_minimum

    app = CTk()
    app.title("Password Generator 🔐")
    app.geometry("860x280")
    set_appearance_mode("dark")
    set_default_color_theme("green")

    frame = CTkFrame(master=app, height=50)
    frame.pack(pady=20, padx=10)

    password_label = CTkLabel(master=frame, text="Password", font=("Times New Roman", 20, "bold"))
    password_label.pack(pady=30, padx=30)

    text = CTkLabel(master=app, text=f"Password Size: {password_size}", font=("Arial", 15, "bold"))
    text.pack()

    password_size_slider = CTkSlider(master=app, from_=default_minimum, to=default_maximum, command=Set_Password_Size)
    password_size_slider.set(password_size)
    password_size_slider.pack()

    generate_button = CTkButton(master=app, text="Generate!", font=("Arial", 35, "bold"), command=Generate_Password)
    generate_button.pack(pady=30, padx=30)


    app.mainloop()

if __name__ == "__main__":
    Main()
