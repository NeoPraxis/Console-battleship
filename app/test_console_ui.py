from subprocess import call
import unittest, io
from unittest.mock import patch
from console_ui import ConsoleUI
from pynput.keyboard import Key, Controller
from threading import Timer


class TestConsoleUI(unittest.TestCase):
    
    def setUp(self) -> None:
        self.console_ui = ConsoleUI()
        self.keyboard = Controller()
        self.time = 0

    def press(self, key):
        self.time += 0.05
        Timer(self.time, self.keyboard.press, ([key])).start()
        self.time += 0.05
        Timer(self.time, self.keyboard.release, ([key])).start()

    def test_if_console_ui_can_instantiate(self):
        
        self.assertIsInstance(self.console_ui, ConsoleUI)
        self.assertTrue(callable(self.console_ui.print_xy))
        self.assertTrue(callable(self.console_ui.listen_for_keyboard_events))
        self.assertTrue(callable(self.console_ui.on_press))
        self.assertIsInstance(self.console_ui.keystrokes, str)
        self.assertTrue(callable(self.console_ui.input))


    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_xy_outputs_to_specified_location_in_console(self, mock_out):
        # TODO print something to console, and then after output i do my assert to check value
        self.console_ui.print_xy(1, 1, 'What is your name?: ')
        output = mock_out.getvalue()
        self.assertIn('What is your name?: ', output)
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_listen_for_keyboard_input(self, mock_out):
        # self.press('W')
        def set_response():
            self.console_ui.keystrokes = 'W'
        Timer(0.005, set_response).start()
        input = self.console_ui.input()
        self.assertIn('W', input)
