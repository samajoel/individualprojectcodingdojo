from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.sale import Sale
from flask_app.models.salesyear import Saleyear
from flask_app.models.salesmonth import Salemonth
from flask_bcrypt import Bcrypt
import json

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register',methods=['POST'])
def register():

    if not User.validate_register(request.form):
        return redirect('/')
    data ={ 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['user_id'] = id

    return redirect('/pdashboard')

       


@app.route('/login',methods=['POST'])
def login():
    user = User.get_by_email(request.form)

    if not user:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/pdashboard')



@app.route('/pdashboard', methods = ['GET'])
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }


     



        

    return render_template("pdashboard.html",
                           user=User.get_by_id(data),
                           recipes=Sale.get_all(), 
                           sum=Sale.sum(), 
                           salesyear=Saleyear.sum_each(), 
                           labels=json.dumps(Saleyear.sum_each_labels()), 
                           values=json.dumps(Saleyear.sum_each_values()), 
                           labels1=json.dumps(Salemonth.sum_each_labels1()), 
                           values1=json.dumps(Salemonth.sum_each_values1()))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')





@app.route('/edit/recipe/<int:id>')
def edit_user(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_recipe.html",edit=Sale.get_one(data),user=User.get_by_id(user_data))

@app.route('/update/recipe',methods=['POST'])
def update_user():
    if 'user_id' not in session:
        return redirect('/logout')
    if not User.validate_user(request.form):
        return redirect('/new/recipe')
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
    }
    User.update(data)
    return redirect('/pdashboard')

    