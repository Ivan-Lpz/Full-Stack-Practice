from pydoc import render_doc
from flask_app import app
from flask import Flask, render_template, request, redirect, session
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja


@app.route("/")
def index():
    dojos = Dojo.get_all()
    return render_template("index.html", dojos=dojos)

@app.route("/ninjas/new")
def new_ninjas():
    all_dojos = Dojo.get_all()

    return render_template("create_form.html",all_dojos=all_dojos)

@app.route("/ninjas/submit",methods=["post"])
def submit_ninjas():
    print(request.form)

    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["dojos_id"]
    }

    Ninja.save(data)
    return redirect("/")

@app.route("/dojos")
def display_dojo():
    all_ninjas = Ninja.get_all()
    print(all_ninjas)
    return render_template("index.html", all_ninjas=all_ninjas)

@app.route("/dojos/<int:id>")
def display_ninjas(id):
    data = {
        "id": id 
    }
    single_dojo = Dojo.get_one(data)
    all_ninjas = Ninja.get_all(data)
    return render_template("dojo_ninjas.html",single_dojo=single_dojo,all_ninjas=all_ninjas)

@app.route("/submit_dojo" ,methods=["post"])
def submit_dojo():
    data = {
        "name": request.form["name"]
    }
    Dojo.save(data)
    return redirect("/")