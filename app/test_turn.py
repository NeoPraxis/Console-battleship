import unittest
from turn import Turn
from shot import Shot
from coordinates import Coordinates
from player import Player

class TestTurn(unittest.TestCase):
    
    def test_if_turn_can_instantiate(self):
        turn = Turn(
            shot = Shot(Coordinates(location = {'y':'A', 'x':'1'})),
            player = Player(name = 'bob', is_ai = False)
        )
        self.assertIsInstance(turn, Turn)
        self.assertIsInstance(turn.shot, Shot)
        self.assertEqual(turn.shot.coordinates.x, '1')
        self.assertEqual(turn.shot.coordinates.y, 'A')
        self.assertIsInstance(turn.player, Player)
        self.assertEqual(turn.player.name, 'bob')
    
    def test_turn_raises_error_on_bad_arguments(self):

        self.assertRaises(TypeError, Turn, 
            Player(name = 'bob', is_ai = False),
            Shot(Coordinates(location = {'y':'A', 'x':'1'}))
        )

        self.assertRaises(TypeError, Turn,
            Shot(Coordinates(location = {'y':'A', 'x':'1'}))
        )

        self.assertRaises(TypeError, Turn,
            Shot(Coordinates(location = {'y':'A', 'x':'1'})),
            'bob'
        )

        