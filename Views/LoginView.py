from tkinter import Tk, ttk
from tkinter import *

from Controllers.UserControllers import  *


class LoginView(Tk):
    def __init__(self):
        super().__init__()

        # основное окно, его размеры и тема
        self.title("Информационная система")
        self.geometry("400x300")
        self.resizable(False,False)
        ttk.Style().theme_use("clam")

        # Поле ввода логина и подпись
        self.login_Lable = ttk.Label(self, text="Ввод Логин", foreground="#ff3366")
        self.login_Lable.pack(anchor="center", pady=10)

        self.login_Entry = ttk.Entry(self, foreground="#ff0099")
        self.login_Entry.pack(anchor="center")
        # Поле ввода пароля и подпись
        self.password_Lable = ttk.Label(self, text="Ввод Пароль", foreground="#ff3366")
        self.password_Lable.pack(anchor="center", pady=10)

        self.password_Entry = ttk.Entry(self, foreground="#ff0099")
        self.password_Entry.pack(anchor="center")
        # Текст (всплывающий)

        self.message_Lable = ttk.Label(self, foreground="#ff0099")
        self.message_Lable.pack(anchor="center")

        # Кнопка входа
        self.enter_Button = ttk.Button(self, text="Вход", command = self.LoginFunc)
        self.bind("<Key-Return>", lambda e: self.LoginFunc())
        self.enter_Button.pack(anchor="center",expand=1)

    def LoginFunc(self):
        print("nya?")


if __name__ == "__main__":
    window = LoginView()
    window.mainloop()