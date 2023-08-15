import mysql.connector
__cnx = None

def get_sql_connection():
    global __cnx
    if __cnx is None:
        cnx = mysql.connector.connect(user='root', password='BU$!ne55',
                                      host='127.0.0.1',
                                      database='abhijeet')

        return cnx
