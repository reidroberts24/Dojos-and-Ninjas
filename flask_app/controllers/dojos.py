from flask import Flask, render_template, redirect, session, request
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def index():
    dojos= Dojo.get_all()
    return render_template("index.html",dojos=dojos)

######################## CREATE NEW DOJO ########################
@app.route('/add/dojo', methods=["POST"])
def new_dojo():
    data = {
        "name" : request.form['dojo_name'],
    }
    Dojo.save(data)
    return redirect('/')

######################## SHOW DOJO ########################
@app.route('/dojo/show/<int:dojo_id>')
def dojo_show(dojo_id):
    dojo = Dojo.get_one({'id':dojo_id})
    ninjas = Ninja.get_all({'dojo_id' : dojo_id})
    return_ninjas = []
    for ninja in ninjas:
        if ninja.dojo_id == dojo_id:
            return_ninjas.append(ninja)

    return render_template('dojo_show.html', dojo=dojo, ninjas=return_ninjas)


######################## UPDATE DOJO ########################


######################## DELETE DOJO ########################
@app.route('/delete/dojo/<int:dojo_id>', methods=["GET", "POST"])
def delete_dojo(dojo_id):
    ninjas = Ninja.get_all({"dojo_id": dojo_id})
    ####### delete all ninjas in the dojo before being able to remove the dojo itself
    for ninja in ninjas:
        if ninja.dojo_id == dojo_id:
            Ninja.delete_ninja(ninja.id)
    Dojo.delete_dojo({"id": dojo_id})
    return redirect("/")
