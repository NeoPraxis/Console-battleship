class Coordinates:

    x = ''
    y = ''

    def __init__(self, location: dict):
        self.y = location.get('y') 
        self.x = location.get('x')
        self.hit = False
        self.model = ''

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
