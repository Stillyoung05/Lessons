import psycopg2
from prettytable import PrettyTable

db_config = {
    'host': 'localhost',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'Odilov__69',
    'port': '5432'
}


def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result


def display_results(results, headers):
    table = PrettyTable(headers)
    table.align = 'l'

    for row in results:
        table.add_row(row)

    print(table)


def main():
    try:
        connection = psycopg2.connect(**db_config)
        print("Connected to the database")

        query = "\d postgres"

        column_names = ["column1", "column2", "column3"]

        results = execute_query(connection, query)
        # display_results(results, column_names)
        print(results)
    except psycopg2.Error as e:
        print(f"Error: {e}")
    finally:
        if connection:
            connection.close()
            print("Connection closed")



