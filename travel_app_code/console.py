import pdb

from models.sight import Sight
from models.city import City
from models.country import Country
from models.blog import Blog
from models.photo import Photo

import repositories.sight_repository as sight_repository
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.blog_repository as blog_repository
import repositories.photo_repository as photo_repository

city_repository.delete_all()
country_repository.delete_all()
sight_repository.delete_all()
blog_repository.delete_all()
photo_repository.delete_all()

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
city_repository.save(city10)

city_repository.select_all()

sight1 = Sight("Pyramids of Giza", city1, True)
sight_repository.save(sight1)
sight2 = Sight("Roman Forum", city2, False)
sight_repository.save(sight2)
sight3 = Sight("Catacombs", city3, True)
sight_repository.save(sight3)
sight4 = Sight("Bibliotecha Alexandria", city4, False)
sight_repository.save(sight4)
sight5 = Sight("Old City", city5, False)
sight_repository.save(sight5)
sight6 = Sight("Roman Ampitheatre", city6, False)
sight_repository.save(sight6)
sight7 = Sight("Acropolis", city7, True)
sight_repository.save(sight7)
sight8 = Sight("Greek Agora and Roman Forum", city8, True)
sight_repository.save(sight8)
sight9 = Sight("Serpentine Column", city9, True)
sight_repository.save(sight9)
sight10 = Sight("Ruins of Ephesus", city10, False)
sight_repository.save(sight10)
sight11 = Sight("Museum", city1, False)
sight_repository.save(sight11)

sight_repository.select_all()





