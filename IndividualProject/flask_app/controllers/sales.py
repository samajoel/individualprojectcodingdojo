from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.sale import Sale
from flask_app.models.user import User


@app.route('/new/recipe')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('new_recipe.html',user=User.get_by_id(data))


@app.route('/create/recipe',methods=['POST'])
def create_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Sale.validate_recipe(request.form):
        return redirect('/new/recipe')
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "user_id": session["user_id"]
    }
    Sale.save(data)
    return redirect('/dashboard')
    





@app.route('/edit/month/<int:id>')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_month.html",edit=Sale.get_one(data),user=User.get_by_id(user_data))




@app.route('/update/month',methods=['POST'])
def update_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "sale": request.form["sale"],
        "id" : request.form["id"]
    }
    Sale.update(data)
    return redirect('/pdashboard')




@app.route('/udashboard/<int:id>')
def show_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "user_id":id
    }
    user_data = {
        "id":session['user_id']
      
    }
    return render_template("udashboard.html",
                           sales=Sale.user_sales(data),
                           user=User.get_by_id(user_data),
                           labels2=Sale.user_sales_label(data), 
                           values2=Sale.user_sales_value(data))




@app.route('/destroy/recipe/<int:id>')
def destroy_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Sale.destroy(data)
    return redirect('/dashboard')



