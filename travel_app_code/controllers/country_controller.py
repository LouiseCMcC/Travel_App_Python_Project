from flask import Flask, render_template, request, redirect
from flask import Blueprint

from repositories import country_repository as country_repository
from repositories import city_repository as city_repository
from repositories import sight_repository as sight_repository
from repositories import photo_repository as photo_repository

from models.city import City
from models.country import Country
from models.sight import Sight
from models.photo import Photo

countries_blueprint = Blueprint("countries", __name__)

# RESTful CRUD Routes

# COUNTRIES PAGE
@countries_blueprint.route("/countries")
def countries():
    return render_template("countries/index.html")

# GET '/countries'
# INDEX UNVISITED 
@countries_blueprint.route("/countries/unvisited")
def unvisited_countries():
    countries = country_repository.select_all()
    return render_template("countries/unvisited.html", countries = countries)

# INDEX VISITED
@countries_blueprint.route("/countries/visited")
def visited_countries():
    countries = country_repository.select_all()
    return render_template("countries/visited.html", countries = countries)

# NEW
# GET '/tasks/new'
@countries_blueprint.route('/countries/new')
def new_country():
    countries = country_repository.select_all()
    return render_template('countries/new.html', countries = countries)

# CREATE
# POST '/tasks'
@countries_blueprint.route('/countries', methods=['POST'])
def create_country():
    country_name = request.form['country_name']
    continent = request.form['continent']
    visited = request.form['visited']
    new_country = Country(country_name, continent, visited)
    country_repository.save(new_country)
    return redirect('/countries')

# SHOW
# GET '/tasks/<id>'
@countries_blueprint.route('/countries/<id>')
def show_country(id):
    country = country_repository.select(id)
    return render_template('countries/show.html', country = country)

# # EDIT
# # GET '/tasks/<id>/edit'
@countries_blueprint.route('/countries/<id>/edit')
def edit_country(id):
    country = country_repository.select(id)
    countries = country_repository.select_all()
    return render_template('countries/edit.html', country = country, countries = countries)

# UPDATE 
# PUT '/tasks/<id>'
@countries_blueprint.route('/countries/<id>', methods=['POST'])
def update_country(id):
    country_name = request.form['country_name']
    continent = request.form['continent']
    visited = request.form['visited']
    country_to_update = Country(country_name, continent, visited, id)
    country_repository.update(country_to_update)
    return redirect('/countries')

# DELETE
# DELETE '/tasks/<id>'
@countries_blueprint.route('/countries/<id>/delete', methods=['POST'])
def delete_country(id):
    country_repository.delete(id)
    return redirect('/countries')