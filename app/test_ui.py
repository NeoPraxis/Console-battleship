import unittest
from unittest.mock import patch
from ui import UI

class TestUI(unittest.TestCase):
    
    def setUp(self) -> None:
        self.ui = UI()

    def test_if_ui_can_instantiate(self):
        self.assertIsInstance(self.ui, UI)
        self.assertTrue(callable(self.ui.get_name))
    
    def test_get_name(self):
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
        
    def test_when_spacebar_pressed_orientation_of_ship_toggles(self):
        pass