from grid import Grid

class AI:
    
    def get_name(self):
        return 'AI'

    def place_ship(self):
        location, orientation = Grid.get_random_coordinates()
        return location, orientation

    def get_shot(self):
        location, orientation = Grid.get_random_coordinates()
        return location