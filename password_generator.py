'''
    Simple Password Generator Written In Python!
    GPL3 License: https://www.gnu.org/licenses/gpl-3.0.en.html#license-text

    Copyright (C) 2024  Luiz Gabriel Magalhães Trindade.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import secrets, string
from customtkinter import *
from pyperclip import copy

def Main():
    def Generate_Password():
        chars = string.ascii_letters+string.digits+string.punctuation
        password = "".join(secrets.choice(chars) for i in range(password_size))
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
