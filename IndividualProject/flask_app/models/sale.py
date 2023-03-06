from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Sale:
    db_name = 'salesrevenue'

    def __init__(self,db_data):
        self.id = db_data['id']
        self.sale = db_data['sale']
        self.month = db_data['month']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.user_id = db_data['user_id']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO sales (sale, month, created_at, updated_at, user_id) VALUES (%(sale)s,%(month)s, NOW(), NOW(), %(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM sales;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_sales = []
        for row in results:
            all_sales.append( cls(row) )
        return all_sales
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM sales WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls( results[0] )

    @classmethod
    def update(cls, data):
        query = "UPDATE sales SET sale=%(sale)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM sales WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    


    @classmethod
    def user_sales(cls,data):
        query = "SELECT * FROM sales WHERE user_id = %(user_id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        user_sales = []
        for row in results:
            user_sales.append( cls(row) )
        return user_sales
    



    @classmethod
    def sum(cls):
        query = "SELECT * FROM sales;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_sales_2 = []
        for row in results:
            all_sales_2.append( cls(row) )  


            
        return sum(Sale.sale for Sale in  all_sales_2)
    


    @classmethod
    def sum_each_labels(cls):
        query = "SELECT users.id as id, users.first_name, users.last_name, sum(sales.sale) as sales FROM users LEFT JOIN sales ON users.id=sales.user_id GROUP BY users.id;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        
                                                # lista de objectos de la clase Saleyear
        labels1 = []
        for row in results:
            labels1.append(row["first_name"])



        return labels1
    



    @classmethod
    def sum_each_labels(cls):
        query = "SELECT users.id as id, users.first_name, users.last_name, sum(sales.sale) as sales FROM users LEFT JOIN sales ON users.id=sales.user_id GROUP BY users.id;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        
                                                # lista de objectos de la clase Saleyear
        values1 = []
        for row in results:
            values1.append(row["sales"])



        return values1
    



    @classmethod
    def user_sales_label(cls,data):
        query = "SELECT * FROM sales WHERE user_id = %(user_id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        labels2 = []
        for row in results:
            labels2.append(row["month"])



        return labels2
    

    @classmethod
    def user_sales_value(cls,data):
        query = "SELECT * FROM sales WHERE user_id = %(user_id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        values2 = []
        for row in results:
            values2.append(row["sale"])



        return values2
    
    



    










    


 




      








  
    

    








    


""" 
    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters","recipe")
        if len(recipe['instructions']) < 3:
            is_valid = False
            flash("Instructions must be at least 3 characters","recipe")
        if len(recipe['description']) < 3:
            is_valid = False
            flash("Description must be at least 3 characters","recipe") """