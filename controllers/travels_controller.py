from flask import Flask, render_template, request, redirect

from repositories import destination_repository, user_repository

from models.destination import Destination

from flask import Blueprint

destinations_blueprint = Blueprint("destinations", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/destinations'
@destinations_blueprint.route("/destinations")
def destinations():
    destinations = destination_repository.select_all()
    return render_template("destinations/index.html", all_destinations = destinations)

# NEW
# GET '/tasks/new'

# CREATE
# POST '/tasks'

# CREATE
# POST '/tasks'

# SHOW
# GET '/tasks/<id>'

# EDIT
# GET '/tasks/<id>/edit'

# UPDATE methods on task_controller method on html
# PUT '/tasks/<id>'

# DELETE
# DELETE '/tasks/<id>'