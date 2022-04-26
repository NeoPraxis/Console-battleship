import sys, copy, time, io
from pynput.keyboard import Listener
from os import system, name



class ConsoleUI:
    
    def __init__(self, on_navigation = None, on_escape = None, on_space = None):
        self.listen_for_keyboard_events()
        self.keystrokes = ''
        self.accepted_input = ''
        self.single_character_input = True
        self.on_navigation = on_navigation
        self.on_escape = on_escape
        self.on_space = on_space
        self.console_x = 0
        self.console_y = 0
        self.console_width = None

    def print_xy(self, x, y, text, width = None):
        self.console_width = width

        if width:
            text = text.center(width)

        # Found this example to solve my printing issues in the console
        # https://stackoverflow.com/questions/7392779/is-it-possible-to-print-a-string-at-a-certain-screen-position-inside-idle
        sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
        sys.stdout.flush()

    def listen_for_keyboard_events(self):
        self.listener = Listener(
            on_press = self.on_press)
        self.listener.start()

    def on_press(self, key):
        key = str(key).replace("'", "")
        self.accepted_input = self.keystrokes
        if self.is_navigation_key(key) and self.on_navigation is not None:
            self.on_navigation(key)
        if self.is_alphanumeric_or_space(key):
            self.keystrokes += key
            if self.single_character_input:
                self.accept_and_clear_input()
            else:
                self.print_xy(self.console_x, self.console_y, self.keystrokes, self.console_width)

        if key == 'Key.enter':
            self.accept_and_clear_input()
        if key == 'Key.space' and self.on_space is not None:
            self.on_space(key)
        if key == 'Key.esc' and self.on_escape is not None:
            self.on_escape(key)
        
    def accept_and_clear_input(self):
        self.accepted_input = self.keystrokes
        self.keystrokes = ''
        return self.accepted_input

    def input(self, single_character_input = True, cursor_position = None):
        self.single_character_input = single_character_input
        if cursor_position:
            self.console_x = cursor_position['x']
            self.console_y = cursor_position['y']

        while not self.accepted_input:
            time.sleep(0.10)
        input_return_value = copy.deepcopy(self.accepted_input)
        self.accepted_input = ''
        return input_return_value
    
    def is_alphanumeric_or_space(self, char: str):
       is_alphanumeric = char.isalnum()
       is_space = char.isspace()
       return is_alphanumeric or is_space
        
    def is_navigation_key(self, key):
        navigation_keys = ['Key.up', 'Key.down', 'Key.left', 'Key.right']
        return key in navigation_keys

    def hide_cursor(self):
        print('\033[?25l', end="")

    def show_cursor(self):
        print('\033[?25h', end="")

    def clear_screen(self, stdout: io.StringIO = None):
        # for windows 
        if name == 'nt':
            _ = system('cls')
        if stdout:
            stdout.seek(0)
            stdout.truncate(0)
        else:
            sys.stdout.flush()

    
        # for mac and linux(here, os.name is 'posix')
        # else:
        #     _ = system('clear')