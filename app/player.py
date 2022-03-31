from grid import Grid
from coordinates import Coordinates

class Player:
    
    def __init__(self, name, is_ai):
        self.name = name
        self.grid = Grid()
        self.is_ai = is_ai

    def receive_a_shot(self, shot_coordinates: Coordinates) -> bool:
        shot_taken = self.grid.take_a_shot(shot_coordinates)
        return shot_taken

        
        