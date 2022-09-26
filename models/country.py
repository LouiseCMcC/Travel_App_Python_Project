class Country:
    def __init__(self, country_name, continent, city, visited = False, id = None):
        self.country_name = country_name
        self.continent = continent
        self.city = city
        self.visited = visited
        self.id = id

    def mark_visited(self):
        self.visited = True
        