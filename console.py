import pdb

from models.city import City
from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

# city_repository.delete_all()
# country_repository.delete_all()

country1 = Country("Egypt", "Africa", True)
country_repository.save(country1)
country2 = Country("Syria", "Asia", False)
country_repository.save(country2)
country3 = Country("France", "Europe", True)
country_repository.save(country3)

country_repository.select_all()

city1 = City("Cairo", country1, True)
city_repository.save(city1)
city2 = City("Palmyra", country2, True)
city_repository.save(city2)
city3 = City("Paris", country3, True)
city_repository.save(city3)

city_repository.select_all()


pdb.set_trace()

