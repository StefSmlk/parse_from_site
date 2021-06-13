from mysql.connector import Error, connect


# def drop_table():
#     try:
#         with connect(
#                 host="localhost",
#                 user='stef',
#                 password='1234',
#                 database='some_companies',
#         ) as connection:
#             drop_table_query = "DROP TABLE companies"
#             with connection.cursor() as cursor:
#                 cursor.execute(drop_table_query)
#     except Error as e:
#         print(e)
#
#
# drop_table()

# def delete_from_table():
#     try:
#         with connect(
#                 host="localhost",
#                 user='stef',
#                 password='1234',
#                 database='some_companies',
#         ) as connection:
#             delete_query = "DELETE FROM companies"
#             with connection.cursor() as cursor:
#                 cursor.execute(delete_query)
#                 connection.commit()
#     except Error as e:
#         print(e)
#
#
# delete_from_table()


try:
    with connect(
            host="localhost",
            user='stef',
            password='1234',
            database='some_companies',
    ) as connection:
        select_movies_query = "SELECT * FROM companies"
        with connection.cursor() as cursor:
            cursor.execute(select_movies_query)
            result = cursor.fetchall()
            for row in result:
                print(row)
except Error as e:
    print(e)


def create_database():
    try:
        with connect(
                host="localhost",
                user='stef',
                password='1234',
        ) as connection:
            create_db_query = "CREATE DATABASE some_companies"
            with connection.cursor() as cursor:
                cursor.execute(create_db_query)
    except Error as e:
        print(e)


def create_table():
    try:
        with connect(
                host="localhost",
                user='stef',
                password='1234',
                database='some_companies',
        ) as connection:
            create_db_query = """CREATE TABLE companies (
                id INT AUTO_INCREMENT PRIMARY KEY,
                company_name VARCHAR(200) UNIQUE,
                ogrn BIGINT,
                okpo BIGINT,
                status VARCHAR(100),
                registration_date VARCHAR(100),
                capital VARCHAR(100)
                );"""
            with connection.cursor() as cursor:
                cursor.execute(create_db_query)
                connection.commit()
    except Error as e:
        print(e)


def insert_to_table(lst):
    try:
        with connect(
                host="localhost",
                user='stef',
                password='1234',
                database='some_companies',
        ) as connection:
            insert_movies_query = f"""
            INSERT INTO companies (company_name, ogrn, okpo, status, registration_date, capital) VALUES (
            '{lst[0]}', {lst[1]}, {lst[2]}, '{lst[3]}', {lst[4]}, {lst[5]}
            );
            """
            with connection.cursor() as cursor:
                cursor.execute(insert_movies_query)
                connection.commit()
    except Error as e:
        print(e)
