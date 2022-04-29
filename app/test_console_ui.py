
import unittest, io
from unittest.mock import patch
from console_ui import ConsoleUI
from pynput.keyboard import Key, Controller
from threading import Timer


class TestConsoleUI(unittest.TestCase):

    def setUp(self) -> None:
        self.console_ui = ConsoleUI(self.on_navigation, self.on_escape, self.on_space, self.on_enter)
        self.keyboard = Controller()
        self.time = 0
        self.handled_navigation_key = False
        self.handled_escape_key = False
        self.handled_space_key = False
        self.handled_enter_key = False

    def get_name(self):
        self.console_ui.print_xy(1, 1, 'What is your name?: ', 60)

    def on_navigation(self, navigation_key):
        self.handled_navigation_key = True

    def on_escape(self, escape_key):
        self.handled_escape_key = True

    def on_space(self, space_key):
        self.handled_space_key = True

    def on_enter(self, enter_key):
        self.handled_enter_key = True

    def press(self, key):
        self.time += 0.2
        Timer(self.time, self.keyboard.press, ([key])).start()
        self.time += 0.3
        Timer(self.time, self.keyboard.release, ([key])).start()

    def test_if_console_ui_can_instantiate(self):
        
        self.assertIsInstance(self.console_ui, ConsoleUI)
        self.assertIsInstance(self.console_ui.keystrokes, str)
        self.assertIsInstance(self.console_ui.single_character_input, bool)
        self.assertIsInstance(self.console_ui.accepted_input, str)
        self.assertTrue(callable(self.console_ui.on_alphanumeric))
        self.assertTrue(callable(self.console_ui.on_navigation))
        self.assertTrue(callable(self.console_ui.on_space))
        self.assertTrue(callable(self.console_ui.on_escape))
        self.assertTrue(callable(self.console_ui.on_enter))
        self.assertTrue(callable(self.console_ui.print_xy))
        self.assertTrue(callable(self.console_ui.listen_for_keyboard_events))
        self.assertTrue(callable(self.console_ui.on_press))
        self.assertTrue(callable(self.console_ui.input))
        self.assertTrue(callable(self.console_ui.is_alphanumeric))
        self.assertTrue(callable(self.console_ui.accept_and_clear_input))
        self.assertTrue(callable(self.console_ui.is_navigation_key))
        self.assertTrue(callable(self.console_ui.hide_cursor))
        self.assertTrue(callable(self.console_ui.show_cursor))
        self.assertTrue(callable(self.console_ui.clear_screen))


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
        is_alphnum_or_space = self.console_ui.is_alphanumeric('a')
        self.assertTrue(is_alphnum_or_space)
        is_alphnum_or_space = self.console_ui.is_alphanumeric('A')
        self.assertTrue(is_alphnum_or_space)
        is_alphnum_or_space = self.console_ui.is_alphanumeric('1')
        self.assertTrue(is_alphnum_or_space)
        is_alphnum_or_space = self.console_ui.is_alphanumeric(' ')
        self.assertTrue(is_alphnum_or_space)
        
    def test_is_not_alphanumeric_returns_false_if_invalid_text_entered(self):
        is_non_alphnum = self.console_ui.is_alphanumeric('.')
        self.assertFalse(is_non_alphnum)
        is_non_alphnum = self.console_ui.is_alphanumeric('Key.enter')
        self.assertFalse(is_non_alphnum)
        is_non_alphnum = self.console_ui.is_alphanumeric('Key.up')
        self.assertFalse(is_non_alphnum)
        is_non_alphnum = self.console_ui.is_alphanumeric('Key.esc')
        self.assertFalse(is_non_alphnum)
        
        
    def test_when_enter_key_pressed_keystrokes_are_stored_in_input_return_value(self):
        Timer(0.5, lambda: self.console_ui.on_press('a')).start()
        input_value = self.console_ui.input(single_character_input = True)
        self.assertEqual(input_value, 'a')

    def test_accept_and_clear_input(self):
        accepted_input = self.console_ui.accept_and_clear_input()
        self.assertEqual(self.console_ui.keystrokes, '')
        self.assertEqual(self.console_ui.accepted_input, accepted_input)

    def test_when_escape_key_pressed_stores_exit_in_input_return_value(self):
        Timer(0.5, lambda: self.console_ui.on_press('Key.esc')).start()
        self.console_ui.input(on_escape = self.on_escape)
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
        navigation_key_pressed = self.console_ui.is_navigation_key('Key.space')
        self.assertFalse(navigation_key_pressed)
        navigation_key_pressed = self.console_ui.is_navigation_key('Key.esc')
        self.assertFalse(navigation_key_pressed)
        navigation_key_pressed = self.console_ui.is_navigation_key('Key.a')
        self.assertFalse(navigation_key_pressed)
        navigation_key_pressed = self.console_ui.is_navigation_key('Key.Z')
        self.assertFalse(navigation_key_pressed)

    def test_handle_cursor_movement_moves_cursor_when_arrow_key_is_pressed(self):
        Timer(0.2, lambda: self.console_ui.on_press('Key.up')).start()
        self.console_ui.input(on_navigation = self.on_navigation)
        self.assertEqual(self.handled_navigation_key, True)

    def test_on_space_is_called_when_space_bar_is_pressed(self):
        Timer(0.2, lambda: self.console_ui.on_press('Key.space')).start()
        self.console_ui.input(on_space = self.on_space)
        self.assertEqual(self.handled_space_key, True)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_text_is_centered_if_specified_width_is_recieved_as_argument(self, mock_out):
        self.get_name()
        output = mock_out.getvalue()
        self.assertIn('                    What is your name?:                     ', output)

    def test_hide_cursor_and_display_keystrokes(self):
        self.get_name()
        self.console_ui.show_cursor()
        def set_response():
            self.console_ui.accepted_input = 'Bob'
        Timer(0.2, set_response).start()
        name = self.console_ui.input(single_character_input = False)
        self.console_ui.hide_cursor()
        self.assertEqual(name, 'Bob')
        
        
        # https://stackoverflow.com/questions/5174810/how-to-turn-off-blinking-cursor-in-command-window#:~:text=Just%20use%20print('%5C033,%2C%20end%3D%22%22)%20.
        # hides cursor print('\033[?25l', end="")
        # shows cursor print('\033[?25h', end="")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_clear_screen_clears_screen_and_stdout(self, mock_out):
        self.get_name()
        self.console_ui.clear_screen(mock_out)
        output = mock_out.getvalue()
        self.assertEqual(output, '')
    


