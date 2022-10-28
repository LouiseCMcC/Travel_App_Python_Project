from db.run_sql import run_sql

from models.country import Country
from models.city import City
from models.sight import Sight
from models.blog import Blog
from models.photo import Photo

import repositories.city_repository as city_repository
import pdb

# save
def save(sight):
    sql = "INSERT INTO sights (sight_name, city_id, visited) VALUES (%s, %s, %s) RETURNING id"
    values = [sight.sight_name, sight.city.id, sight.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    sight.id = id
    return sight

# select_all
def select_all():
    sights = []

    sql = "SELECT * FROM sights"
    results = run_sql(sql)

    for row in results:
        city = city_repository.select(row['city_id'])
        sight = Sight(row['sight_name'], city, row['visited'], row['id'])
        sights.append(sight)
    return sights

# select
def select(id):
    sight = None
    sql = "SELECT * FROM sights WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        city = city_repository.select(result['city_id'])
        sight = Sight(result['sight_name'], city, result['visited'], result['id'])
    return sight

# delete_all
def delete_all():
    sql = "DELETE FROM sights"
    run_sql(sql)

# delete
def delete(id):
    sql = "DELETE FROM sights WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# update
def update(sight):
    sql = "UPDATE sights SET (sight_name, city_id, visited) = (%s, %s, %s) WHERE id = %s"
    values = [sight.sight_name, sight.city.id, sight.visited, sight.id]
    run_sql(sql, values) 


def search(sight_input):
    sql = "SELECT * FROM sights WHERE sight = %s"
    values = [sight_input]
    run_sql(sql, values)

