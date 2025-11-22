from tkinter import Tk, ttk
from tkinter import *

from Controllers.UserControllers import  *

from Views.ChangeUserDataView import ChangeUserDataView


class AdminPanelView(Tk):
    def __init__(self, login):
        super().__init__()

        self.user = UserController.show(login)
        
        self.title(f"Панель Администратора: {self.user.login}")
        self.geometry("800x600")
        self.resizable(False,False)

        # Текст создание логина
        self.create_login_Label = ttk.Label(self,text="Логин", foreground="#ff3366")
        self.create_login_Label.pack(anchor="center", pady=10)
        # Ввод создание логина
        self.create_login_Entry = ttk.Entry(self, foreground="#ff0099")
        self.create_login_Entry.pack(anchor="center")

        # Текст создание пароля
        self.create_password_Label = ttk.Label(self,text="Пароль", foreground="#ff3366")
        self.create_password_Label.pack(anchor="center", pady=10)
        # Ввод создание логина
        self.create_password_Entry = ttk.Entry(self, foreground="#ff0099")
        self.create_password_Entry.pack(anchor="center")

        # Кнопка Создания пользователя
        self.create_user_Button = ttk.Button(self,text="Создать Пользователя", command=self.Create_User)
        self.bind("<Return>", lambda e: self.Create_User())
        self.create_user_Button.pack(anchor="center", expand=1)

        # Текст для сообщений системы пользователю
        self.message_Label = ttk.Label(self,text="", foreground="#ff3366")
        self.message_Label.pack(anchor="center")

        # Таблица с пользователями
        column_headings=("login","password","ban","date_auth","role")
        self.users_Treeview = ttk.Treeview(columns=column_headings,show="headings")
        self.users_Treeview.pack(fill=X,expand=1)
        

        # Заполнение Таблицы
        self.enter_user_data()

        # Перенаправление в изменение данных пользователя
        self.bind("<<TreeviewSelect>>",self.select_change_data)

        # Кнопка перезагрузки списка
        self.tree_reboot_Button = ttk.Button(text="Перезагрузить список", command=self.enter_user_data)
        self.tree_reboot_Button.pack(anchor="center", expand=1)

        # Кнопка выхода из панели
        self.exit_Button = ttk.Button(text="Выход", command=self.Escape)
        self.bind("<Escape>",lambda e: self.Escape())
        self.exit_Button.pack(anchor="center", expand=1)

    
    def select_change_data(self,event):
        """Переход в окно изменения выбранного пользователя
        """
        select = self.users_Treeview.selection()[0]
        selected = self.users_Treeview.item(select)["values"][0]
        if UserController.show(selected).role_id.id != 1:
            ChangeUserDataWindow = ChangeUserDataView(selected)
            self.message_Label["text"] = "Переход в окно изменение пароля"
        else:
            self.message_Label["text"] = "Недоступно"

    def enter_user_data(self):
        """Формирования данных в таблице
        """
        for item in self.users_Treeview.get_children():
            self.users_Treeview.delete(item)

        list = UserController.get()
        user_list = []
        for user in list:
            if user.ban:
                ban = "Да"
            else:
                ban = "Нет"

            if user.date_auth is None:
                date_auth = "Не входил"
            else:
                date_auth = user.date_auth
        
            user_list.append(
                (user.login, user.password, ban, date_auth, user.role_id.role)
            )
        
        # настройка Таблицы с пользователями
        self.users_Treeview.heading("login", text="Логин")
        self.users_Treeview.heading("password", text="Пароль")
        self.users_Treeview.heading("ban", text="Блокировка")
        self.users_Treeview.heading("date_auth", text="Дата авторизации")
        self.users_Treeview.heading("role", text="Роль")
        # Настройка ширины
        self.users_Treeview.column("#1",width=159)
        self.users_Treeview.column("#2",width=159)
        self.users_Treeview.column("#3",width=159)
        self.users_Treeview.column("#4",width=159)
        self.users_Treeview.column("#5",width=159)

        for user in user_list:
            self.users_Treeview.insert("",END,values=user)


    def Escape(self):
        """Выход из панели администратора
        """
        from Views.LoginView import LoginView
        LoginViewWindow = LoginView()
        self.destroy()
    
    def Create_User(self):
        """Создание пользователя по введённому логину и паролю
        """
        login = self.create_login_Entry.get()
        password = self.create_password_Entry.get()
        if login != "" and password != "":
            if login != UserController.show(login).login:
                UserController.add(login,password)
                self.message_Label["text"] = "Создание пользователя успешно"
                self.enter_user_data()
            else:
                self.message_Label["text"] = "Пользователь с таким Логином уже существует"
        else:
            self.message_Label["text"] = "Создание пользователя завершилось ошибкой"


if __name__ == "__main__":
    window = AdminPanelView("Admin")
    window.mainloop()