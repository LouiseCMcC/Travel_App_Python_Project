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

photos_blueprint = Blueprint("photos", __name__)

# PHOTOS PAGE
@photos_blueprint.route("/photos")
def photos():
    return render_template("photos/index.html")

# NEW
@photos_blueprint.route('/photos/new')
def new_photo():
    photos = photo_repository.select_all()
    return render_template('photos/new.html', photos = photos)

# ARCHIVE
@photos_blueprint.route('/photos/archive')
def archived_photos():
    photos = photo_repository.select_all()
    return render_template('/photos/archive.html', photos=photos)

# DELETE
@photos_blueprint.route('/photos/<id>/delete', methods=['POST'])
def delete_photo(id):
    photo_repository.delete(id)
    return redirect('/photos')


