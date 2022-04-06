from grid import Grid
from coordinates import Coordinates
from ship import Ship

class Player:
    
    def __init__(self, name, is_ai):
        self.name = name
        self.grid = Grid()
        self.is_ai = is_ai

    def receive_a_shot(self, shot_coordinates: Coordinates) -> bool:
        shot_taken = self.grid.take_a_shot(shot_coordinates)
        return shot_taken

    def is_defeated(self) -> bool:
        has_operational_ship = next((m for m in Ship.models.keys() if not self.grid.is_ship_sunk(m)), None)
        return not has_operational_ship
        
        
        