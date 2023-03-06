

from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Salemonth:
    db_name = 'salesrevenue'

    def __init__(self,db_data):
        self.month = db_data['month']
        self.sales = db_data['sales']
  


    @classmethod
    def sum_each_labels1(cls):
        query = "SELECT sales.month as month, sum(sales.sale) as sales FROM users JOIN sales ON users.id=sales.user_id GROUP BY sales.month;"
        results =  connectToMySQL(cls.db_name).query_db(query)                                       # lista de objectos de la clase Saleyear
        labels1 = []
        for row1 in results:
            labels1.append(row1["month"])
        return labels1




    @classmethod
    def sum_each_values1(cls):
        query = "SELECT sales.month as month, sum(sales.sale) as sales FROM users JOIN sales ON users.id=sales.user_id GROUP BY sales.month;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        values1 = []
        for row1 in results:
            values1.append(int(row1["sales"]))
        return values1
    

