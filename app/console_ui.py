import sys, copy
from pynput.keyboard import Listener


class ConsoleUI:
    
    def __init__(self):
        self.listen_for_keyboard_events()
        self.keystrokes = ''

    def print_xy(self, x, y, text):
        # Found this example to solve my printing issues in the console
        # https://stackoverflow.com/questions/7392779/is-it-possible-to-print-a-string-at-a-certain-screen-position-inside-idle
        sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
        sys.stdout.flush()

    def listen_for_keyboard_events(self):
        self.listener = Listener(
            on_press = self.on_press)
        self.listener.start()

    def on_press(self, key):
        self.keystrokes += key.char
        
    def input(self):
        while not self.keystrokes:
            pass
        keystrokes = copy.deepcopy(self.keystrokes)
        self.keystrokes = ''
        return keystrokes
        