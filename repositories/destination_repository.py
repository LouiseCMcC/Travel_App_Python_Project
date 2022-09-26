from db.run_sql import run_sql

from models.user import User
from models.destination import Destination

import repositories.user_repository as user_repository

# save
def save(destination):
    sql = "INSERT INTO destinations (user_id, continent, country, city, sight, visited) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [destination.user.id, destination.continent, destination.country, destination.city, destination.sight, destination.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    destination.id = id
    return destination

# select_all
def select_all():
    destinations = []

    sql = "SELECT * FROM destinations"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select(row['user_id'])
        destination = Destination(user, row['continent'], row['country'], row['city'], row['sight'], row['visited'], row['id'])
        destinations.append(destination)
    return destinations 

# select
def select(id):
    destination = None
    sql = "SELECT * FROM destinations WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        user = user_repository.select(result['user_id'])
        destination = Destination(result['city'], user, result['country'], result['continent'], result['sight'], result['visited'], result['id'])
    return destination



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