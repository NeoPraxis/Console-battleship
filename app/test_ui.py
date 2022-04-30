
import unittest, io
from unittest.mock import patch
from threading import Timer
from console_ui import ConsoleUI
from ui import UI
from player import Player
from coordinates import Coordinates

class TestUI(unittest.TestCase):
    
    def setUp(self) -> None:
        self.ui = UI()

    def test_if_ui_can_instantiate(self):
        self.assertIsInstance(self.ui, UI)
        self.assertIsInstance(self.ui.console_ui, ConsoleUI)
        self.assertIsInstance(self.ui.cursor, dict)
        self.assertIsInstance(self.ui.orientation, str)
        self.assertIsInstance(self.ui.is_placing_ship, bool)
        self.assertIsInstance(self.ui.place_ship_model, str)
        self.assertIsInstance(self.ui.keystrokes, str)
        self.assertTrue(callable(self.ui.get_name))
        self.assertTrue(callable(self.ui.display_place_ship_instructions))
        self.assertTrue(callable(self.ui.place_ship))
        self.assertTrue(callable(self.ui.print_grid))
        self.assertTrue(callable(self.ui.get_grid_content))
        self.assertTrue(callable(self.ui.on_navigation))
        self.assertTrue(callable(self.ui.on_space))
        self.assertTrue(callable(self.ui.on_enter))
        self.assertTrue(callable(self.ui.get_shot))
    
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
        player = Player('Bob', is_ai = False)
        Timer(0.5, lambda: self.ui.console_ui.on_press('Key.enter')).start()
        self.ui.place_ship('Destroyer', player)
        output = mock_out.getvalue()
        self.assertIn('1: Place your Destroyer', output)
        self.assertIn('2: Move arrow keys to navigate position', output)
        self.assertIn('3: Press spacebar to change orientation', output)
        self.assertIn('4: Press enter to place your Destroyer', output)

    @patch('sys.stdout', new_callable=io.StringIO)  
    def test_if_ui_can_print_grid(self, mock_out):
        player = Player('Bob', is_ai = False)

        location = {'y':'A', 'x':'1'}
        ship_coordinates_list1 = player.grid.get_location_coordinates(
            model = 'Destroyer', location = location, orientation = 'h'
            )
        player.grid.add_ship('Destroyer', ship_coordinates_list1)

        self.ui.print_grid(player)
        output = mock_out.getvalue()
        self.assertIn('    1   2   3   4   5   6   7   8   9   0 ', output)
        self.assertIn('A |[O]| O |   |   |   |   |   |   |   |   |', output)

    def test_ui_can_return_content_for_single_coordinate_on_grid(self):
        player: Player = Player('Bob', is_ai = False)
        location = {'y':'A', 'x':'1'}
        ship_coordinates_list1 = player.grid.get_location_coordinates(
            model = 'Destroyer', location = location, orientation = 'h'
            )
        player.grid.add_ship('Destroyer', ship_coordinates_list1)
        coordinates = Coordinates(location={'y':'A', 'x':'2'})
        player.receive_a_shot(coordinates)
        coordinates2 = Coordinates(location={'y':'A', 'x':'3'})
        player.receive_a_shot(coordinates2)
        all_ship_coordinates = player.grid.get_all_ship_coordinates()

        grid_content = self.ui.get_grid_content(player, 'A', '1', all_ship_coordinates)
        self.assertEqual(grid_content, '[O]')

        grid_content = self.ui.get_grid_content(player, 'A', '3', all_ship_coordinates)
        self.assertEqual(grid_content, ' * ')

        grid_content = self.ui.get_grid_content(player, 'A', '4', all_ship_coordinates)
        self.assertEqual(grid_content, '   ')
        
        grid_content = self.ui.get_grid_content(player, 'A', '2', all_ship_coordinates)
        self.assertEqual(grid_content, ' X ')

    def test_up_down_left_right_arrow_keys_moves_cursor_and_stores_coordinates(self):
        self.ui.on_navigation('Key.right')
        self.assertEqual(self.ui.cursor, {'y':'A', 'x':'2'})
        self.ui.on_navigation('Key.left')
        self.assertEqual(self.ui.cursor, {'y':'A', 'x':'1'})
        self.ui.on_navigation('Key.down')
        self.assertEqual(self.ui.cursor, {'y':'B', 'x':'1'})
        self.ui.on_navigation('Key.up')
        self.assertEqual(self.ui.cursor, {'y':'A', 'x':'1'})
        self.ui.on_navigation('Key.up')
        self.assertEqual(self.ui.cursor, {'y':'A', 'x':'1'})
        
    def test_spacebar_changes_orientation(self):
        self.ui.on_space('Key.space')
        self.assertEqual(self.ui.orientation, 'v')

    def test_ui_can_display_targeting_grid(self):
        pass

        