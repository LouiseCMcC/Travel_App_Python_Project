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
import pdb
sights_blueprint = Blueprint("sights", __name__)

# RESTful CRUD Routes

# # NEW
# GET '/tasks/new'
@sights_blueprint.route('/sights/new')
def new_sight():
    sights = sight_repository.select_all()
    cities = city_repository.select_all()
    return render_template('sights/new.html', sights = sights, cities = cities)

# # CREATE
# # POST '/tasks'
@sights_blueprint.route('/sights', methods=['POST'])
def create_sight():
    sight_name = request.form['sight_name']
    city_id = request.form['city_id']
    visited = request.form['visited']
    city = city_repository.select(city_id)
    sight = Sight(sight_name, city, visited)
    sight_repository.save(sight)
    return redirect('/sights')

# SHOW
# GET '/tasks/<id>'
@sights_blueprint.route('/cities/<id>/sights')
def show_sight(id):
    sight = sight_repository.select(id)
    sights = sight_repository.select_all()
    return render_template('sights/show.html', sight = sight, sights = sights)

# EDIT
# GET '/tasks/<id>/edit'
@sights_blueprint.route('/sights/<id>/edit')
def edit_sight(id):
    sight = sight_repository.select(id)
    sights = sight_repository.select_all()
    cities = city_repository.select_all()
    return render_template('sights/edit.html', sight = sight, sights = sights, cities = cities)

# # UPDATE 
# # PUT '/tasks/<id>'
@sights_blueprint.route('/sights/<id>', methods=['POST'])
def update_city(id):
    sight_name = request.form['sight_name']
    city_id = request.form['city_id']
    city = city_repository.select(city_id)
    visited = request.form['visited']
    sight_to_update = Sight(sight_name, city, visited, id)
    sight_repository.update(sight_to_update)
    return redirect('/sights')


# DELETE
# DELETE '/tasks/<id>'
@sights_blueprint.route('/sights/<id>/delete', methods=['POST'])
def delete_sight(id):
    sight_repository.delete(id)
    return redirect('/sights')


# # SEARCH '/cities/<id>/sights'
# @sights_blueprint.route("/cities/<id>/sights", methods=["POST", "GET"])
# def search(searched_sight):
#         sight = request.form["searched_sight"]
#         if sight == sight.sight_name:
#             return redirect('/cities/<id>/sights')
#         else:
#             return render_template("/")