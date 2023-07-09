
from flask_app import app
from flask_app.controllers import dojos, ninjas
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
if __name__=="__main__":
    app.run(debug=True)