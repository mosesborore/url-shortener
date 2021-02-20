import os
import yaml
import psycopg2

YAML_FILE_PATH = __file__.replace("database.py", "config.yaml")

def activate_db():
    """ 
        creates a connection with the database
        returns the connection object
    """
    try:
        f = open(YAML_FILE_PATH, "r")
        config = yaml.load(f, Loader=yaml.FullLoader)

        connection = psycopg2.connect(host=config['host'], port=config['port'],
                                database=config['database'], user=config['user'], password=config['password'])

        if connection:
            return connection
    except Exception as e:
        print(f"Error! cannot connect to the database: {str(e)}")


def create_table():
    try:
        conn = activate_db()
        cursor = conn.cursor()

        query = """
            CREATE TABLE urlManager(
            id SERIAL PRIMARY KEY NOT NULL UNIQUE,
            long_url TEXT, short_url TEXT);
        """

        # create the table
        cursor.execute(query)
        commit_and_close_connection(conn)
        print('\nTable was created successfully\n')
    except psycopg2.errors.DuplicateTable as e:
        print(f"\ntable already exists:\n[CAUGHT ERROR] {str(e)}")


def commit_and_close_connection(connection):
    """ 
    commits and closes the connection to the database
    using the connection object passed as parameter
    """
    connection.commit()
    connection.close()

def insert_new_entry(long_url: str):
    """ inserts the new value into the table"""
    conn = activate_db()
    cursor = conn.cursor()

    query = f"INSERT INTO urlManager (long_url) VALUES (\'{long_url}\');"

    cursor.execute(query)
    commit_and_close_connection(conn)


def select_all():
    """returns all the information in the database"""
    try:
        conn = activate_db()
        cursor = conn.cursor()

        query = """
            SELECT EXISTS(
            SELECT * FROM urlManager);
        """
        cursor.execute(query)

        if cursor.fetchall():
            # if the table exists
            cursor.execute('SELECT * FROM urlManager;')
            return cursor.fetchall()
        conn.close()
    except psycopg2.errors.UndefinedTable:
        create_table()
        select_all()


def update_short_url(id, short_url: str):
    """
        updates 'short_url' the column with the shortened version
        of the value in 'url' column
    """

    conn = activate_db()
    cursor = conn.cursor()

    query = f""" UPDATE urlManager SET short_url = \'{short_url}\' WHERE id = {id}"""

    cursor.execute(query)
    commit_and_close_connection(conn)


def find_full_url(short_url):

    conn = activate_db()
    cursor = conn.cursor()

    cursor.execute(
        f"""SELECT long_url FROM urlmanager WHERE short_url=\'{short_url}\';""")

    return cursor.fetchall()[0][0]


def get_last_entry():
    query = """ SELECT * FROM urlManager ORDER BY id DESC LIMIT 1"""

    conn = activate_db()
    cursor = conn.cursor()

    cursor.execute(query)

    temp = cursor.fetchall()[0]

    data = {"id": temp[0], "long_url": temp[1], "short_url": temp[2]}

    return data

    conn.close()


if __name__ == '__main__':
    # insert_new_entry('https://second_entry.com.adasdasfdasdfdffasdasdasdasdasdasdasdda')
    print(select_all())
    print()
    print(get_last_entry()['id'])
    print(find_full_url(5))
