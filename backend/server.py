from flask import Flask, request, jsonify
import products_dao
import nm_dao
import json
from sql_connection import get_sql_connection
app = Flask(__name__)
connection =get_sql_connection()


@app.route('/getProducts', methods=['GET'])
def get_products():
    product = products_dao.get_all_products(connection)
    response=jsonify(product)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/deleteProduct', methods=['POST'])
def delete_products():
    return_id = products_dao.delete_product(connection, request.form['Product_id'])
    response = jsonify({
        'Product_id' : return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertProduct', methods=['POST'])
def insertProduct():
    requestpayload = request.form['data']
    Product_id = products_dao.insert_new_product(connection , requestpayload)
    response = jsonify({
        'Product_id': Product_id
    })
    return response

    response.headers.add('Access-Control-Allow-Origin', '*')
@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = nm_dao.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ =='__main__':
    print("Starting Python Server for Abhijeet Grosery Store ")
    app.run(port=5000)
