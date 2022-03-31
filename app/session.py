from coordinates import Coordinates
from player import Player
from turn import Turn
from ship import Ship
from shot import Shot

class Session:

    def __init__(self):
        self.__players = []
        self.__turns = []

    # Play a new game calls set up players, loop, get winner

    # Set up new game with players

    def set_player_name(self, player: Player):
        pass

    def add_player(self, player: Player):
        if len(self.__players) >= 2:
            return
        self.__players.append(player) 
        
    def number_of_players(self):
        return len(self.__players)

    def get_coordinates_from_player(self, player):
        location={'y':'A', 'x':'1'}
        return location, 'h'

    def place_ship_on_player_grid(self, player, model):
        location, orientation = self.get_coordinates_from_player(player)
        ship_coordinates = player.grid.get_location_coordinates(model, location, orientation)
        try:
            result = player.grid.add_ship(model, ship_coordinates)
        except:
            result = False
        return result

    def place_ships(self, player):
        for model in Ship.models:
            while not self.place_ship_on_player_grid(player, model):
                pass
    
        

    # Round Hand

    # Turn Handler for both players

    def add_turn(self, turn: Turn):
        self.__turns.append(turn)
    
    def number_of_turns(self):
        return len(self.__turns)

    # get shot from player
    def verify_a_shot(self, shot: Shot, player: Player) -> bool:
        # Boolean can be mathematical lmfao
        is_shot_verified = not not not player.grid.is_shot_taken(shot.coordinates)
        return is_shot_verified

    def record_a_shot(self, shot: Shot, player: Player) -> bool:
        is_shot_recieved = player.receive_a_shot(shot.coordinates)
        return is_shot_recieved
    # announce the turn results
    # Display Get Weener
