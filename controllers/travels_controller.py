from flask import Flask, render_template, request, redirect

from repositories import country_repository, city_repository

from models.city import City
from models.country import Country

from flask import Blueprint

travels_blueprint = Blueprint("travels", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/countries'
@travels_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", all_countries = countries)

# INDEX
# GET '/cities'
@travels_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", all_cities = cities)

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