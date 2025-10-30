from Models.Base import *
from Models.Roles import Roles

class Users(Base):
    """Таблица с пользователями
    """
    id = PrimaryKeyField()
    login = CharField(unique=True,max_length=25)
    password = CharField()
    ban = BooleanField(default=False)
    first_auth = BooleanField(default=True)
    date_auth = DateField(null=True)
    role_id = ForeignKeyField(Roles)

if __name__ == "__main__":
    mysqlBD.create_tables([Users])