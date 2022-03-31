from coordinates import Coordinates

class Shot:
    
    def __init__(self, coordinates: Coordinates):
        
        self.coordinates: Coordinates = coordinates
    
    def __eq__(self, other):
        return self.coordinates.x == other.coordinates.x \
            and self.coordinates.y == other.coordinates.y
