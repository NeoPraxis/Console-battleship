from subprocess import call
import unittest, io
from unittest.mock import patch
from console_ui import ConsoleUI
from pynput.keyboard import Key, Controller
from threading import Timer


class TestConsoleUI(unittest.TestCase):

    def setUp(self) -> None:
        self.console_ui = ConsoleUI(self.on_navigation, self.on_escape)
        self.keyboard = Controller()
        self.time = 0
        self.handled_navigation_key = False
        self.handled_escape_key = False

    def on_navigation(self, navigation_key):
        self.handled_navigation_key = True

    def on_escape(self, escape_key):
        self.handled_escape_key = True

    def press(self, key):
        self.time += 0.2
        Timer(self.time, self.keyboard.press, ([key])).start()
        self.time += 0.3
        Timer(self.time, self.keyboard.release, ([key])).start()

    def test_if_console_ui_can_instantiate(self):
        
        self.assertIsInstance(self.console_ui, ConsoleUI)
        self.assertTrue(callable(self.console_ui.print_xy))
        self.assertTrue(callable(self.console_ui.listen_for_keyboard_events))
        self.assertTrue(callable(self.console_ui.on_press))
        self.assertIsInstance(self.console_ui.keystrokes, str)
        self.assertIsInstance(self.console_ui.single_character_input, bool)
        self.assertTrue(callable(self.console_ui.input))
        self.assertIsInstance(self.console_ui.accepted_input, str)
        self.assertTrue(callable(self.console_ui.is_alphanumeric_or_space))
        self.assertTrue(callable(self.console_ui.accept_and_clear_input))
        self.assertTrue(callable(self.console_ui.is_navigation_key))


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
            self.console_ui.accepted_input = 'W'
        Timer(0.2, set_response).start()
        input = self.console_ui.input(single_character_input = True)
        self.assertIn('W', input)

    def test_is_alphanumeric_or_space_returns_true_if_valid_text_entered(self):
        is_alphnum_or_space = self.console_ui.is_alphanumeric_or_space('a')
        self.assertTrue(is_alphnum_or_space)
        is_alphnum_or_space = self.console_ui.is_alphanumeric_or_space('A')
        self.assertTrue(is_alphnum_or_space)
        is_alphnum_or_space = self.console_ui.is_alphanumeric_or_space('1')
        self.assertTrue(is_alphnum_or_space)
        is_alphnum_or_space = self.console_ui.is_alphanumeric_or_space(' ')
        self.assertTrue(is_alphnum_or_space)
        
    def test_is_not_alphanumeric_returns_false_if_invalid_text_entered(self):
        is_non_alphnum = self.console_ui.is_alphanumeric_or_space('.')
        self.assertFalse(is_non_alphnum)
        is_non_alphnum = self.console_ui.is_alphanumeric_or_space('Key.enter')
        self.assertFalse(is_non_alphnum)
        is_non_alphnum = self.console_ui.is_alphanumeric_or_space('Key.up')
        self.assertFalse(is_non_alphnum)
        is_non_alphnum = self.console_ui.is_alphanumeric_or_space('Key.esc')
        self.assertFalse(is_non_alphnum)
        
        
    def test_when_enter_key_pressed_keystrokes_are_stored_in_input_return_value(self):
        Timer(0.1, lambda: self.console_ui.on_press('a')).start()
        Timer(0.6, lambda: self.console_ui.on_press('Key.enter')).start()
        input_value = self.console_ui.input()
        self.assertEqual(input_value, 'a')

    def test_accept_and_clear_input(self):
        accepted_input = self.console_ui.accept_and_clear_input()
        self.assertEqual(self.console_ui.keystrokes, '')
        self.assertEqual(self.console_ui.accepted_input, accepted_input)


    def test_when_spacebar_pressed_orientation_of_ship_toggles(self):
        pass

    def test_when_escape_key_pressed_stores_exit_in_input_return_value(self):
        self.console_ui.on_press('Key.esc')
        self.assertEqual(self.handled_escape_key, True)

    def test_is_navigation_key_returns_true_if_arrows_are_pressed(self):
        navigation_key_pressed = self.console_ui.is_navigation_key('Key.up')
        self.assertTrue(navigation_key_pressed)
        navigation_key_pressed = self.console_ui.is_navigation_key('Key.down')
        self.assertTrue(navigation_key_pressed)
        navigation_key_pressed = self.console_ui.is_navigation_key('Key.left')
        self.assertTrue(navigation_key_pressed)
        navigation_key_pressed = self.console_ui.is_navigation_key('Key.right')
        self.assertTrue(navigation_key_pressed)
        navigation_key_pressed = self.console_ui.is_navigation_key('Key.spacebar')
        self.assertFalse(navigation_key_pressed)
        navigation_key_pressed = self.console_ui.is_navigation_key('Key.esc')
        self.assertFalse(navigation_key_pressed)
        navigation_key_pressed = self.console_ui.is_navigation_key('Key.a')
        self.assertFalse(navigation_key_pressed)
        navigation_key_pressed = self.console_ui.is_navigation_key('Key.Z')
        self.assertFalse(navigation_key_pressed)

    def test_handle_cursor_movement_moves_cursor_when_arrow_key_is_pressed(self):
        self.console_ui.on_press('Key.up')
        self.assertEqual(self.handled_navigation_key, True)
