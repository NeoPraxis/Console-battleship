
from coordinates import Coordinates
from console_ui import ConsoleUI
from grid import Grid
from player import Player
from shot import Shot
from ship import Ship
class UI:
    
    def __init__(self):
        self.console_ui = ConsoleUI()
        self.cursor = {'y':'A', 'x':'1'}
        self.orientation = 'h'
        self.player = None
        self.opponent = None
        self.is_placing_ship = False
        self.place_ship_model = ''
        self.keystrokes = ''

    def get_name(self):
        self.console_ui.clear_screen()
        self.console_ui.print_xy(1, 1, 'What is your name?: ', 60)
        self.console_ui.show_cursor()
        name = self.console_ui.input(
            single_character_input = False, 
            cursor_position = {'x': 2, 'y': 1},
            on_alphanumeric = self.on_alphanumeric
        )

        self.console_ui.hide_cursor()
        return name

    def display_place_ship_instructions(self, model):
        self.console_ui.clear_screen()
        self.console_ui.print_xy(1, 1, f'1: Place your {model}', 60)
        self.console_ui.print_xy(2, 1, '2: Move arrow keys to navigate position.', 60)
        self.console_ui.print_xy(3, 1, '3: Press spacebar to change orientation.', 60)
        self.console_ui.print_xy(4, 1, f'4: Press enter to place your {model}.', 60)
    
    def place_ship(self, model: str, player: Player):
        self.is_placing_ship = True
        self.place_ship_model = model
        self.player = player
        self.display_place_ship_instructions(model)
        self.print_grid(player)
        self.console_ui.input(on_navigation = self.on_navigation, on_space = self.on_space)
        self.is_placing_ship = False
        return self.cursor, self.orientation
    
    def get_shot(self, player: Player, opponent: Player):
        self.player = player
        self.opponent = opponent
        self.print_grid(player, is_targeting = False)
        self.print_grid(opponent, is_targeting = True)
        self.console_ui.input(on_navigation = self.on_navigation)
        return self.cursor

    def print_grid(self, player: Player, is_targeting: bool = False):
        left = 61 if is_targeting else 1
        self.console_ui.print_xy(5, left, 'Target Grid' if is_targeting else 'Ocean Grid', 60)
        grid_header = '   '.join(Grid.x)
        self.console_ui.print_xy(6, left, f'    {grid_header} ', 60)
        grid_line = '+'.join('---' for x in Grid.x)
        self.console_ui.print_xy(7, left, f'  |{grid_line}|', 60)
        all_ship_coordinates = player.grid.get_all_ship_coordinates()
        if self.is_placing_ship:
            ship_cursor = player.grid.get_location_coordinates(self.place_ship_model, self.cursor, self.orientation)
            all_ship_coordinates += ship_cursor

        for y in Grid.y:
            print_x = Grid.y.index(y) * 2 + 8
            row_string = f'{y} |'
            for x in Grid.x:
                grid_content = self.get_grid_content(player, y, x, all_ship_coordinates, is_targeting)
                row_string += f'{grid_content}|'
            self.console_ui.print_xy(print_x, left, row_string, 60)
            self.console_ui.print_xy(print_x + 1, left, f'  |{grid_line}|', 60)

    def get_grid_content(self, player: Player, y, x, all_ship_coordinates, is_targeting: bool = False):
        grid_content = ' '
        coordinates = Coordinates(location = {'y':y, 'x':x})
        if is_targeting:
            all_ship_coordinates = []
        match = list(filter(lambda c: c == coordinates, all_ship_coordinates))
        if match:
            grid_content = 'X' if match[0].hit else 'O'
        else:
            match = list(filter(lambda s: s.coordinates == coordinates, player.grid.shots))
            if match:
                grid_content = 'X' if match[0].coordinates.hit else '*'
        
        is_cursor = self.cursor['x'] == x and self.cursor['y'] == y and (self.is_placing_ship or is_targeting)
        return f'[{grid_content}]' if is_cursor else f' {grid_content} '
    
    def on_alphanumeric(self, key):
        self.keystrokes += key

    def on_navigation(self, key):
        x_index = Grid.x.index(self.cursor['x'])
        y_index = Grid.y.index(self.cursor['y'])

        if 'Key.right' == key and x_index < len(Grid.x) - 1:
            self.cursor['x'] = Grid.x[x_index + 1]
        
        if 'Key.left' == key and x_index > 0:
            self.cursor['x'] = Grid.x[x_index - 1]

        if 'Key.down' == key and y_index < len(Grid.y) - 1:
            self.cursor['y'] = Grid.y[y_index + 1]

        if 'Key.up' == key and y_index > 0:
            self.cursor['y'] = Grid.y[y_index - 1]

        if self.player:
            self.print_grid(self.player)
            if not self.is_placing_ship:
                self.print_grid(self.opponent, is_targeting = True)
                
    def on_space(self, key):
        self.orientation = 'v' if self.orientation == 'h' else 'h'
        if self.player:
            self.print_grid(self.player)

    def on_enter(self, key):
        pass 

    def turn_results(self, player: Player, shot: Shot):
        hit_result = f'{player.name} scored a hit on {shot.coordinates.model}' if shot.coordinates.hit else ' '*60
        left = 1 if player.is_ai else 61
        self.console_ui.print_xy(1, left, hit_result, 60)
        is_sunk = shot.coordinates.hit and self.opponent.grid.is_ship_sunk(shot.coordinates.model)
        sunk_result = f'{player.name} sunk {shot.coordinates.model}' if is_sunk else ' '*60
        self.console_ui.print_xy(2, left, sunk_result, 60)
        self.console_ui.print_xy(3, left, ' '*60, 60)
        self.console_ui.print_xy(4, left, ' '*60, 60)

    def game_results(self, player: Player, number_of_turns: int):
        left = 1 if player.is_ai else 61
        game_result = f'{player.name} is victorious!'
        self.console_ui.print_xy(3, left, game_result, 60)
        self.console_ui.print_xy(4, left, f'in {int(number_of_turns / 2)} turns', 60)
        self.console_ui.input(on_navigation = self.on_navigation)
