import psycopg2
from psycopg2.extras import RealDictCursor
from config import config
import json
import datetime

# def db_get_attributes():
#     con = None
#     try:
#         con = psycopg2.connect(**config())
#         cursor = con.cursor(cursor_factory=RealDictCursor)
#         SQL = 'SELECT * FROM attributes;'
#         cursor.execute(SQL)
#         data = cursor.fetchall()
#         cursor.close()
#         return json.dumps({"attributes_list": data})
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if con is not None:
#             con.close()


def db_get_consultant():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor(cursor_factory=RealDictCursor)
        SQL = 'SELECT * FROM d_consultants;'
        cursor.execute(SQL)
        data = cursor.fetchall()
        cursor.close()
        return json.dumps({"consultant_list": data})
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def db_get_customer():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor(cursor_factory=RealDictCursor)
        SQL = 'SELECT * FROM d_customers;'
        cursor.execute(SQL)
        data = cursor.fetchall()
        cursor.close()
        return json.dumps({"customer_list": data})
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def db_log_hours(consultant_id = int, customer_id = int, startTime = datetime, endTime = datetime, lunchbreak = bool):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor(cursor_factory=RealDictCursor)
        SQL = 'INSERT INTO f_time_management (startTime, endTime, lunchbreak, consultant_id, customer_id) VALUES (%s, %s, %s, %s, %s);'
        cursor.execute(SQL, (startTime, endTime, lunchbreak, consultant_id, customer_id))
        con.commit()
        result = {"success": "logged hours for consultant id: %s " % consultant_id}
        cursor.close()
        return json.dumps(result)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

# def db_get_attribute_by_id(id):
#     con = None
#     try:
#         con = psycopg2.connect(**config())
#         cursor = con.cursor(cursor_factory=RealDictCursor)
#         SQL = 'SELECT * FROM attributes where id = %s;'
#         cursor.execute(SQL, (id,))
#         row = cursor.fetchone()
#         cursor.close()
#         return json.dumps(row)
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if con is not None:
#             con.close()
          
# def db_create_attribute(attribute_name, attribute_description, attribute_value, person_id):
#     con = None
#     try:
#         con = psycopg2.connect(**config())
#         cursor = con.cursor(cursor_factory=RealDictCursor)
#         SQL = 'INSERT INTO attributes (attribute_name, attribute_description, attribute_value, person_id) VALUES (%s, %s, %s, %s);'
#         cursor.execute(SQL, (attribute_name, attribute_description, attribute_value, person_id))
#         con.commit()
#         result = {"success": "created attribute name: %s " % attribute_name}
#         cursor.close()
#         return json.dumps(result)
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if con is not None:
#             con.close()

# def db_update_attribute(id, attribute_name, attribute_description, attribute_value, person_id):
#     con = None
#     try:
#         con = psycopg2.connect(**config())
#         cursor = con.cursor(cursor_factory=RealDictCursor)
#         SQL = 'UPDATE attributes SET attribute_name = %s, attribute_description = %s, attribute_value = %s WHERE person_id = %s;'
#         cursor.execute(SQL, (attribute_name, attribute_description, attribute_value, person_id))
#         con.commit()
#         cursor.close()
#         result = {"success": "updated attribute id: %s " % id}
#         return json.dumps(result)
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if con is not None:
#             con.close()

# def db_delete_attribute(id):
#     con = None
#     try:
#         con = psycopg2.connect(**config())
#         cursor = con.cursor(cursor_factory=RealDictCursor)
#         SQL = 'DELETE FROM attributes WHERE id = %s;'
#         cursor.execute(SQL, (id,))
#         con.commit()
#         cursor.close()
#         result = {"success": "deleted attribute id: %s " % id}
#         return json.dumps(result)
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if con is not None:
#             con.close()

if __name__ == '__main__':
      
    print(db_get_persons())    

            