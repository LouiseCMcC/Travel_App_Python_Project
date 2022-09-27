import pdb

from models.city import City
from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

city_repository.delete_all()
country_repository.delete_all()

country1 = Country("Egypt", "Africa", True)
country_repository.save(country1)
country2 = Country("Syria", "Asia", False)
country_repository.save(country2)
country3 = Country("France", "Europe", True)
country_repository.save(country3)
country4 = Country("Greece", "Europe", True)
country_repository.save(country4)
country5 = Country("Turkey", "Asia", False)
country_repository.save(country5)

country_repository.select_all()

city1 = City("Cairo", country1, True)
city_repository.save(city1)
city2 = City("Palmyra", country2, True)
city_repository.save(city2)
city3 = City("Paris", country3, True)
city_repository.save(city3)
city4 = City("Alexandria", country1, False)
city_repository.save(city4)
city5 = City("Damascus", country2, False)
city_repository.save(city5)
city6 = City("Nimes", country3, False)
city_repository.save(city6)
city7 = City("Athens", country4, True)
city_repository.save(city7)
city8 = City("Thessaloniki", country4, True)
city_repository.save(city8)
city9 = City("Istanbul", country5, True)
city_repository.save(city9)
city10 = City("Ephesus", country5, False)


city_repository.select_all()




