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

    