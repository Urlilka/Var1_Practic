from peewee import *

mysqlBD = MySQLDatabase(
    "GilAisp2_Var1_Prac",
    user = "GilAisp2_Admin",
    password = "000000",
    host = "10.11.13.118",
    port = 3306
)

if __name__ == "__main__":
    # print("GilAisp2_Admin")
    mysqlBD.connect()
    print("mysqlBD.connect()")