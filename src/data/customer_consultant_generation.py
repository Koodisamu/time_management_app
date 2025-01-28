import psycopg2 as psycopg2
from config import config

# List of consultants
consultants_list = [
    'Anna Korhonen', 'Mikko Virtanen', 'Sanna Laine', 'Jari Mäkinen', 'Elina Niemi',
    'Juha Lehtonen', 'Laura Peltonen', 'Timo Aalto', 'Kati Heikkilä', 'Petri Rantanen',
    'Eeva Saarinen', 'Ville Hämäläinen', 'Noora Kallio', 'Antti Salonen', 'Riikka Toivonen',
    'Henri Lindholm', 'Mari Koskinen', 'Pekka Räsänen', 'Sami Virtanen', 'Krista Mäkelä'
]

# List of customers
customer_list= [
    'TechCorp', 'DataSoft', 'InnoGroup', 'FinConsult', 'BuildIT',
    'HealthPro', 'EduServices', 'GreenEnergy', 'MediaFlow', 'AutoTech'
]


# with psycopg2.connect(**config()) as conn:
#     with conn.cursor() as cur:
#         for row in consultants_list:
#             cur.execute('INSERT INTO d_consultants (name, location, email) VALUES (%s, %s, %s)', (row['name'], row['location'], row['email']))



def populate_customers_table():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        # Insert the customer data into the database
        SQL = '''
        INSERT INTO d_customers (customerName)
        VALUES (%s);
        '''
        for customer in customer_list:
            cursor.execute(SQL, (customer,))  # Pass a single-element tuple

        con.commit()
    except Exception as e:
        print("An error occurred:", e)
    finally:
        if con is not None:
            con.close()

def populate_consultants_table():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        # Insert the customer data into the database
        SQL = '''
        INSERT INTO d_consultants (consultantName)
        VALUES (%s);
        '''
        for consultant in consultants_list:
            cursor.execute(SQL, (consultant,))  # Pass a single-element tuple

        con.commit()
    except Exception as e:
        print("An error occurred:", e)
    finally:
        if con is not None:
            con.close()

if __name__ == '__main__':
    populate_consultants_table()


# def insert_many_vendors():
#     """ Insert multiple vendors into the vendors table  """
#     sql = "INSERT INTO vendors(vendor_name) VALUES(%s) RETURNING *"
#     config = load_config()
#     try:
#         with  psycopg2.connect(**config) as conn:
#             with  conn.cursor() as cur:
#                 # execute the INSERT statement
#                 cur.executemany(sql, vendor_list)
#             # commit the changes to the database
#             conn.commit()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)