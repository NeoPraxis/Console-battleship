import unittest, io
from unittest.mock import patch
from threading import Timer
from console_ui import ConsoleUI
from ui import UI

class TestUI(unittest.TestCase):
    
    def setUp(self) -> None:
        self.ui = UI()

    def test_if_ui_can_instantiate(self):
        self.assertIsInstance(self.ui, UI)
        self.assertIsInstance(self.ui.console_ui, ConsoleUI)
        self.assertTrue(callable(self.ui.get_name))
        self.assertTrue(callable(self.ui.display_place_ship_instructions))
        self.assertTrue(callable(self.ui.place_ship))
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_name(self, mock_out):
        def set_response():
            self.ui.console_ui.accepted_input = 'Bob'
        Timer(0.2, set_response).start()
        name = self.ui.get_name()
        output = mock_out.getvalue()
        self.assertEqual(name, 'Bob')
        self.assertIn('What is your name?: ', output)

    @patch('sys.stdout', new_callable=io.StringIO)  
    def test_display_place_ship_instructions_prints_to_console(self, mock_out):
        self.ui.place_ship('Destroyer')
        output = mock_out.getvalue()
        self.assertIn('1: Place your Destroyer.', output)
        self.assertIn('2: Move arrow keys to navigate position.', output)
        self.assertIn('3: Press spacebar to change orientation.', output)
        self.assertIn('4: Press enter to place your Destroyer.', output)


    def test_up_down_left_right_arrow_keys_moves_cursor_and_stores_coordinates(self):
        pass

    def test_prompt_for_coordinates_returns_current_cursor_position(self):
        pass

    def test_get_grid_content_returns_correct_character_for_given_coordinate(self):
        pass

    def test_display_grid_renders_grid_with_grid_content(self):
        pass

    def test_console_clears_screen_to_refresh_ui_display_properly(self):
        pass
        
    def test_when_spacebar_pressed_orientation_of_ship_toggles(self):
        pass