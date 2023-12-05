import psycopg2

db_host = "localhost"
db_name = "DATABASE NOMI"
db_user = "postgres"
db_password = "DATABASE PAROLI"

conn = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_password)
cursor = conn.cursor()
file_paths = ["""10 MOCKAROO DAN OLINGAN FAYL PATH LARI"""]

queries = []
a = "\\"
for o in file_paths:
    o.replace("/", a[0])
    queries.append("""{a[0]}i {l}""")

for query in queries:
    cursor.execute(query)
    result = cursor.fetchall()
    print(f"Query: {query}\nResult: {result}\n")

cursor.close()
conn.close()
