import unittest
from grid import Grid

class TestGrid(unittest.TestCase):
    
    def test_if_grid_can_instantiate_with_correct_properties(self):
        self.grid = Grid()
        self.assertIsInstance(self.grid, Grid)
        self.assertIsInstance(self.grid.x, list)
        self.assertIsInstance(self.grid.y, list)
        self.assertEqual(self.grid.x[0], 'A')
        self.assertEqual(self.grid.x[9], 'J')
        self.assertEqual(self.grid.y[0], '1')
        self.assertEqual(self.grid.y[9], '0')
        self.assertIsInstance(self.grid.ships, list)
        self.assertIsInstance(self.grid.shots, list)

