import unittest
from coordinates import Coordinates


class TestCoordinates(unittest.TestCase):

    def test_if_can_instantiate_coordinates_with_correct_properties(self):
        coordinates = Coordinates(location={'y':'A', 'x':'1'})
        self.assertIsInstance(coordinates, Coordinates)
        self.assertIsInstance(coordinates.x, str)
        self.assertIsInstance(coordinates.y, str)
        self.assertIsInstance(coordinates.hit, bool)
        self.assertIsInstance(coordinates.model, str)
        self.assertEqual(coordinates.y, 'A')
        self.assertEqual(coordinates.x, '1')
    

if __name__ == '__main__':
    unittest.main()

