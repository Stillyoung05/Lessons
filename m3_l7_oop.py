# from psycopg2 import *
#
#
# class DefaultDB:
#     def __init__(self):
#         self.connection = connect(dbname='postgres',
#                                   user='postgres',
#                                   password='Odilov__69',
#                                   host='localhost',
#                                   port=5432)
#         self.cursor = self.connection.cursor()
#         self.cursor.execute(f"""
#         create table if not exists phone1(
#         id serial,
#         phone1_name varchar(30) not null
#         );
#         """)
#         self.cursor.execute(f"""
# create table if not exists phone1(
# id serial primary key,
# phone1_name varchar(30) not null
# );
# """)
#
#     def insert_method(self):
#         self.cursor.execute(f"""
# insert into phone1 values
# (1,'black'),
# (2,'green'),
# (3,'white');
# insert into phone2 values
# (1,'light blue'),
# (2,'white'),
# (3,'black');
# """)
#         self.connection.commit()
#
#     def join_meth(self):
#         self.cursor.execute(f"""
# select phone1.id, phone1.phone1_name, phone2.id, phone2.phone2_name from phone1 inner join phone2 on phone1.phone1_name
# =phone2.phone2_name;
# """)
#
#     def fetch_data(self):
#         return self.cursor.fetchall()
#
#
# obj = DefaultDB()
# obj.insert_method()
# obj.join_meth()
# print(obj.fetch_data())
from psycopg2 import *
from deep_translator import *

dbname = 'postgres'
user = 'postgres'
password = 'Odilov__69'
host = 'localhost'
port = 5432


def translate(matn):
    resp = GoogleTranslator(source='uz', target='en').translate(matn)
    return resp


class MyData:
    def __init__(self):
        self.connection = connect(dbname=dbname,
                                  user=user,
                                  password=password,
                                  host=host,
                                  port=port)
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS dictionary(id INT, uzbek_word VARCHAR(45), english_word VARCHAR(45));")

    def add_data(self, id: int, uzbek: str, english: str):
        self.cursor.execute(f"INSERT INTO dictionary VALUES('{id}', '{uzbek}', '{english}');\n\n")
        self.connection.commit()

    def show_data(self):
        self.cursor.execute("SELECT * FROM dictionary;")

        return self.cursor.fetchall()


obj = MyData()

option = 1
index = 1
while option:
    option = int(input("\n\n1. Yangi so'z qo'shish\n2. So'zlarni ko'rish\n0. Chiqish\nKiritish: "))

    if option == 1:
        for i in range(1, int(input("\nNechta so'z qo'shasiz?: ")) + 1):
            uz = input(f"\n{i} so\'zni kiriting: ")
            obj.add_data(index, uz, translate(uz))
            index += 1
    elif option == 2:
        for i in obj.show_data():
            print(i)

