from db.run_sql import run_sql

from models.sight import Sight
from models.country import Country
from models.city import City
from models.blog import Blog

import pdb

# select_all
def select_all():
    blogs = []

    sql = "SELECT * FROM blogs"
    results = run_sql(sql)

    for row in blogs:
        blog = Blog(row['blog_name'], row['blog_content'], row['id'])
        blogs.append(blog)
    return blogs