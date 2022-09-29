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

# CREATE
# POST '/tasks'
@blogs_blueprint.route('/blogs', methods=['POST'])
def create_blog():
    blog_name = request.form['blog_name']
    blog_date = request.form['blog_date']
    blog_content = request.form['blog_content']
    new_blog = Blog(blog_name, blog_date, blog_content)
    blog_repository.save(new_blog)
    return redirect('/blogs')

# ARCHIVE
@blogs_blueprint.route('/blogs/archive')
def archived_blogs():
    blogs = blog_repository.select_all()
    return render_template('/blogs/archive.html', blogs=blogs)

 # EDIT
# # GET '/tasks/<id>/edit'
@blogs_blueprint.route('/blogs/<id>/edit')
def edit_blog(id):
    blog = blog_repository.select(id)
    blogs = blog_repository.select_all()
    return render_template('blogs/edit.html', blog = blog, blogs = blogs)

# UPDATE 
# PUT '/tasks/<id>'
@blogs_blueprint.route('/blogs/<id>', methods=['POST'])
def update_blog(id):
    blog_name = request.form['blog_name']
    blog_date = request.form['blog_date']
    blog_content = request.form['blog_content']
    blog_to_update = Blog(blog_name, blog_date, blog_content, id)
    blog_repository.update(blog_to_update)
    return redirect('/blogs')

# DELETE
@blogs_blueprint.route('/blogs/<id>/delete', methods=['POST'])
def delete_blog(id):
    blog_repository.delete(id)
    return redirect('/blogs')


