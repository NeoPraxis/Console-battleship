from curses import KEY_A1
from subprocess import call
import unittest, io
from unittest.mock import patch
from console_ui import ConsoleUI
from pynput.keyboard import Key#, Controller
from threading import Timer


class TestConsoleUI(unittest.TestCase):
    
    def setUp(self) -> None:
        self.console_ui = ConsoleUI()
        #self.keyboard = Controller()
        self.time = 0

    def press(self, key):
        self.time += 0.05
        Timer(self.time, self.keyboard.press, ([key])).start()
        self.time += 0.05
        Timer(self.time, self.keyboard.release, ([key])).start()

    def test_if_console_ui_can_instantiate(self):
        
        self.assertIsInstance(self.console_ui, ConsoleUI)
        self.assertTrue(callable(self.console_ui.print_xy))
        #self.assertTrue(callable(self.console_ui.listen_for_keyboard_events))
        self.assertTrue(callable(self.console_ui.on_press))
        self.assertIsInstance(self.console_ui.keystrokes, str)
        self.assertIsInstance(self.console_ui.single_character_input, bool)
        self.assertTrue(callable(self.console_ui.input))
        self.assertIsInstance(self.console_ui.input_return_value, str)
        self.assertTrue(callable(self.console_ui.is_alphanumeric_or_space))


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
            self.console_ui.input_return_value = 'W'
        Timer(0.005, set_response).start()
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
        Timer(0.005, lambda: self.console_ui.on_press('a')).start()
        input_value = self.console_ui.input()
        self.assertEqual(input_value, 'a')

    def test_when_spacebar_pressed_orientation_of_ship_toggles(self):
        pass

    def test_when_escape_key_pressed_stores_exit_in_input_return_value(self):
        pass

    def test_is_navigation_key_returns_true_if_arrows_are_pressed(self):
        pass

    def test_handle_cursor_movement_moves_cursor_when_arrow_key_is_pressed(self):
        pass

    def test_up_down_left_right_arrow_keys_moves_cursor_and_stores_coordinates(self):
        pass

    def test_display_input_buffer_shows_text_while_typing(self):
        pass

    def test_prompt_for_coordinates_returns_current_cursor_position(self):
        pass

    def test_get_grid_content_returns_correct_character_for_given_coordinate(self):
        pass

    def test_display_grid_renders_grid_with_grid_content(self):
        pass

    def test_console_clears_screen_to_refresh_ui_display_properly(self):
        pass