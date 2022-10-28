class City:
    def __init__(self, city_name, country, visited = False, id = None):
        self.city_name = city_name
        self.country = country
        self.visited = visited
        self.id = id

    def mark_visited(self):
        self.visited = True
