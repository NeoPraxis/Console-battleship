from console_ui import ConsoleUI

class UI:
    
    def __init__(self):
        self.console_ui = ConsoleUI()

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
        self.console_ui.print_xy(1, 1, '2: Move arrow keys to navigate position.', 60)
        self.console_ui.print_xy(1, 1, '3: Press spacebar to change orientation.', 60)
        self.console_ui.print_xy(1, 1, f'4: Press enter to place your {model}.', 60)
    
    def place_ship(self, model: str):
        self.display_place_ship_instructions(model)

        