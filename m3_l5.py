import psycopg2
from psycopg2 import sql


# dbname = 'postgres'
# user = 'postgres'
# password = ''
# host = 'localhost'
# port = 5432


def create_database(db_name, user, password, host="localhost", port=5432):
    try:
        connection = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="",
            host="localhost",
            port="5432"
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            create_db_query = sql.SQL("CREATE DATABASE {}").format(
                sql.Identifier(db_name)
            )
            cursor.execute(create_db_query)

        print(f"Database '{db_name}' created successfully.")
    except psycopg2.Error as e:
        print(f"Error creating database: {e}")
    finally:
        if connection:
            connection.close()


def delete_database(db_name, user, password, host="localhost", port=5432):
    try:
        connection = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Odilov__69",
            host="localhost",
            port="5432"
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            drop_db_query = sql.SQL(f"DROP DATABASE IF EXISTS {db_name}")

            cursor.execute(drop_db_query)

        print(f"Database '{db_name}' deleted successfully.")
    except psycopg2.Error as e:
        print(f"Error deleting database: {e}")
    finally:
        if connection:
            connection.close()


def create_table(table_name, columns, user, password, db_name, host="localhost", port=5432):
    try:
        connection = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="",
            host="localhost",
            port="5432"
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            columns_str = ', '.join([f"{col['name']} {col['type']}" for col in columns])
            create_table_query = sql.SQL("CREATE TABLE {} ({})").format(
                sql.Identifier(table_name),
                sql.SQL(columns_str)
            )
            cursor.execute(create_table_query)

        print(f"Table '{table_name}' created successfully.")
    except psycopg2.Error as e:
        print(f"Error creating table: {e}")
    finally:
        if connection:
            connection.close()


def delete_table(table_name, user, password, db_name, host="localhost", port=5432):
    try:
        connection = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="",
            host="localhost",
            port="5432"
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            drop_table_query = sql.SQL(f"DROP TABLE IF EXISTS {db_name}")
            cursor.execute(drop_table_query)

        print(f"Table '{table_name}' deleted successfully.")
    except psycopg2.Error as e:
        print(f"Error deleting table: {e}")
    finally:
        if connection:
            connection.close()


def copy_from_table(table_name, csv_file_path, user, password, db_name, host="localhost", port=5432):
    try:
        connection = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="",
            host="localhost",
            port="5432"
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            csv_file_path = "YOUR FILE PATH"
            copy_to_query = f"COPY {table_name} TO '{csv_file_path}' WITH CSV HEADER"
            cursor.execute(copy_to_query)

        print(f"Data from table '{table_name}' copied to '{csv_file_path}' successfully.")
    except psycopg2.Error as e:
        print(f"Error exporting data to CSV: {e}")
    finally:
        if connection:
            connection.close()



