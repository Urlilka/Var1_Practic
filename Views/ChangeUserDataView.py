from tkinter import ttk, Tk
from tkinter import *

from Controllers.UserControllers import UserController

class ChangeUserDataView(Tk):
    def __init__(self, login):
        super().__init__()

        self.user = UserController.show(login)

        self.title(f"Изменение пользователя: {self.user.login}")
        self.geometry("450x350")
        self.resizable(False,False)
        ttk.Style().theme_use("clam")


if __name__ == "__main__":
    window = ChangeUserDataView("test_text")
    window.mainloop()