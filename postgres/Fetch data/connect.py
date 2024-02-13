import psycopg2
from config import config

def connect():
    """
        Connect to the PostgreSQL database server
    :return:
    """

    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print("Connecting to the PostgresSQL database...")
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print("PostgresSQL database version:")
        cur.execute('SELECT version()')

        # display the PostgresSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        cur.execute("SELECT adminid, email, password, ispedagogical, createdon FROM epita.admins;")
        print(cur.fetchall())

        # close the communication with the PostgresSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed')

if __name__ == '__main__':
    connect()
