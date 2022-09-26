class Destination:
    def __init__(self, city, user, country, continent, sight, visited = False, id = None):
        self.city = city
        self.user = user
        self.country = country
        self.continent = continent
        self.sight = sight
        self.visited = visited
        self.id = id

def mark_visited(self):
    self.visited = True
