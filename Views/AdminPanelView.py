from tkinter import Tk, ttk
from tkinter import *

from Controllers.UserControllers import  *

class AdminPanelView(Tk):
    def __init__(self, login):
        super().__init__()

        self.user = UserController.show(login)
        
        self.title(f"Панель Администратора: {self.user.login}")
        self.geometry("400x300")
        self.resizable(False,False)
        ttk.Style().theme_use("clam")

        # Текст создание логина
        self.create_login_Label = ttk.Label(self,text="Логин", foreground="#ff3366")
        self.create_login_Label.pack(anchor="center")
        # Ввод создание логина
        self.create_login_Label = ttk.Entry(self, foreground="#ff0099")
        self.create_login_Label.pack(anchor="center")

        # Текст создание пароля
        self.create_password_Label = ttk.Label(self,text="Пароль", foreground="#ff3366")
        self.create_password_Label.pack(anchor="center")
        # Ввод создание логина
        self.create_password_Label = ttk.Entry(self, foreground="#ff0099")
        self.create_password_Label.pack(anchor="center")

        # Кнопка Создания пользователя
        self.create_user_Button = ttk.Button(text="Создать Пользователя", command=Create_User)
        self.create_user_Button.pack(anchor="center", expand=1)

    def Create_User(self):
        pass


if __name__ == "__main__":
    window = AdminPanelView("User")
    window.mainloop()