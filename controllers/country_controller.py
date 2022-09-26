from flask import Flask, render_template, request, redirect
from flask import Blueprint

from repositories import country_repository as country_respository
from repositories import city_repository as city_repository

from models.city import City
from models.country import Country

countries_blueprint = Blueprint("countries", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/countries'
@countries_blueprint.route("/countries")
def countries():
    countries = country_respository.select_all()
    return render_template("countries/index.html", countries = countries)

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