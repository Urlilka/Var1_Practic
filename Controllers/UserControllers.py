from Models.Users import *

class UserController:

    @classmethod
    def get(cls):
        """Вывод Списка Пользхователей
        """
        return Users.select()
    
    @classmethod
    def add(cls, login, password, role_id = 2):
        """Добавление Пользователя

        Args:
            login (str): Имя пользователя
            password (str): Пароль пользователя
            role_id (int): Роль пользователя, ссылка на роль в таблице roles. По умолчанию 2.
        """
        Users.create(login=login, password=password, role_id=role_id)
    
    @classmethod
    def update(cls, id, **fields):
        """Обновление Пользователя

        Args:
            id (int): id обновляемого пользователя
            **fields: Обновляемый параметр = Значение
        """
        for key,value in fields.items():
            Users.update({key:value}).where(Users.id == id).execute()
    
    @classmethod
    def show(cls, login):
        """Вывод пользователя по логину, иначе ничего

        Args:
            login (str): Имя пользователя

        Returns:
            str: Имя пользователя из таблицы users, иначе None
        """
        return Users.get_or_none(Users.login == login)


    @classmethod
    def auth(cls, login, password):
        """Проверка пароля пользователя

        Args:
            login (str): Имя пользователя
            password (str): Парооль пользователя

        Returns:
            Model: выводит указанные данные пользователя, иначе False
        """
        cls.user = cls.show(login)
        if cls.user is not None:
            if cls.user.password == password:
                return cls.user
            else:
                return False
        else:
            return False

if __name__ == "__main__":
    # UserController.add("Admin","123456",role_id=1)
    # UserController.add("User","123456")

    for row in UserController.get():
        print(row.login,row.password,row.ban,row.first_auth,row.date_auth,row.role_id)

    # UserController.auth("Admin","123456")
    # print(UserController.auth("Admin","123456").login)
    # print(type(UserController.auth("Admin","123456")))