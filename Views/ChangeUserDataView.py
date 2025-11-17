from tkinter import ttk, Tk
from tkinter import *

from Controllers.UserControllers import UserController

class ChangeUserDataView(Tk):
    def __init__(self, login):
        super().__init__()

        self.user = UserController.show(login)

        self.title(f"Изменение пользователя: {self.user.login}")
        self.geometry("450x400")
        self.resizable(False,False)
        ttk.Style().theme_use("clam")

        # Меняем имя
        self.Change_name_Label = ttk.Label(self,text="Логин", foreground="#ff3366").pack(anchor="center",pady=[10,2])
        self.Change_name_Entry = ttk.Entry(self, foreground="#ff0099").pack(anchor="center",pady=[0,15])

        # Меняем пароль
        self.Change_password_Label = ttk.Label(self,text="Пароль", foreground="#ff3366").pack(anchor="center",pady=[0,2])
        self.Change_password_Entry = ttk.Entry(self, foreground="#ff0099").pack(anchor="center",pady=[0,30])

        # Применить изменения
        self.Apply_changes_Button = ttk.Button(self, text="Применить изменения").pack(anchor="center",pady=[0,30])

        # Разбан
        self.Change_ban_Button = ttk.Button(self, text="Изменение блокировки").pack(anchor="center",pady=[0,30])

        # Сброс даты
        self.Change_data_Button = ttk.Button(self, text="Сброс Даты").pack(anchor="center", pady=[0,30])

        # Сообщения от системы пользователю
        self.message_Label = ttk.Label(self,text="_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_", foreground="#ff3366").pack(anchor="center")

        def Change_user(self):
            pass

        def Change_ban(self):
            pass

        def Change_data(self):
            pass


if __name__ == "__main__":
    window = ChangeUserDataView("test_text")
    window.mainloop()