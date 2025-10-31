from tkinter import Tk, ttk
from tkinter import *

from Controllers.UserControllers import  *


class LoginView(Tk):
    def __init__(self):
        super().__init__()

        # основное окно, его размеры и тема
        self.title("Информационная система")
        self.geometry("600x400")
        self.minsize(400,200)
        self.maxsize(800,600)
        ttk.Style().theme_use("clam")

        # Поле ввода логина и подпись
        self.login_Lable = ttk.Label(self, text="Ввод Логин", foreground="#ff3366")
        self.login_Lable.pack(anchor="center",pady=5, padx=15)

        self.login_Entry = ttk.Entry(self, foreground="#ff0099")
        self.login_Entry.pack(anchor="center",pady=2, padx=15)
        # Поле ввода пароля и подпись
        self.password_Lable = ttk.Label(self, text="Ввод Пароль", foreground="#ff3366")
        self.password_Lable.pack(anchor="center",pady=5, padx=15)

        self.password_Entry = ttk.Entry(self, foreground="#ff0099")
        self.password_Entry.pack(anchor="center", pady=2, padx=15)
        # Текст (всплывающий)

        # Кнопка входа



if __name__ == "__main__":
    window = LoginView()
    window.mainloop()