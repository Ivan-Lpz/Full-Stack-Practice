from flask_app import app
from flask import Flask, render_template, request, redirect, session, flash
from flask_app.models.users import User
from flask_app.models.recipes import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["post"])
def register_user():
    # print("trying to register here")
    # print(request.form)
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": request.form["password"],
        "confirm_password": request.form["confirm_password"],
    }
    this_user = User.find_one_by_email(data)
    if this_user:
        flash("Email is already in use!")
        return redirect("/")

    
    if not User.validate(data):
        print("not valid")
        return redirect("/")

    #information is valid
    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    data["password"] = pw_hash
    # print(f"password: {request.form['password']}")
    # print(f"hashed password: {pw_hash}")


    user_id = User.save(data)
    session["logged_id"] = user_id
    
    return redirect("/recipes")


@app.route("/logout")
def logout():
    session.clear()        #session.clear will clear absolutely everything in the session 
    #del session["logged_id"]      del session at the value of "logged_id will only get rid of that part of session"
    return redirect("/")


@app.route("/recipes")
def success(): 
    if "logged_id" not in session:
        return redirect("/")
        #pull data for logged in user 

    data = {
        "id": session["logged_id"]

    }
    logged_user = User.find_one_by_id(data)
    # print(logged_user.id)
    #pull in data for all recipes
    all_recipes = Recipe.get_all()
    return render_template("main.html", logged_user=logged_user,all_recipes=all_recipes)

@app.route("/login", methods=["post"])
def login_user():
    
    data = {
        "email": request.form["email"]
    }
    
    this_user = User.find_one_by_email(data)
    if not this_user:
    #first thing we do is check if the user by that email exists 
    # and if they don't, flash message and redirect to form page
        flash("Invalid email/password")
        return redirect("/")
    #if it does exist
    #check the password, compare the hashed passwords to see if they are equal
    #if not equal then flash message and redirect to form page

    if not bcrypt.check_password_hash(this_user.password, request.form['password']):
        flash("Invalid email/password")
        return redirect("/")

    #if they are equal, you loggged in
    session["logged_id"] = this_user.id
    print("successful login")
    return redirect("/recipes")

    #END OF LOGIN AND REGISTRATION ROUTES  #END OF LOGIN AND REGISTRATION ROUTES #END OF LOGIN AND REGISTRATION ROUTES #END OF LOGIN AND REGISTRATION 

@app.route("/recipes/new")
def new_recipe():
    if "logged_id" not in session:
        return redirect("/")
    return render_template("create_recipe.html")

@app.route("/recipes/submit",methods=["post"])
def submit_recipes():
    #print(request.form)

    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "date_cooked": request.form["date_cooked"],
        "under_cert_time": request.form["under_cert_time"],
        "users_id": session["logged_id"]
    }
    validated = Recipe.validate(data)
    if not validated:
        return redirect("/recipes/new")
    

    Recipe.save(data)
    return redirect("/recipes")


@app.route("/recipes/single_recipe/<int:id>")
def single_recipe(id):
    
    data = {
        "id": id
    }
    user_data = {
        "id": session["logged_id"]
    }
    logged_user = User.find_one_by_id(user_data)
    print(logged_user)
    single_recipe = Recipe.get_one(data)
    return render_template("view_recipe.html", single_recipe=single_recipe,logged_user=logged_user)


@app.route("/recipes/edit/<int:id>")
def edit_recipe_page(id):
    if "logged_id" not in session:
        return redirect("/")
    data = {
        "id":id
    }
    single_recipe = Recipe.get_one(data)
    return render_template("edit.html", single_recipe=single_recipe)

@app.route("/recipes/edit/<int:id>/submit_edit", methods=["post"])
def submit_edit(id):
    print(id)
    if "under_cert_time" not in request.form:
        # flash("need the time value")
        # is_valid = False
        time = 1
    else:
        time = request.form["under_cert_time"]
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "date_cooked": request.form["date_cooked"],
        "under_cert_time": time,
        "id": id
        #"users_id": session["logged_id"]
    }
    validated = Recipe.validate(data)
    if not validated:
        return redirect("/recipes/edit/"+str(id))
    Recipe.submit_edit(data)
    return redirect("/recipes")


@app.route("/recipes/delete/<int:id>")
def delete_recipe(id):
    print(f"trying to delete user with id:{id}")
    data = {
        "id": id
    }
    Recipe.delete_recipe(data)
    return redirect("/recipes")



