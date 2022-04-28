from coordinates import Coordinates
from console_ui import ConsoleUI
from grid import Grid
from player import Player
class UI:
    
    def __init__(self):
        self.console_ui = ConsoleUI()
        self.cursor = {'y':'A', 'x':'1'}
        self.orientation = 'h'
        self.player = None

    def get_name(self):
        self.console_ui.clear_screen()
        self.console_ui.print_xy(1, 1, 'What is your name?: ', 60)
        self.console_ui.show_cursor()
        name = self.console_ui.input(single_character_input = False, cursor_position = {'x': 2, 'y': 1})
        self.console_ui.hide_cursor()
        return name

    def display_place_ship_instructions(self, model):
        self.console_ui.clear_screen()
        self.console_ui.print_xy(1, 1, f'1: Place your {model}', 60)
        self.console_ui.print_xy(2, 1, '2: Move arrow keys to navigate position.', 60)
        self.console_ui.print_xy(3, 1, '3: Press spacebar to change orientation.', 60)
        self.console_ui.print_xy(4, 1, f'4: Press enter to place your {model}.', 60)
    
    def place_ship(self, model: str, player: Player):
        self.player = player
        self.display_place_ship_instructions(model)
        self.print_grid(player)
        self.console_ui.input(on_navigation = self.on_navigation, on_space = self.on_space, on_enter = self.on_enter)
        return self.cursor, self.orientation

    def print_grid(self, player):
        grid_header = '   '.join(Grid.x)
        self.console_ui.print_xy(6, 1, f'    {grid_header} ', 60)
        grid_line = '+'.join('---' for x in Grid.x)
        self.console_ui.print_xy(7, 1, f'  |{grid_line}|', 60)

        for y in Grid.y:
            print_x = Grid.y.index(y) * 2 + 8
            row_string = f'{y} |'
            for x in Grid.x:
                grid_content = self.get_grid_content(player, y, x)
                row_string += f'{grid_content}|'
            self.console_ui.print_xy(print_x, 1, row_string, 60)
            self.console_ui.print_xy(print_x + 1, 1, f'  |{grid_line}|', 60)

    def get_grid_content(self, player: Player, y, x):
        grid_content = ' '
        all_ship_coordinates = player.grid.get_all_ship_coordinates()
        coordinates = Coordinates(location = {'y':y, 'x':x})
        match = list(filter(lambda c: c == coordinates, all_ship_coordinates))
        if match:
            grid_content = 'X' if match[0].hit else 'O'
        else:
            match = list(filter(lambda s: s.coordinates == coordinates, player.grid.shots))
            if match:
                grid_content = '*'
        is_cursor = self.cursor['x'] == x and self.cursor['y'] == y
        return f'[{grid_content}]' if is_cursor else f' {grid_content} '

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

    def on_space(self, key):
        self.orientation = 'v' if self.orientation == 'h' else 'h'
        if self.player:
            self.print_grid(self.player)

    def on_enter(self, key):
        pass 