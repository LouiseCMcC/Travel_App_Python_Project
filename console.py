import pdb

from models.destination import Destination
from models.user import User

import repositories.destination_repository as destination_repository
import repositories.user_repository as user_repository


# destination_repository.delete_all()
# user_repository.delete_all()

user1 = User("Indiana", "Jones")
user_repository.save(user1)
user2 = User("Lara", "Croft")
user_repository.save(user2)
user3 = User("Scarlett", "Marlowe")
user_repository.save(user3)

user_repository.select_all()

destination1 = Destination("Cairo", user1, "Egypt", "Africa", "Pyramids of Giza", False)
destination_repository.save(destination1)
destination2 = Destination("Palmyra", user2, "Syria", "Asia", "Roman Forum", True)
destination_repository.save(destination2)
destination3 = Destination("Paris", user3, "Europe", "France", "Catacombs", False)
destination_repository.save(destination3)

pdb.set_trace()

