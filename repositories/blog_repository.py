from db.run_sql import run_sql

from models.sight import Sight
from models.country import Country
from models.city import City
from models.blog import Blog
from models.photo import Photo

import pdb

# save
def save(blog):
    sql = "INSERT INTO blogs (blog_name, blog_date, blog_content) VALUES (%s, %s, %s) RETURNING *"
    values = [blog.blog_name, blog.blog_date, blog.blog_content]
    results = run_sql(sql, values)
    blog.id = results[0]['id']
    
    return blog 

# select_all
def select_all():
    blogs = []

    sql = "SELECT * FROM blogs"
    results = run_sql(sql)

    for row in blogs:
        blog = Blog(row['blog_name'], row['blog_content'], row['id'])
        blogs.append(blog)
    return blogs

# select
def select(id):
    blog = None
    sql = "SELECT * FROM blogs WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        blog = Blog(result['blog_name'], result['blog_date'], result['blog_content'], result['id'])
    return blog

# delete_all
def delete_all():
    sql = "DELETE FROM blogs"
    run_sql(sql)

# delete
def delete(id):
    sql = "DELETE FROM blogs WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# update
def update(blog):
    sql = "UPDATE blogs SET (blog_name, blog_date, blog_content) = (%s, %s, %s) WHERE id = %s"
    values = [blog.blog_name, blog.blog_date, blog.blog_content, blog.id]
    run_sql(sql, values)