from tkinter import ttk, Tk
from tkinter import *

from Controllers.UserControllers import UserController


class ChangePassView(Tk):
    """Окно Изменения Пароля и его функции
    """
    def __init__(self, login):
        super().__init__()

        self.user = UserController.show(login)

        self.title(f"Изменение пароля: {self.user.login}")
        self.geometry("350x350")
        self.resizable(False,False)


        # Ввод старого пароля
        self.Old_Password_Lable = ttk.Label(self, text="Ввод Старый Пароль", foreground="#ff3366")
        self.Old_Password_Lable.pack(anchor="center", pady=10)

        self.Old_Password_Entry = ttk.Entry(self, foreground="#ff0099")
        self.Old_Password_Entry.pack(anchor="center")



        # Ввод нового пароля
        self.New_Password_Lable = ttk.Label(self, text="Ввод Новый Пароль", foreground="#ff3366")
        self.New_Password_Lable.pack(anchor="center", pady=10)

        self.New_Password_Entry = ttk.Entry(self, foreground="#ff0099")
        self.New_Password_Entry.pack(anchor="center")


        # Ввод подтверждения нового пароля
        self.Conf_New_Password_Lable = ttk.Label(self, text="Ввод Подтверждения Нового Пароля", foreground="#ff3366")
        self.Conf_New_Password_Lable.pack(anchor="center", pady=10)

        self.Conf_New_Password_Entry = ttk.Entry(self, foreground="#ff0099")
        self.Conf_New_Password_Entry.pack(anchor="center")



        # Текст (всплывающий)
        self.message_Lable = ttk.Label(self, foreground="#ff0099")
        self.message_Lable.pack(anchor="center", expand=1)


        # Кнопка Изменения Пароля
        self.enter_Button = ttk.Button(self, text="Изменить Пароль", command = self.Change_Pass)
        self.bind("<Return>", lambda e: self.Change_Pass())
        self.enter_Button.pack(anchor="center",expand=1)


        # Кнопка выхода
        self.escape_Button = ttk.Button(self, text="Выход", command = self.Escape)
        self.bind("<Escape>", lambda e: self.Escape())
        self.escape_Button.pack(anchor="center",expand=1)
    

    def Change_Pass(self):
        """Изменение пароля по введённому паролю
        """
        old_pass = self.Old_Password_Entry.get()
        new_pass = self.New_Password_Entry.get()
        conf_new_pass = self.Conf_New_Password_Entry.get()


        if  old_pass != "" and new_pass != "" and conf_new_pass != "":
            if old_pass == self.user.password:
                if new_pass == conf_new_pass:
                    UserController.update(self.user.id, password = new_pass, first_auth = False)
                    self.message_Lable["text"] = "Пароль успешно изменён"
                else:
                    self.message_Lable["text"] = "Новый пароль должен совпадать с введёным повторно"
            else:
                self.message_Lable["text"] = "Старый пароль не совпадает с введёным."
        else:
            self.message_Lable["text"] = "Все поля должны быть заполнены"

    def Escape(self):
        """Выход из окна
        """
        self.destroy()

if __name__ == "__main__":
    window = ChangePassView("User")
    window.mainloop()