import unittest
from coordinates import Coordinates
from grid import Grid
from shot import Shot

class TestGrid(unittest.TestCase):
    
    def setUp(self):
        self.grid = Grid()

    def test_if_grid_can_instantiate_with_correct_properties(self):
        self.assertIsInstance(self.grid, Grid)
        self.assertIsInstance(self.grid.x, list)
        self.assertIsInstance(self.grid.y, list)
        self.assertEqual(self.grid.x[0], 'A')
        self.assertEqual(self.grid.x[9], 'J')
        self.assertEqual(self.grid.y[0], '1')
        self.assertEqual(self.grid.y[9], '0')
        self.assertIsInstance(self.grid.ships, list)
        self.assertIsInstance(self.grid.shots, list)
        
    def test_add_ship_fails_with_incorrect_number_of_coordinates(self):
        
        coordinates = [
            Coordinates(location={'x':'A', 'y':'1'}),
            Coordinates(location={'x':'A', 'y':'2'}),
            Coordinates(location={'x':'A', 'y':'3'})
        ]

        self.assertRaises(TypeError, self.grid.add_ship, 'Destroyer', coordinates)
        self.assertTrue(len(self.grid.ships) == 0)
    
    def test_if_shot_can_be_added(self):
        coordinates = Coordinates(location={'x':'A', 'y':'1'})
        self.grid.add_shot(coordinates)
        self.assertEqual(len(self.grid.shots), 1)
        self.assertIsInstance(self.grid.shots[0].coordinates, Coordinates)
        
    def test_if_model_is_already_placed_on_grid(self):
        is_model_placed = self.grid.is_model_already_placed('Destroyer')
        self.assertFalse(is_model_placed)
        coordinates = [
            Coordinates(location={'x':'A', 'y':'1'}),
            Coordinates(location={'x':'A', 'y':'2'})
        ]
        self.grid.add_ship('Destroyer', coordinates)
        is_model_placed = self.grid.is_model_already_placed('Destroyer')
        self.assertTrue(is_model_placed)

    def test_if_ship_coordinates_are_occupied_in_grid(self):
        coordinates = [
            Coordinates(location={'x':'A', 'y':'1'}),
            Coordinates(location={'x':'A', 'y':'2'})
        ]
        is_blocked = self.grid.is_ship_blocked(coordinates)
        self.assertFalse(is_blocked)
        self.grid.add_ship('Destroyer', coordinates)
        is_blocked = self.grid.is_ship_blocked(coordinates)
        self.assertTrue(is_blocked)

    def test_if_grid_can_return_coordinates_for_all_placed_ships(self):
        coordinates = self.grid.get_all_ship_coordinates()
        self.assertEqual(len(coordinates), 0)
        coordinates = [
            Coordinates(location={'x':'A', 'y':'1'}),
            Coordinates(location={'x':'A', 'y':'2'})
        ]
        self.grid.add_ship('Destroyer', coordinates)
        coordinates = self.grid.get_all_ship_coordinates()
        self.assertEqual(len(coordinates), 2)

        coordinates = [
            Coordinates(location={'x':'A', 'y':'1'}),
            Coordinates(location={'x':'A', 'y':'2'}),
            Coordinates(location={'x':'A', 'y':'3'})
        ]
        self.grid.add_ship('Cruiser', coordinates)

        coordinates = self.grid.get_all_ship_coordinates()
        self.assertEqual(len(coordinates), 5)
    