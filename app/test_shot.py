import unittest
from shot import Shot
from coordinates import Coordinates

class TestShot(unittest.TestCase):

    def test_if_shot_can_instantiate_with_correct_properties(self):
        coordinates = Coordinates(location={'y':'A', 'x':'1'})
        shot = Shot(coordinates)
        self.assertIsInstance(shot, Shot)
        self.assertIsInstance(shot.coordinates, Coordinates)
    

if __name__ == '__main__':
    unittest.main()
