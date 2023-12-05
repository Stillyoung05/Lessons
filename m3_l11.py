from psycopg2 import *
from pandas import *

db_info = {'host': 'localhost',
           'database': 'postgres',
           'user': 'postgres',
           'password': 'Odilov__69',
           'port': '5432'
           }
conn = connect(**db_info)
cur = conn.cursor()
create_query1 = """CREATE TABLE IF NOT EXISTS Courses (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(255) NOT NULL
);
"""
create_query2 = """CREATE TABLE IF NOT EXISTS Students (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE
);
"""
create_query3 = """Create table if not exists Enrollments (
    enrollment_id serial primary key,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    grade VARCHAR(2),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);
"""
select_query = """select
    Courses.course_id,
    Courses.course_name,
    COUNT(Enrollments.enrollment_id) AS enrollment_count
FROM
    Enrollments
JOIN

    Enrollments ON Courses.course_id = Enrollments.course_id
GROUP BY
    Courses.course_id, Courses.course_name
ORDER BY
    enrollment_count DESC
LIMIT 3;
"""
student_data = (1, 'Jamshid', 'Odilov', '03-09-2000')
insert_query = f"""insert in Students values{student_data}"""
course_data = (1, 'Web design')
insert_query2 = f"""insert in Courses values{course_data}"""
queries = [create_query1, create_query2, create_query3]
for j in queries:
    cur.execute(j)
my_query = read_sql(select_query, conn)
print(my_query)

conn.commit()
conn.close()
