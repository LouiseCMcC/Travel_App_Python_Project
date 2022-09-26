from flask import Flask, render_template, request, redirect
from flask import Blueprint

from repositories import country_repository as country_respository
from repositories import city_repository as city_repository

from models.city import City
from models.country import Country

cities_blueprint = Blueprint("cities", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/cities'
@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", cities = cities)

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