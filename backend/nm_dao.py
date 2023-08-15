def get_uoms(connection):

    cursor=connection.cursor()
    query = ("SELECT * from abhijeet.un")
    cursor.execute(query)
    response = []
    i=0
    for (Un_id, Un_nm) in cursor:
        response.append({
            'idUn_id': Un_id,
            'Un_nm' : Un_nm,


        })

    return response

if __name__=='__main__':
    from sql_connection import get_sql_connection

    connection = get_sql_connection()
    print(get_uoms(connection))
