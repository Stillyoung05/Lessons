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

query = f"""
create table if not exists phone1(
id serial primary key, 
phone1_name varchar(30) not null
);
"""
query2 = f"""
create table if not exists phone2(
id serial primary key,
phone2_name varchar(30) not null
);
"""
insert_query1 = f"""
insert into phone1 values
(1,'black'),
(2,'green'), 
(3,'white');
"""
insert_query2 = f"""
insert into phone2 values(1,
'light blue'),
(2,'white'), 
(3,'black');
"""
join_method = f"""
select phone1.id, phone1.phone1_name, phone2.id, phone2.phone2_name from phone1 inner join phone2 on phone1.phone1_name
=phone2.phone2_name;
"""
curs.execute(query)
curs.execute(query2)
# curs.execute(insert_query1)
# curs.execute(insert_query2)
curs.execute(join_method)
x = curs.fetchall()
print(a for a in x)

root1.commit()
curs.close()
root1.close()
