one_to_one = ["""
CREATE TABLE User (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(100) NOT NULL
);


CREATE TABLE UserProfile (
    user_id INT PRIMARY KEY REFERENCES User(user_id),
    full_name VARCHAR(100),
    email VARCHAR(100) UNIQUE
);
""", """
CREATE TABLE Student (
    student_id SERIAL PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    enrollment_date DATE
);


CREATE TABLE StudentDetails (
    student_id INT PRIMARY KEY REFERENCES Student(student_id),
    address VARCHAR(200),
    contact_number VARCHAR(20)
);
""", """
CREATE TABLE Employee (
    employee_id SERIAL PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    hire_date DATE
);


CREATE TABLE Manager (
    manager_id SERIAL PRIMARY KEY,
    manager_name VARCHAR(100) NOT NULL,
    employee_id INT UNIQUE REFERENCES Employee(employee_id)
);
""", """
CREATE TABLE Customer (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE
);


CREATE TABLE BillingInformation (
    billing_id SERIAL PRIMARY KEY,
    credit_card_number VARCHAR(20),
    customer_id INT UNIQUE REFERENCES Customer(customer_id)
);
""", """
CREATE TABLE Company (
    company_id SERIAL PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    industry VARCHAR(50)
);


CREATE TABLE CEO (
    ceo_id SERIAL PRIMARY KEY,
    ceo_name VARCHAR(100) NOT NULL,
    company_id INT UNIQUE REFERENCES Company(company_id)
);
"""]

one_to_many = ["""
CREATE TABLE Department (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(50) NOT NULL
);


CREATE TABLE Employees (
    employee_id SERIAL PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    department_id INT REFERENCES Department(department_id)
);
""", """
CREATE TABLE Author (
    author_id SERIAL PRIMARY KEY,
    author_name VARCHAR(100) NOT NULL
);


CREATE TABLE Books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    publication_date DATE,
    author_id INT REFERENCES Author(author_id)
);
""", """
CREATE TABLE Customer (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    email VARCHAR(100)
);


CREATE TABLE Orders (
    order_id SERIAL PRIMARY KEY,
    order_date DATE,
    total_amount DECIMAL(10, 2),
    customer_id INT REFERENCES Customer(customer_id)
);
""", """
CREATE TABLE University (
    university_id SERIAL PRIMARY KEY,
    university_name VARCHAR(100) NOT NULL,
    location VARCHAR(50)
);


CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    university_id INT REFERENCES University(university_id)
);
""", """
CREATE TABLE Project (
    project_id SERIAL PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    start_date DATE,
    end_date DATE
);


CREATE TABLE Tasks (
    task_id SERIAL PRIMARY KEY,
    task_name VARCHAR(200) NOT NULL,
    project_id INT REFERENCES Project(project_id)
);
"""]


for i in range(0, 5):
    print(f"ONE TO ONE QUERY: {one_to_one[i]}\nONE TO MANY QUERY: {one_to_many[i]} ")

