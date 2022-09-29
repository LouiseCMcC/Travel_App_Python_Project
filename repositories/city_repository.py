from db.run_sql import run_sql

from models.sight import Sight
from models.country import Country
from models.city import City
from models.blog import Blog
from models.photo import Photo

import repositories.country_repository as country_repository
import pdb

# save
def save(city):
    sql = "INSERT INTO cities (city_name, country_id, visited) VALUES (%s, %s, %s) RETURNING id"
    values = [city.city_name, city.country.id, city.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city

# select_all
def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['city_name'], country, row['visited'], row['id'])
        cities.append(city)
    return cities

# select
def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        country = country_repository.select(result['country_id'])
        city = City(result['city_name'], country, result['visited'], result['id'])
    return city


# delete_all
def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)

# delete
def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# update
def update(city):
    sql = "UPDATE cities SET (city_name, country_id, visited) = (%s, %s, %s) WHERE id = %s"
    values = [city.city_name, city.country.id, city.visited, city.id]
    run_sql(sql, values)