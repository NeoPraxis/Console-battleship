import unittest
from coordinates import Coordinates


class TestCoordinates(unittest.TestCase):

    def test_if_can_instantiate_coordinates_with_correct_properties(self):
        coordinates = Coordinates(location={'x':'A', 'y':'1'})
        self.assertIsInstance(coordinates, Coordinates)
        self.assertIsInstance(coordinates.x, str)
        self.assertIsInstance(coordinates.y, str)
        self.assertEqual(coordinates.x, 'A')
        self.assertEqual(coordinates.y, '1')
    

if __name__ == '__main__':
    unittest.main()

