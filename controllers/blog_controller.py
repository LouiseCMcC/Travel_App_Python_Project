from flask import Flask, render_template, request, redirect
from flask import Blueprint

from repositories import blog_repository, country_repository as country_repository
from repositories import city_repository as city_repository
from repositories import sight_repository as sight_repository
from repositories import photo_repository as photo_repository

from models.city import City
from models.country import Country
from models.sight import Sight
from models.photo import Photo
import pdb

blogs_blueprint = Blueprint("blogs", __name__)

# BLOGS PAGE
@blogs_blueprint.route("/blogs")
def cities():
    return render_template("blogs/index.html")

# NEW
@blogs_blueprint.route('/blogs/new')
def new_blog():
    blogs = blog_repository.select_all()
    return render_template('blogs/new.html', blogs = blogs)

# ARCHIVE
@blogs_blueprint.route('/blogs/archive')
def archived_blogs():
    blogs = blog_repository.select_all()
    return render_template('/blogs/archive.html', blogs=blogs)


# DELETE

# DELETE_ALL
