"""POSTGRESQLDA  MYSCHOOL DATABASE OCHIB OLISH KERAK AVVAL"""
"""PASSWORDNI HAM TO'G'RILAB RUN QILING"""

import psycopg2

hostname = 'localhost'
database = 'myschool'  # -------------------
username = 'postgres'
pwd = 'Odilov__69'  # ----------------------------
portid = 5432

cur = None
conn = None

try:
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=portid)

    cur = conn.cursor()

    """TABLE LAR YARATAMIZ"""

    create_bio = '''CREATE TABLE IF NOT EXISTS bio(
                            id               SERIAL,
                            region           CHAR(50) NOT NULL,
                            district         CHAR(50) NOT NULL,
                            adress           CHAR(100) NOT NULL,
                            schoolname       CHAR(50) NOT NULL,
                            area             REAL,
                            created          DATE,
                            isreconstructed  BOOLEAN,
                            isspecialized    BOOLEAN NOT NULL,
                            phone            CHAR(13) NOT NULL,
                            email            CHAR(50),
                            classes          INT NOT NULL,
                            allstudents      INT  NOT NULL)'''
    create_socialmedia = '''CREATE TABLE IF NOT EXISTS socialmedia(
                            id               SERIAL,
                            telegram         CHAR(50) NOT NULL,
                            instagram        CHAR(50),
                            facebook         CHAR(50),
                            twitter          CHAR(50),
                            youtube          CHAR(50))'''
    create_staff = '''CREATE TABLE IF NOT EXISTS staff(
                            id               SERIAL,
                            fname            CHAR(50) NOT NULL,
                            lname            CHAR(50) NOT NULL,
                            ismale           BOOLEAN NOT NULL,
                            age              INT NOT NULL,
                            position         CHAR(50) NOT NULL,
                            adress           CHAR(150) NOT NULL,
                            phone            CHAR(13) NOT NULL,
                            qualification    CHAR(50),
                            experience       INT,
                            joiningdate      DATE,
                            teachingsubject  CHAR(50))'''
    create_class = '''CREATE TABLE IF NOT EXISTS class(
                            id               SERIAL,
                            teacher          CHAR(50) NOT NULL,
                            degree           SMALLINT NOT NULL,
                            classname        CHAR(20) NOT NULL,
                            students         INT NOT NULL,
                            capitan          CHAR(150) NOT NULL)'''
    create_student = '''CREATE TABLE IF NOT EXISTS student(
                            id               SERIAL,
                            fname            CHAR(50) NOT NULL,
                            lname            CHAR(50) NOT NULL,
                            phone            CHAR(13),
                            age              SMALLINT NOT NULL,
                            ismale           BOOLEAN NOT NULL,
                            adress           CHAR(150) NOT NULL,
                            classname        CHAR(20) NOT NULL,
                            health           CHAR(50),
                            gpa              SMALLINT  NOT NULL)'''
    cur.execute('DROP TABLE IF EXISTS bio')
    cur.execute('DROP TABLE IF EXISTS socialmedia')
    cur.execute('DROP TABLE IF EXISTS staff')
    cur.execute('DROP TABLE IF EXISTS class')
    cur.execute('DROP TABLE IF EXISTS student')
    cur.execute(create_bio)
    cur.execute(create_socialmedia)
    cur.execute(create_staff)
    cur.execute(create_class)
    cur.execute(create_student)

    """BIOGA QIYMATLAR BERAMIZ"""
    print('\n..............Maktab haqidagi malumotlarni kiritamiz..................\n')
    region1 = input('viloyatni kiriting: ')
    district = input('Tuman/shaharni kiriting: ')
    adress1 = input('Qolgan toliq manzilni kiriting: ')
    schoolname = input('Maktab nomini kiriting: ')
    area = float(input('Maydonini kiriting: '))
    created = input('Qachon ishga tushgan(01.01.2000): ')
    isreconstructed = input('Maktab tamirlanganmi? (ha=true, yoq=false): ')
    isspecialized = input('Maktab ixtisoslashtirilgan maktabmi? (ha=true, yoq=false): ')
    phone1 = input('Telefon raqamni kiriting (+998941234567): ')
    email = input("Maktab aloqa pochtasini kiriting: ")
    classes = int(input("Maktabda nechta sinf bor: "))
    allstudents = int(input("Maktabdagi o'quvchilar sonini kiriting: "))

    insert_query1 = "INSERT INTO bio (region, district, adress, schoolname, area, created, isreconstructed, isspecialized, phone, email, classes, allstudents) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    insert_values1 = (
        region1, district, adress1, schoolname, area, created, isreconstructed, isspecialized, phone1, email, classes,
        allstudents)
    cur.execute(insert_query1, insert_values1)

    """SOCIAL MEDIA"""
    print('\n..............Maktab ijtimoiy tarmoqlarini kiritamiz..................\n')
    telegram = input('Telegram linkni kiriting: ')
    instagram = input('Instagram linkni kiriting: ')
    facebook = input('Facebook linkni kiriting: ')
    twitter = input('Twitter account linkini kiriting: ')
    youtube = input('YouTube kanal linkini kiriting: ')
    insert_query2 = "INSERT INTO socialmedia (telegram, instagram, facebook, twitter, youtube) VALUES (%s, %s, %s, %s, %s)"
    insert_values2 = (telegram, instagram, facebook, twitter, youtube)
    cur.execute(insert_query2, insert_values2)

    """STAFF"""
    insert_values3 = []
    print('\n................Maktab ishchilar malumotlarini kiritamiz...................\n')
    workers = int(input("necha hodim bor?: "))
    for worker in range(workers):
        print(f"\n\n{worker + 1}-hodim haqida malumotlar kiritamiz\n\n")
        fname1 = input('Hodim ismini kiriting: ')
        lname1 = input('Familiyasini kiriting: ')
        ismale1 = (input("Jinsi haqida malumot bering (erkek = true, ayol = false): "))
        age1 = int(input("Hodim yoshini kiriting: "))
        position = input('Lavozimni kiriting: ')
        adress2 = input("Hodim manzilini kiriting: ")
        phone2 = input('Telefon raqamni kiriting(+998941234567): ')
        qualification = input('Mutaxasisligini kiriting: ')
        experience = int(input("Ish tajriba yillarini raqamda kiriting: "))
        joiningdate = input('Ishga kirgan vaqtni kiriting (01.01.2001): ')
        teachingsubject = input('Oqitadigan fanni kiriting: ')
        values = (fname1, lname1, ismale1, age1, position, adress2, phone2, qualification, experience, joiningdate,
                  teachingsubject)
        insert_values3.append(values)
    insert_query3 = "INSERT INTO staff (fname, lname, ismale, age, position, adress, phone, qualification, experience, joiningdate, teachingsubject) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    for records1 in insert_values3:
        cur.execute(insert_query3, records1)
    """CLASS"""
    insert_values4 = []
    print('\n................Sinflar malumotlarini kiritamiz...................\n')
    groups = int(input("necha sinf bor?: "))
    for group in range(groups):
        print(f"\n\nnavbatdagi sinf haqida malumotlar kiritamiz\n\n")
        teacher = input('Oqituvchi ismi-sharfini kiriting: ')
        degree = int(input('Sinf darajasini kiriting (1, 4, 7, 11): '))
        classname1 = input('Sinf nomini kiriting (A, B, D, Y): ')
        students = int(input('Oquvchilar sonini kiriting: '))
        capitan = input("Sinf sardori ism-sharfini kiriting: ")
        values = (teacher, degree, classname1, students, capitan)
        insert_values4.append(values)
    insert_query4 = "INSERT INTO class (teacher, degree, classname, students, capitan) VALUES (%s, %s, %s, %s, %s)"
    for records2 in insert_values4:
        cur.execute(insert_query4, records2)
    """STUDENT"""
    insert_values5 = []
    print('\n................Studentlar malumotlarini kiritamiz...................\n')
    pupils = int(input("necha student bor?: "))
    for pupil in range(pupils):
        print(f"\n\nnavbatdagi o`quvchi haqida malumotlar kiritamiz\n\n")
        fname2 = input('Oquvchi ismini kiriting: ')
        lname2 = input('Familiyasini kiriting: ')
        phone3 = input('Telefon raqamni kiriting(+998941234567): ')
        age2 = int(input('Yoshini kiriting: '))
        ismale2 = (input("Jinsi haqida malumot bering (erkek = true, ayol = false): "))
        adress3 = input("Manzilini kiriting: ")
        classname2 = input("Sinfini kiriting: ")
        health = input("Sog'ligi haqida ma'lumot bering: ")
        gpa = int(input("Oxirgi o'quv yili bahosini (1-5) kiriting: "))
        values = (fname2, lname2, phone3, age2, ismale2, adress3, classname2, health, gpa)
        insert_values5.append(values)
    insert_query5 = "INSERT INTO student (fname, lname, phone, age, ismale, adress, classname, health, gpa) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    for records3 in insert_values5:
        cur.execute(insert_query5, records3)

    conn.commit()



except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
