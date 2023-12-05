import psycopg2
from psycopg2 import sql


def create_database(database_name):
    connection = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="DATABASE PAROLI",
        database="postgres"
    )
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(database_name)))
    connection.close()
    connection = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="DATABASE PAROLI",
        database="postgres"
    )
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS table1 (
            ID SERIAL PRIMARY KEY,
            Name VARCHAR(255),
            Age INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS table2 (
            ProductID SERIAL PRIMARY KEY,
            ProductName VARCHAR(255),
            Price DECIMAL(10, 2)
        )
    ''')
    table_names = "table1", "table2"
    column_names = ["column1", "column2", "column3"]
    data = [
        (1, "QWERR", 20000),
        (1, "QWERН", 1000),
        (1, "QWERRНГШ", 45000)
    ]
    for n in table_names:
        insert_query = f"INSERT INTO {n} ({', '.join(column_names)}) VALUES %s;"

        cursor.executemany(insert_query, data)

        connection.commit()
    connection.close()

#
# for i in range(1, 6):
#     db_name = f'database{i}'
#     create_database(db_name)


# s = "dahdnasb osdfjsjd skdcksmxcz skdczxc"
# words = list(a for a in s.split())
# # print(words[::-1])
# ans = ""
# for j in words[::-1]:
#     ans += j + " "
#
# print(ans[:-1])

# print(m)

# def points(games):
#     score = 0
#     for j in games:
#         x = int(j[0])
#         y = int(j[2])
#         if x < y:
#             score += 3
#         if x == y:
#             score += 1
#         else:
#             score = score
#     return score
#
#
# d = points(["3:3"])
# print(d)


# def round_by_2_decimal_places(n):
#     return round(float(n), 2)


# j = round_by_2_decimal_places("2.4578")
# print(j)
