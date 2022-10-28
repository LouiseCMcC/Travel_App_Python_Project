# Travel_App Pseudocode:

# Create travel_manager database file.
# Create countries, cities and sights tables in travel_manager database.
# Countries table has fields id(serial primary key), name (varchar), continent(varchar) and visited(boolean).
# Cities table has fields id(serial primary key), name(varchar), country_id(foreign key from countries) and visited(boolean).
# Sights table has fields id(srrial primary key), name(varchar), city_id(foreign key from cities) and visited(boolean).
# drop db travel_manager.
# create db travel_manager.
# run psql to check tables exist in database.
# Create country, city and sight classes in models directory.
# Country class has name, continent and visited parameters.
# City class has name, country and visited parameters.
# Sight class has name, city and visited parameters.
# Create instances of these classes in the console file. 
# Write function to save instances in corresponding repository files -
# write sql commands to insert into table placeholders of the correspoding fields and the corresponding values, and return all.
# store these values as a list in a variable 'values'.
# call run_sql function.
# update the saved instance to have an id.



