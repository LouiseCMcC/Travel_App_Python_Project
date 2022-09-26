from db.run_sql import run_sql

from models.country import Country
from models.city import City

import repositories.country_repository as country_repository

# save
def save(city):
    sql = "INSERT INTO cities (city_name, country, visited) VALUES (%s, %s, %s) RETURNING *"
    values = [city.city_name, city.country, city.visited]
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
        country = country_repository.select(row['country_name'])
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



# def delete_all():
#     sql = "DELETE FROM destinations"
#     run_sql(sql)

# def delete(id):
#     sql = "DELETE FROM destinations WHERE id = %s"
#     values = [id]
#     run_sql(sql)

# def update(task):
#     sql = "DELETE destinations SET (user_id, continent, country, city, sight, visited) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
#     values = [destination.user.id, destination.continent, destination.country, destination.city, destination.sight, destination.completed, destination.id]
#     run_sql(sql, values)