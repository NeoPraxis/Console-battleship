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
        self.assertTrue(callable(self.player.is_defeated))

    def test_if_player_can_receive_a_shot(self):
        shot_coordinates = Coordinates(location = {'y':'A', 'x':'1'})
        shot_taken = self.player.receive_a_shot(shot_coordinates)
        self.assertTrue(shot_taken)
        self.assertEqual(len(self.player.grid.shots), 1)
        shot_taken = self.player.receive_a_shot(shot_coordinates)
        self.assertFalse(shot_taken)

    def test_is_defeated(self):
        # 1
        location = {'y':'A', 'x':'1'}
        ship_coordinates_list1 = self.player.grid.get_location_coordinates(
            model = 'Destroyer', location = location, orientation = 'h'
            )
        self.player.grid.add_ship('Destroyer', ship_coordinates_list1)
        # 2
        location = {'y':'B', 'x':'1'}
        ship_coordinates_list2 = self.player.grid.get_location_coordinates(
            model = 'Submarine', location = location, orientation = 'h'
            )
        self.player.grid.add_ship('Submarine', ship_coordinates_list2)
        # 3
        location = {'y':'C', 'x':'1'}
        ship_coordinates_list3 = self.player.grid.get_location_coordinates(
            model = 'Cruiser', location = location, orientation = 'h'
            )
        self.player.grid.add_ship('Cruiser', ship_coordinates_list3)
        # 4
        location = {'y':'D', 'x':'1'}
        ship_coordinates_list4 = self.player.grid.get_location_coordinates(
            model = 'Battleship', location = location, orientation = 'h'
            )
        self.player.grid.add_ship('Battleship', ship_coordinates_list4)
        # 5
        location = {'y':'E', 'x':'1'}
        ship_coordinates_list5 = self.player.grid.get_location_coordinates(
            model = 'Carrier', location = location, orientation = 'h'
            )
        self.player.grid.add_ship('Carrier', ship_coordinates_list5)


        is_defeated = self.player.is_defeated()
        self.assertFalse(is_defeated)
        ship_coordinates_list1[0].hit = True
        ship_coordinates_list1[1].hit = True

        ship_coordinates_list2[0].hit = True
        ship_coordinates_list2[1].hit = True
        ship_coordinates_list2[2].hit = True

        ship_coordinates_list3[0].hit = True
        ship_coordinates_list3[1].hit = True
        ship_coordinates_list3[2].hit = True
        
        ship_coordinates_list4[0].hit = True
        ship_coordinates_list4[1].hit = True
        ship_coordinates_list4[2].hit = True
        ship_coordinates_list4[3].hit = True

        ship_coordinates_list5[0].hit = True
        ship_coordinates_list5[1].hit = True
        ship_coordinates_list5[2].hit = True
        ship_coordinates_list5[3].hit = True
        ship_coordinates_list5[4].hit = True
        is_defeated = self.player.is_defeated()
        self.assertTrue(is_defeated)
        
        

    

        