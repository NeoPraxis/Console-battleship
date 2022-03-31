from distutils.log import error
import unittest
from ship import Ship
from coordinates import Coordinates

class TestShip(unittest.TestCase):

    def test_if_ship_can_instantiate_with_properties(self):
        coordinates = [
            Coordinates(location={'x':'A', 'y':'1'}),
            Coordinates(location={'x':'A', 'y':'2'})
        ]
        ship = Ship(model='Destroyer', coordinates=coordinates)
        self.assertIsInstance(ship, Ship)
        self.assertIsInstance(ship.size, int)
        self.assertEqual(ship.size, 2)
        self.assertIsInstance(ship.model, str)
        self.assertEqual(ship.model, 'Destroyer')
        self.assertIsInstance(ship.coordinates, list)
        self.assertTrue(ship.coordinates[0].x == 'A')
        self.assertTrue(ship.coordinates[0].y == '1')
        self.assertIsInstance(ship.models, dict)
        self.assertEqual(ship.models.get('Destroyer'), 2)
        self.assertEqual(ship.models.get('Cruiser'), 3)
        self.assertEqual(ship.models.get('Submarine'), 3)
        self.assertEqual(ship.models.get('Battleship'), 4)
        self.assertEqual(ship.models.get('Carrier'), 5)
        
    def test_if_ship_matches_correct_number_of_coordinates(self):

        coordinates = [
            Coordinates(location={'x':'A', 'y':'1'}),
            Coordinates(location={'x':'A', 'y':'2'}),
        ]

        self.assertRaises(TypeError, Ship, 'Cruiser', coordinates)

        
            