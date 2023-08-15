from sql_connection  import get_sql_connection
def get_all_products(connection):

    cursor = connection.cursor()

    query =("SELECT product.Product_id, product.Name, product.Un_id, product.Price_per_unit,un.Un_nm FROM abhijeet.product"
            " inner join abhijeet.un on product.Un_id=un.idUn_id;")
    cursor.execute(query)
    response = []
    for (Product_id, Name, Un_id, Price_per_unit, Un_nm ) in cursor:
        response.append(
            {
                'Product_id': Product_id,
                'Name' : Name,
                'Un_id' : Un_id,
                'Price_per_unit' : Price_per_unit,
                'Un_nm' :Un_nm
            }
        )

    return response

def insert_new_product(connection,products):
    cursor =connection.cursor()
    query=(" insert  into abhijeet.product "
           "(Product_id, Name, Un_Id, Price_per_unit) VALUES (%s,%s,%s,%s);")
    data=(products['Product_id'],products['product_name'], products['Un_id'], products['Price_per_value'])
    cursor.execute(query, data)
    connection.commit()
    return cursor.lastrowid

def delete_product(connection,Product_id):
    cursor = connection.cursor()
    query =("DELETE FROM abhijeet.product where Product_id=" +str(Product_id))
    cursor.execute(query)
    connection.commit()

if __name__=='__main__':
    connection = get_sql_connection()
    print(insert_new_product(connection,{
        'product_name':'VadaPav',
        'Un_id':'2',
        'Price_per_value':'12'

    }))

