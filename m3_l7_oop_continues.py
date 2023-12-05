from psycopg2 import *
# from deep_translator import *
from uuid import uuid4

dbname = 'postgres'
user = 'postgres'
password = 'Odilov__69'
host = 'localhost'
port = 5432


# def translate(matn):
#     resp = GoogleTranslator(source='uz', target='en').translate(matn)
#     return resp


class MyData:
    def __init__(self):
        self.connection = connect(dbname=dbname,
                                  user=user,
                                  password=password,
                                  host=host,
                                  port=port)
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            f"CREATE TABLE IF NOT EXISTS phones_m(id serial, name VARCHAR(20), model VARCHAR(40));")

    def add_date(self):
        amount = int(input("Enter amount of data: "))
        model = uuid4()
        for a in range(1, amount + 1):
            name = input(f"Enter name{a} for phone{a}: ")
            self.cursor.execute(f"""
            insert into phones_m values({a}, '{name}', '{model}');
            """)

    def fetch_data(self):
        self.cursor.execute("""select * from phones_m;""")
        return self.cursor.fetchall()


my_obj = MyData()
my_obj.add_date()
# print(my_obj.fetch_data())
for k in my_obj.fetch_data():
    print(k)
