import unittest
from player import Player
from grid import Grid
from coordinates import Coordinates

class TestPlayer(unittest.TestCase):

    def setUp(self) -> None:
        self.player = Player(name = 'bob', is_ai = False)

    def test_if_test_player_can_instantiate(self):
        self.assertIsInstance(self.player, Player)
        self.assertIsInstance(self.player.name, str)
        self.assertEqual(self.player.name, 'bob')
        self.assertIsInstance(self.player.grid, Grid)
        self.assertIsInstance(self.player.is_ai, bool)
        self.assertFalse(self.player.is_ai)
        self.assertTrue(callable(self.player.receive_a_shot))

    def test_if_player_can_receive_a_shot(self):
        shot_coordinates = Coordinates(location = {'y':'A', 'x':'1'})
        shot_taken = self.player.receive_a_shot(shot_coordinates)
        self.assertTrue(shot_taken)
        self.assertEqual(len(self.player.grid.shots), 1)
        shot_taken = self.player.receive_a_shot(shot_coordinates)
        self.assertFalse(shot_taken)

    

        