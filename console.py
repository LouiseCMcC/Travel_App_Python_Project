import pdb

from models.city import City
from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository


# city_repository.delete_all()
# country_repository.delete_all()



country_repository.select_all()
city_repository.select_all()

GO FROM HERE ***

destination1 = Destination("Cairo", user1, "Egypt", "Africa", "Pyramids of Giza", False)
city_repository.save(destination1)
destination2 = Destination("Palmyra", user2, "Syria", "Asia", "Roman Forum", True)
city_repository.save(destination2)
destination3 = Destination("Paris", user3, "Europe", "France", "Catacombs", False)
city_repository.save(destination3)

pdb.set_trace()

