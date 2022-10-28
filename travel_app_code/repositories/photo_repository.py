from controllers.photo_controller import photos
from db.run_sql import run_sql

from models.sight import Sight
from models.country import Country
from models.city import City
from models.blog import Blog
from models.photo import Photo

import pdb

# save
def save(photo):
    sql = "INSERT INTO photos (photo_date, photo_location, photo_url) VALUES (%s, %s, %s) RETURNING *"
    values = [photo.photo_name, photo.photo_date, photo.photo_url]
    results = run_sql(sql, values)
    photo.id = results[0]['id']
    
    return photo 

# select_all
def select_all():
    photos = []

    sql = "SELECT * FROM photos"
    results = run_sql(sql)

    for row in photos:
        photo = Photo(row['photo_date'], row['photo_location'], row['photo_url'], row['id'])
        photos.append(photos)
    return photos

# select
def select(id):
    photo = None
    sql = "SELECT * FROM photos WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        photo = Photo(result['photo_date'], result['photo_location'], result['photo_url'], result['id'])
    return photo

# delete_all
def delete_all():
    sql = "DELETE FROM photos"
    run_sql(sql)

# delete
def delete(id):
    sql = "DELETE FROM photos WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# update
def update(photo):
    sql = "UPDATE photos SET (photo_date, photo_location, photo_url) = (%s, %s, %s) WHERE id = %s"
    values = [photo.photo_date, photo.photo_location, photo.photo_url, photo.id]
    run_sql(sql, values)