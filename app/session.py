from coordinates import Coordinates
from player import Player
from turn import Turn
from ship import Ship
from shot import Shot
from grid import Grid
from ai import AI
from ui import UI

class Session:

    def __init__(self):
        self.__players = []
        self.__turns = []
        self.ai = AI()
        self.ui = UI()

    def start_new_game(self):
        self.set_up_game()
        self.play_a_game()
        winner = self.get_winner()
        return winner

    def set_up_game(self):
        player = Player(' ', is_ai = False)
        opponent = Player('AI', is_ai = True)
        self.set_player_name(player)
        self.set_player_name(opponent)
        self.add_player(player)
        self.add_player(opponent)
        self.place_ships(player)
        self.place_ships(opponent)
        
    def set_player_name(self, player: Player):
        if player.is_ai == True:
            player.name = self.ai.get_name()
        else:
            player.name = self.ui.get_name()

    def add_player(self, player: Player):
        if len(self.__players) >= 2:
            return
        self.__players.append(player) 
        
    def number_of_players(self):
        return len(self.__players)

    def get_coordinates_from_player(self, player: Player, model: str):
        if player.is_ai == True:
            location, orientation = self.ai.place_ship()
            return location, orientation
        return self.ui.place_ship(model, player)
    
    def place_ship_on_player_grid(self, player: Player, model: str):
        location, orientation = self.get_coordinates_from_player(player, model)
        ship_coordinates = player.grid.get_location_coordinates(model, location, orientation)
        try:
            result = player.grid.add_ship(model, ship_coordinates)
        except:
            result = False
        return result
    
    def place_ships(self, player: Player):
        for model in Ship.models:
            while not self.place_ship_on_player_grid(player, model):
                pass
    
    def play_a_game(self) -> bool:
        is_game_over = False
        while not is_game_over:
            is_game_over = self.play_a_round()
        return is_game_over

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
            self.display_turn_results(player, shot)
        is_game_over = self.is_game_over()
        return is_game_over

    def get_shot_from_player(self, player: Player, opponent: Player):
        if player.is_ai == True:
            location = self.ai.get_shot()
        else:
            location = self.ui.get_shot(player, opponent)
        return location

    def get_verified_shot(self, player: Player, opponent: Player) -> Shot:
        shot = None
        is_shot_verified = False
        while not is_shot_verified:
            xy_coordinates = self.get_shot_from_player(player, opponent)
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
    
    def is_game_over(self):
        defeated_player = next((p for p in self.__players if p.is_defeated()), None)
        return defeated_player is not None

    def get_winner(self):
        winner = next((p for p in self.__players if not p.is_defeated()), None)
        return winner

    def display_turn_results(self, player: Player, shot: Shot):
        self.ui.turn_results(player, shot)

    def display_game_winner(self, player: Player):
        self.ui.game_results(player, self.number_of_turns())

