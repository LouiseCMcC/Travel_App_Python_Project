from db.run_sql import run_sql

from models.country import Country
from models.city import City

# save
def save(country):
    sql = "INSERT INTO countries (country_name, continent, city, visited) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [country.country_name, country.continent, country.city, country.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country 

# select_all
def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(row['country_name'], row['continent'], row['city'], row['visited'], row['id'])
        countries.append(country)
    return countries

# select
def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        country = Country(result['country_name'], result['continent'], result['city'], result['visited'], result['id'])
    return country

# def delete_all():
#     sql = "DELETE FROM users"
#     run_sql(sql)

# def delete(id):
#     sql = "DELETE FROM users WHERE id = %s"
#     values = [id]
#     run_sql(sql)

# def update(user):
#     sql = "DELETE users SET (first_name, last_name) = (%s, %s) WHERE id = %s"
#     values = [user.first_name, user.last_name]
#     run_sql(sql, values)

