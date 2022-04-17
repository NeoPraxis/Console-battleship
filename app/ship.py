from coordinates import Coordinates


class Ship:
    
    models = {
        'Destroyer': 2,
        'Cruiser': 3,
        'Submarine': 3,
        'Battleship': 4,
        'Carrier': 5
    }

    def __init__(self, model, coordinates):
        self.size = self.models.get(model)
        self.model = model
        if self.size != len(coordinates):
            raise TypeError(f'{self.model} requires {self.size} coordinates')
        self.coordinates = coordinates
    
