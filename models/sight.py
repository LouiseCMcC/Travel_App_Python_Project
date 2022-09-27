class Sight:
    def __init__(self, sight_name, city, visited, id = None):
        self.sight_name = sight_name
        self.city = city
        self.visited = visited
        self.id = id

    def mark_visited(self):
        self.visited = True