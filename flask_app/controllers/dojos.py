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
    return render_template('dojo_show.html', dojo=dojo, ninjas=ninjas)

######################## UPDATE DOJO ########################


######################## DELETE DOJO ########################
