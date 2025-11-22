from tkinter import Tk, ttk
from tkinter import *

from Controllers.UserControllers import  UserController

from Views.ChangePassView import ChangePassView
from Views.AdminPanelView import AdminPanelView

from datetime import datetime


class LoginView(Tk):
    """Окно Авторизации и его функции
    """
    def __init__(self):
        super().__init__()

        
        # основное окно, его размеры и тема
        self.title("Информационная система")
        self.geometry("400x300")
        self.resizable(False,False)

        
        # Поле ввода логина и подпись
        self.login_Lable = ttk.Label(self, text="Ввод Логин", foreground="#ff3366")
        self.login_Lable.pack(anchor="center", pady=10)

        self.login_Entry = ttk.Entry(self, foreground="#ff0099")
        self.login_Entry.pack(anchor="center")
        
        
        # Поле ввода пароля и подпись
        self.password_Lable = ttk.Label(self, text="Ввод Пароль", foreground="#ff3366")
        self.password_Lable.pack(anchor="center", pady=10)

        self.password_Entry = ttk.Entry(self, show="*", foreground="#ff0099")
        self.password_Entry.pack(anchor="center")
        
        
        # Текст (всплывающий)
        self.message_Lable = ttk.Label(self, foreground="#ff0099")
        self.message_Lable.pack(anchor="center", expand=1)


        # Кнопка входа
        self.enter_Button = ttk.Button(self, text="Вход", command = self.LoginFunc)
        self.bind("<Return>", lambda e: self.LoginFunc())
        self.enter_Button.pack(anchor="center",expand=1)


        # Кнопка выхода из панели
        self.exit_Button = ttk.Button(text="Выход", command=self.Escape)
        self.bind("<Escape>",lambda e: self.Escape())
        self.exit_Button.pack(anchor="center",pady=30, expand=1)


        self.counter_for_ban = {}


    def Escape(self):
        """Выход из окна
        """
        self.destroy()

    def LoginFunc(self):
        """Функция Входа в Админ панель, Изменения пароля и с проверкой на разные случаи и функцией бана пользователя в зависимости от ситуаций.
        """
        login = self.login_Entry.get()
        password = self.password_Entry.get()
        user = UserController.auth(login=login, password=password)

        if login == "" or password == "":
            self.message_Lable["text"] = "Необходимо заполнить все поля"

        else:
            if not user:
                self.message_Lable["text"] = f"Вы ввели неверный логин и/или пароль.\nПожалуйста проверьте ещё раз введенные данные"

                if login not in self.counter_for_ban:
                    self.counter_for_ban[login] = 0
                else:
                    self.counter_for_ban[login] =+ 1

                if self.counter_for_ban[login] >= 3:
                    UserController.update(user.id,ban=1)

            elif user.role_id.id == 1:
                self.counter_for_ban[login] = 0
                self.message_Lable["text"] = f"Переход в Панель Администратора"
                UserController.update(user.id, date_auth = datetime.now().date())
                AdminPanelWindow = AdminPanelView(user.login) # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                # AdminPanelWindow = AdminPanelView("Admin")
                self.destroy()

            elif user.first_auth:
                self.counter_for_ban[login] = 0
                self.message_Lable["text"] = f"Вход в окно Изменения Пароля"
                ChangePassWindow = ChangePassView(user.login)

            elif user.date_auth is not None and (datetime.now().date() - user.date_auth).days >= 31:
                self.counter_for_ban[login] = 0
                UserController.update(user.id, ban=1)
                self.message_Lable["text"] = f"В связи не авторизации в течении месяца - ваша учётная запись была заблокированна.\nОбратитесь к администратору"
            
            elif user.ban:
                self.message_Lable["text"] = f"Вы заблокированы.\nОбратитесь к администратору"
            
            elif user.role_id.id == 2: #---------------------------------------
                self.counter_for_ban[login] = 0
                self.message_Lable["text"] = f"Переход в Панель Пользователя"
                UserController.update(user.id, date_auth = datetime.now().date())

            else:
                self.message_Lable["text"] = "Произошла непредвиденная ошибка"


if __name__ == "__main__":
    window = LoginView()
    window.mainloop()