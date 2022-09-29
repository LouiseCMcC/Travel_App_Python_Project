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

cities_blueprint = Blueprint("cities", __name__)

# RESTful CRUD Routes

# CITIES PAGE
@cities_blueprint.route("/cities")
def cities():
    return render_template("cities/index.html")

# INDEX
# GET '/cities'
# INDEX UNVISITED CITIES
@cities_blueprint.route("/cities/unvisited")
def unvisited_cities():
    cities = city_repository.select_all()
    return render_template("cities/unvisited.html", cities = cities)

# INDEX VISITED CITIES
@cities_blueprint.route("/cities/visited")
def visited_cities():
    cities = city_repository.select_all()
    return render_template("cities/visited.html", cities = cities)

# NEW
# GET '/tasks/new'
@cities_blueprint.route('/cities/new')
def new_city():
    cities = city_repository.select_all()
    countries = country_repository.select_all()
    return render_template('cities/new.html', cities = cities, countries = countries)

# CREATE
# POST '/tasks'
@cities_blueprint.route('/cities', methods=['POST'])
def create_city():
    city_name = request.form['city_name']
    country_id = request.form['country_id']
    visited = request.form['visited']
    country = country_repository.select(country_id)
    city = City(city_name, country, visited)
    city_repository.save(city)
    return redirect('/cities')

# SHOW
# GET '/tasks/<id>'
@cities_blueprint.route('/cities/<id>')
def show_city(id):
    city = city_repository.select(id)
    # country = country_repository.select(id)
    return render_template('cities/show.html', city = city)



# EDIT
# GET '/tasks/<id>/edit'
@cities_blueprint.route('/cities/<id>/edit')
def edit_city(id):
    city = city_repository.select(id)
    cities = city_repository.select_all()
    countries = country_repository.select_all()
    return render_template('cities/edit.html', city = city, cities = cities, countries = countries)

# UPDATE 
# PUT '/tasks/<id>'
@cities_blueprint.route('/cities/<id>', methods=['POST'])
def update_city(id):
    city_name = request.form['city_name']
    country_id = request.form['country_id']
    country = country_repository.select(country_id)
    visited = request.form['visited']
    city_to_update = City(city_name, country, visited, id)
    city_repository.update(city_to_update)
    return redirect('/cities')


# DELETE
# DELETE '/tasks/<id>'
@cities_blueprint.route('/cities/<id>/delete', methods=['POST'])
def delete_city(id):
    city_repository.delete(id)
    return redirect('/cities')