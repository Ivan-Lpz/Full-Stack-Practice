from pydoc import render_doc
from flask_app import app
from flask import Flask, render_template, request, redirect, session
from flask_app.models.users import User #user is the class name in the models user.py file
#and import any other models you use in this file!

@app.route("/users")
def index():
    all_users = User.get_all()
    print(all_users)
    return render_template("index.html", all_users = all_users)

@app.route("/users/new")
def create_user():
    return render_template("create.html")

@app.route("/create/user/submit",methods=["post"])
def submit_user():
    print(request.form)

    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
    }
    User.save(data)
    
    return redirect("/users")

@app.route("/users/<int:id>")
def single_user_page(id):
    print(f"looking for user with id: {id}")
    data = {
        "id": id
    }
    
    single_user = User.get_one(data)
    return render_template("single_user.html", single_user= single_user)

@app.route("/users/<int:id>/edit")
def edit_user_page(id):
    data = {
        "id": id
    }
    
    single_user = User.get_one(data)
    return render_template("edit.html", single_user= single_user)

@app.route("/create/user/<int:id>/submit_edit", methods=["post"])       #methods post is only when you are taking in information
def submit_edit(id):
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "id": id
    }

    User.submit_edit(data)

    return redirect("/users")

@app.route("/users/<int:id>/edit/delete")   
def delete_user(id):
    print(f"trying to delete user with id: {id}")
    data = {
        "id": id
    }
    
    User.delete_user(data)
    return redirect("/users")










