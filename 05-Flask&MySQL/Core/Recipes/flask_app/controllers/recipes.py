from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

# ******  Route New Recipe *******  

@app.route('/recipes/new')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/')
    return render_template("new_recipe.html")

# ******  Route Create Recipe  *******  

@app.route('/recipes/create' , methods=['post'])
def add_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    data = {
        **request.form,
        'user_id':session['user_id']
    }
    Recipe.create_recipe(data)
    return redirect('/dashboard')


# ******  Route Edit Recipe  *******  


@app.route('/recipes/edit/<int:recipe_id>')
def edit_recipe(recipe_id):
    if 'user_id' not in session:
        return redirect('/')
    recipe =  Recipe.get_by_id({'id':recipe_id})
    return render_template("edit_recipe.html", recipe= recipe)



@app.route('/recipes/update', methods=['post'])
def update_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    Recipe.update(request.form)
    return redirect('/dashboard')

@app.route('/recipes/show/<int:recipe_id>')
def show_recipe(recipe_id):
    if 'user_id' not in session:
        return redirect('/')
    recipe = Recipe.get_by_id({'id':recipe_id})
    logged_user = User.get_by_id({'id':session['user_id']})
    return render_template("show_recipe.html", recipe=recipe, logged_user= logged_user)

@app.route('/recipes/delete/<int:recipe_id>')
def delete_recipe(recipe_id):
     if 'user_id' not in session:
        return redirect('/')
     Recipe.delete({'id':recipe_id})
     return redirect('/dashboard')