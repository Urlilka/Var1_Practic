from Models.Base import *

class Roles(Base):
    """Таблица с ролями
    """
    id = PrimaryKeyField()
    role = CharField(unique=True,max_length=20)

if __name__ == "__main__":
    mysqlBD.create_tables([Roles])