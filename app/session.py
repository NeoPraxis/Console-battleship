from coordinates import Coordinates
from player import Player
from turn import Turn
from ship import Ship
from shot import Shot
from grid import Grid

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
    # TODO keep playing ROUNDS until game is over
    def play_a_round(self):
        is_game_over = self.play_a_turn(self.__players[0], self.__players[1])
        if is_game_over:
            return is_game_over
        is_game_over = self.play_a_turn(self.__players[1], self.__players[0])
        return is_game_over

    def play_a_turn(self, player: Player, opponent: Player) -> bool:
        shot = self.get_verified_shot(player, opponent)
        recorded_shot = self.record_a_shot(shot, opponent)
        if recorded_shot:
            turn = Turn(shot, player)
            self.add_turn(turn)
        # TODO make test if player is Da Feet Ed, hit the grid in the player
        is_game_over = False
        return is_game_over

    def get_verified_shot(self, player: Player, opponent: Player) -> Shot:
        shot = None
        is_shot_verified = False
        while not is_shot_verified:
            # TODO get a shot from AI or UI \
            player_response = Grid.get_random_coordinates()
            xy_coordinates = player_response[0]
            shot_coordinates = Coordinates(xy_coordinates)
            shot = Shot(shot_coordinates)
            is_shot_verified = self.verify_a_shot(shot, opponent)
        return shot

    def add_turn(self, turn: Turn):
        self.__turns.append(turn)
    
    def number_of_turns(self):
        return len(self.__turns)

    def verify_a_shot(self, shot: Shot, player: Player) -> bool:
        # Boolean can be mathematical lmfao
        is_shot_verified = not not not player.grid.is_shot_taken(shot.coordinates)
        return is_shot_verified

    def record_a_shot(self, shot: Shot, player: Player) -> bool:
        is_shot_recieved = player.receive_a_shot(shot.coordinates)
        return is_shot_recieved
    # announce the turn results
    # Display Get Weener


