import sqlite3
from contextlib import contextmanager

database = "./test.db"


@contextmanager
def create_connection(db_file):
    """create a database connection to a SQLite database"""
    conn = sqlite3.connect(db_file)
    yield conn
    conn.rollback()
    conn.close()


def create_table(conn, create_table_sql):
    """create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


if __name__ == "__main__":
    sql_create_status_table = """
    CREATE TABLE status (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE CHECK(name IN ('new', 'in progress', 'completed'))
    );"""

    sql_create_users_table = """
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname TEXT,
        email TEXT UNIQUE
    );"""

    sql_create_tasks_table = """
    CREATE TABLE tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        status_id INTEGER,
        user_id INTEGER,
        FOREIGN KEY (status_id) REFERENCES status (id),
        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
    );"""

    with create_connection(database) as conn:
        if conn is not None:
            create_table(conn, sql_create_users_table)
            create_table(conn, sql_create_status_table)
            create_table(conn, sql_create_tasks_table)
        else:
            print("Error! cannot create the database connection.")
