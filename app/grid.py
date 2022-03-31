from coordinates import Coordinates
from ship import Ship
from shot import Shot
from coordinates import Coordinates

class Grid:
    x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    y = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    def __init__(self):
        self.ships: list[Ship] = []
        self.shots = []

    def add_ship(self, model, coordinates):
        ship = Ship(model, coordinates)
        self.ships.append(ship)

    def add_shot(self, coordinates):
        shot = Shot(coordinates)
        self.shots.append(shot)

    def is_model_already_placed(self, model):
        models = []
        for ship in self.ships:
            models.append(ship.model)
        is_model_placed = model in models
        return is_model_placed

    def is_ship_blocked(self, ship_coordinates: Coordinates):
        all_coordinates = self.get_all_ship_coordinates()
        for coordinate in ship_coordinates:
            if coordinate in all_coordinates:
                return True
        return False

    def get_all_ship_coordinates(self):
        coordinates = []

        for ship in self.ships:
            coordinates += ship.coordinates
        return coordinates


