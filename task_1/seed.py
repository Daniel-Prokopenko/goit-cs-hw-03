import sqlite3
from contextlib import contextmanager
from faker import Faker

database = "./test.db"
fake = Faker()


@contextmanager
def create_connection(db_file):
    """create a database connection to a SQLite database"""
    conn = sqlite3.connect(db_file)
    yield conn
    conn.commit()
    conn.close()


def create_fake_statuses(conn, n=3):
    """create fake status data"""
    statuses = ["new", "in progress", "completed"]
    sql = """ INSERT INTO status(name) VALUES(?) """
    cur = conn.cursor()
    for status in statuses[:n]:
        cur.execute(sql, (status,))
    conn.commit()


def create_fake_users(conn, n=10):
    """create fake user data"""
    sql = """ INSERT INTO users(fullname, email) VALUES(?, ?) """
    cur = conn.cursor()
    for _ in range(n):
        cur.execute(sql, (fake.name(), fake.email()))
    conn.commit()


def create_fake_tasks(conn, n=20):
    """create fake task data"""
    sql = """ INSERT INTO tasks(title, description, status_id, user_id) VALUES(?, ?, ?, ?) """
    cur = conn.cursor()
    for _ in range(n):
        title = fake.sentence(nb_words=4)
        description = fake.text(max_nb_chars=200)
        status_id = fake.random_int(min=1, max=3)  # Assuming we have 3 statuses
        user_id = fake.random_int(min=1, max=10)  # Assuming we have 10 users
        cur.execute(sql, (title, description, status_id, user_id))
    conn.commit()


if __name__ == "__main__":
    with create_connection(database) as conn:
        if conn is not None:
            create_fake_statuses(conn)
            create_fake_users(conn)
            create_fake_tasks(conn)
        else:
            print("Error! cannot create the database connection.")
