import random
from typing import List
from coordinates import Coordinates
from ship import Ship
from shot import Shot

class Grid:
    y = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    x = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    @staticmethod
    def get_random_coordinates() -> dict:
        return {'x': random.choice(Grid.x), 'y': random.choice(Grid.y)}, random.choice(['h', 'v'])
    
    def __init__(self):
        self.ships: list[Ship] = []
        self.shots: list[Shot] = []

    def add_ship(self, model, coordinates_list):
        ship = Ship(model, coordinates_list)
        is_model_placed: bool = self.is_model_already_placed(model)
        if is_model_placed:
            return

        is_overlapped = self.is_ship_blocked(coordinates_list)
        
        if is_overlapped:
            return

        for ship_coordinates in coordinates_list:
            ship_coordinates.model = model

        self.ships.append(ship)
        return True

    def add_shot(self, coordinates):
        shot = Shot(coordinates)
        self.shots.append(shot)

    def is_model_already_placed(self, model) -> bool:
        models = [ship.model for ship in self.ships]
        is_model_placed = model in models
        return is_model_placed

    def is_ship_blocked(self, ship_coordinates: Coordinates):
        all_coordinates = self.get_all_ship_coordinates()
        for coordinate in ship_coordinates:
            if coordinate in all_coordinates:
                return True
        return False

    def get_all_ship_coordinates(self) -> List[Coordinates]:
        coordinates = []

        for ship in self.ships:
            coordinates += ship.coordinates
        return coordinates

    def get_location_coordinates(self, model: str, location: dict, orientation: str):
        coordinates = []
        size = Ship.models[model]
        x_index = Grid.x.index(location['x'])
        y_index = Grid.y.index(location['y'])
        
        for z in range(0, size):
            
            exceeds_grid_boundary = x_index >= 10 or y_index >= 10

            if exceeds_grid_boundary:
                return []

            xy_location = {'y':Grid.y[y_index], 'x':Grid.x[x_index]}
            new_coordinates = Coordinates(location = xy_location)
            coordinates.append(new_coordinates)

            if orientation == 'h':
                x_index += 1
            
            else:
                y_index += 1

        return coordinates

    def is_shot_taken(self, coordinates: Coordinates):
        if Shot(coordinates) in self.shots:
            return True

    def take_a_shot(self, shot_coordinates: Coordinates):
        if not self.is_shot_taken(shot_coordinates):
            self.add_shot(shot_coordinates)
            self.record_a_hit(shot_coordinates)
            return True
    
    def record_a_hit(self, shot_coordinates: Coordinates):
        if not isinstance(shot_coordinates, Coordinates):
            raise f'shot_coordinates must be of type Coordinates'
        for ship_coordinates in self.get_all_ship_coordinates():
            if ship_coordinates == shot_coordinates:
                shot_coordinates.model = ship_coordinates.model
                ship_coordinates.hit = True
                shot_coordinates.hit = True
