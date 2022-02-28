from coordinates import Coordinates


class Ship:
    
    models  = {
        'Destroyer': 2,
        'Cruiser': 3,
        'Submarine': 3,
        'Battleship': 4,
        'Carrier': 5
    }

    def __init__(self, size, coordinates):
        self.size = size
        self.coordinates = coordinates
