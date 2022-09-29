from controllers.photo_controller import photos
from db.run_sql import run_sql

from models.sight import Sight
from models.country import Country
from models.city import City
from models.blog import Blog
from models.photo import Photo

import pdb

# select_all
def select_all():
    photos = []

    sql = "SELECT * FROM photos"
    results = run_sql(sql)

    for row in photos:
        photo = Photo(row['photo_name'], row['photo_content'], row['id'])
        photos.append(photos)
    return photos