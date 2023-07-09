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
    Ninja.save(data)
    return redirect(f"/dojo/show/{selected_dojo_id}")

######################## UPDATE NINJA ########################
@app.route('/edit/ninja/form/<int:ninja_id>')
def edit_ninja_form(ninja_id):
    ninja = Ninja.get_one(ninja_id)
    dojos = Dojo.get_all()
    return render_template('edit_ninja.html', ninja=ninja, dojos=dojos)

@app.route('/edit/ninja/info/<int:ninja_id>', methods=["POST"])
def update_ninja_info(ninja_id):
    selected_dojo_id = request.form['dojo']

    data = {
        'id':ninja_id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': selected_dojo_id
    }
    Ninja.update(data)
    return redirect(f"/dojo/show/{selected_dojo_id}")

######################## CREATE NEW NINJA ########################
######################## DELETE NINJA ########################
@app.route('/delete/ninja/<int:ninja_id>', methods=["POST"])
def delete_ninja(ninja_id):
    ninja = Ninja.get_one(ninja_id)
    dojo = ninja.dojo_id
    Ninja.delete_ninja(ninja_id)
    return redirect(f"/dojo/show/{dojo}")
