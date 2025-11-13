from tkinter import Tk, ttk
from tkinter import *

from Controllers.UserControllers import  *


class AdminPanelView(Tk):
    def __init__(self, login):
        super().__init__()

        self.user = UserController.show(login)
        
        self.title(f"Панель Администратора: {self.user.login}")
        self.geometry("800x600")
        self.resizable(False,False)
        ttk.Style().theme_use("clam")

        # Текст создание логина
        self.create_login_Label = ttk.Label(self,text="Логин", foreground="#ff3366")
        self.create_login_Label.pack(anchor="center", pady=10)
        # Ввод создание логина
        self.create_login_Label = ttk.Entry(self, foreground="#ff0099")
        self.create_login_Label.pack(anchor="center")

        # Текст создание пароля
        self.create_password_Label = ttk.Label(self,text="Пароль", foreground="#ff3366")
        self.create_password_Label.pack(anchor="center", pady=10)
        # Ввод создание логина
        self.create_password_Label = ttk.Entry(self, foreground="#ff0099")
        self.create_password_Label.pack(anchor="center")

        # Кнопка Создания пользователя
        self.create_user_Button = ttk.Button(text="Создать Пользователя", command=self.Create_User)
        self.create_user_Button.pack(anchor="center", expand=1)

        # Таблица с пользователями
        column_headings=("login","password","ban","date_auth","role")
        self.users_Treeview = ttk.Treeview(columns=column_headings,show="headings")
        self.users_Treeview.pack(fill=X,expand=1)
        # настройка Таблицы с пользователями
        self.users_Treeview.heading("login", text="Логин")
        self.users_Treeview.heading("password", text="Пароль")
        self.users_Treeview.heading("ban", text="Блокировка")
        self.users_Treeview.heading("date_auth", text="Дата авторизации")
        self.users_Treeview.heading("role", text="Роль")
        # Заполнение Таблицы
        self.enter_user_data()
        # Перенаправление в изменение данных пользователя

        # Кнопка выхода из панели
        self.exit_Button = ttk.Button(text="Выход", command=self.Escape)
        self.bind("<Escape>",lambda e: self.Escape())
        self.exit_Button.pack(anchor="center", expand=1)
    

    def enter_user_data(self):
        for item in self.users_Treeview.get_children():
            self.users_Treeview.delete(item)

        list = UserController.get()
        user_list = []
        for user in list:
            if user.ban:
                ban = "Да"
            else:
                ban = "Нет"

            if user.first_auth is None:
                date_auth = "Не входил"
            else:
                date_auth = user.date_auth
        
        user_list.append(
            (user.login, user.password, ban, date_auth, user.role_id.role)
        )

        for user in user_list:
            self.users_Treeview.insert("",END,values=user)


    def Escape(self):
        from Views.LoginView import LoginView
        LoginViewWindow = LoginView()
        self.destroy()
    
    def Create_User(self):
        print("Пока только в вашем воображении")


if __name__ == "__main__":
    window = AdminPanelView("User")
    window.mainloop()