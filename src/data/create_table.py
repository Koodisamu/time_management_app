import psycopg2 as psycopg2
from config import config

def create_table_customer():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = """
        CREATE TABLE d_customers
        (id SERIAL PRIMARY KEY,
        customerName VARCHAR(50) NOT NULL
        );
        """
        cursor.execute(SQL)
        con.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def create_table_consultant():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = """
        CREATE TABLE d_consultants
        (id SERIAL PRIMARY KEY,
        consultantName VARCHAR(50) NOT NULL
        );
        """
        cursor.execute(SQL)
        con.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def create_table_fact():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = """
        CREATE TABLE f_time_management
        (id SERIAL PRIMARY KEY,
        startTime TIMESTAMP,
        endTime TIMESTAMP,
        lunchBreak BOOLEAN,
        consultant_id INTEGER,
        customer_id INTEGER,
        CONSTRAINT fk_consultant FOREIGN KEY (consultant_id) REFERENCES d_consultants(id),
        CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES d_customers(id)
        );
        """
        cursor.execute(SQL)
        con.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

if __name__ == '__main__':
    #create_table_customer()
    #create_table_consultant()
    #create_table_fact()