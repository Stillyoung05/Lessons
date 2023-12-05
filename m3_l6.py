from psycopg2 import *

dbname = 'postgres'
user = 'postgres'
password = 'Odilov__69'
host = 'localhost'
port = 5432

root1 = connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host,
    port=port
)
curs = root1.cursor()
for _ in range(20):
    root1.execute(
        """create table column_delete values(id bigint primary key, column1 varchar(20), column2 varchar(20);""")
column = input("Enter the name of column: ")
value = input("Enter the value of column: ")

delete_raw_query = (f"""
delete from  where {column} = {value};
""")

root1.commit()
curs.close()
root1.close()
