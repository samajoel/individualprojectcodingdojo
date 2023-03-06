
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash




class Saleyear:
    db_name = 'salesrevenue'

    def __init__(self,db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.sales = db_data['sales']


    @classmethod
    def sum_each(cls):
        query = "SELECT users.id as id, users.first_name, users.last_name, sum(sales.sale) as sales FROM users LEFT JOIN sales ON users.id=sales.user_id GROUP BY users.id;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_sales = []
        for row in results:
            all_sales.append( cls(row) )
        return all_sales
    

    @classmethod
    def sum_each_labels(cls):
        query = "SELECT users.id as id, users.first_name, users.last_name, sum(sales.sale) as sales FROM users LEFT JOIN sales ON users.id=sales.user_id GROUP BY users.id;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        
                                                # lista de objectos de la clase Saleyear
        labels = []
        for row in results:
            labels.append(row["first_name"])



        return labels




    @classmethod
    def sum_each_values(cls):
        query = "SELECT users.id as id, users.first_name, users.last_name, sum(sales.sale) as sales FROM users LEFT JOIN sales ON users.id=sales.user_id GROUP BY users.id;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        
                                                # lista de objectos de la clase Saley
    
        values = []
        for row in results:
            values.append(int(row["sales"]))
        return values
    

        
        
        
        
        
       