import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """
    Create and connect to the sparkifydb and return the connection and 
    cursor to sparkifydb

    Returns
    -------
    cur : psycopg2.extensions.cursor
        a new cursor object to sparkifydb database

    conn : psycopg2.extensions.connection
        a new connection object to sparkifydb database   
    """
    # connect to default database
    try:
        conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    except psycopg2.Error as e:
        print("Error: Could not make connection to the Postgres database")
        print(e)

    try:
        cur = conn.cursor()
    except psycopg2.Error as e: 
        print("Error: Could not get cursor to the Database")
        print(e)

    conn.set_session(autocommit=True)

    # drop sparkify database with UTF8 encoding
    try:
        cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    except psycopg2.Error as e:
        print("Error: Dropping table")
        print(e)

    # create sparkify database with UTF8 encoding
    try:
        cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")
    except psycopg2.Error as e:
        print("Error: Issue creating table")
        print(e)
    
    # close cursor and connection to default database
    cur.close()
    conn.close()  

    # connect to sparkify database
    try:
        conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    except psycopg2.Error as e:
        print("Error: Could not make connection to the Postgres database")
        print(e)
    
    try:
        cur = conn.cursor()
    except psycopg2.Error as e: 
        print("Error: Could not get cursor to the Database")
        print(e)

    return cur, conn


def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    
    Parameters
    ----------
    cur : psycopg2.extensions.cursor
        a new cursor object to sparkifydb database

    conn : psycopg2.extensions.connection
        a new connection object to sparkifydb database   
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list. 

    Parameters
    ----------
    cur : psycopg2.extensions.cursor
        a new cursor object to sparkifydb database

    conn : psycopg2.extensions.connection
        a new connection object to sparkifydb database   
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    - Drops (if exists) and Creates the sparkifydb database. 
    
    - Establishes connection with the sparkify database and gets
    cursor to it.  
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """
    # Create database
    cur, conn = create_database()

    # drop database tables    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    # close cursor and connection to database
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
