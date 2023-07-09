from flask import Flask, render_template, redirect, session, request
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/new/ninja/form')
def new_ninja_form():
    dojos = Dojo.get_all()
    return render_template('new_ninja.html', dojos=dojos)

######################## CREATE NEW NINJA ########################
@app.route('/add/ninja', methods=["POST"])
def new_ninja():
    selected_dojo_id = request.form['dojo']
    data = {
        "dojo_id": selected_dojo_id,
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age']
    }
    print(data['dojo_id'])
    Ninja.save(data)
    return redirect(f"/dojo/show/{selected_dojo_id}")
