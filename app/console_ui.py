import sys, copy
#from pynput.keyboard import Listener


class ConsoleUI:
    
    def __init__(self):
        #self.listen_for_keyboard_events()
        self.keystrokes = ''
        self.input_return_value = ''
        self.single_character_input = True

    def print_xy(self, x, y, text):
        # Found this example to solve my printing issues in the console
        # https://stackoverflow.com/questions/7392779/is-it-possible-to-print-a-string-at-a-certain-screen-position-inside-idle
        sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
        sys.stdout.flush()

    # def listen_for_keyboard_events(self):
    #     self.listener = Listener(
    #         on_press = self.on_press)
    #     self.listener.start()

    def on_press(self, key):
        self.keystrokes += str(key).replace("'", "")
        self.input_return_value = self.keystrokes
        # Check for navigation keys (arrows) 
        # Check for enter key (confirm selection)
        # Check for escape key (exit)
        # Check for alphanum and spaces (name) (can use .upper/ .lower)

    def input(self, single_character_input = True):
        self.single_character_input = single_character_input
        while not self.input_return_value:
            pass
        input_return_value = copy.deepcopy(self.input_return_value)
        self.input_return_value = ''
        return input_return_value
    
    def is_alphanumeric_or_space(self, char: str):
       is_alphanumeric = char.isalnum()
       is_space = char.isspace()
       return is_alphanumeric or is_space
        