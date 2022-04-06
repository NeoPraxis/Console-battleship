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
        self.assertEqual(self.grid.y[0], 'A')
        self.assertEqual(self.grid.y[9], 'J')
        self.assertEqual(self.grid.x[0], '1')
        self.assertEqual(self.grid.x[9], '0')
        self.assertIsInstance(self.grid.ships, list)
        self.assertIsInstance(self.grid.shots, list)
        self.assertTrue(callable(self.grid.is_ship_sunk))
        
    def test_add_ship_fails_with_incorrect_number_of_coordinates(self):
        
        coordinates = [
            Coordinates(location={'y':'A', 'x':'1'}),
            Coordinates(location={'y':'A', 'x':'2'}),
            Coordinates(location={'y':'A', 'x':'3'})
        ]

        self.assertRaises(TypeError, self.grid.add_ship, 'Destroyer', coordinates)
        self.assertTrue(len(self.grid.ships) == 0)
    
    def test_if_shot_can_be_added(self):
        coordinates = Coordinates(location={'y':'A', 'x':'1'})
        self.grid.add_shot(coordinates)
        self.assertEqual(len(self.grid.shots), 1)
        self.assertIsInstance(self.grid.shots[0].coordinates, Coordinates)
        
    def test_if_model_is_already_placed_on_grid(self):
        is_model_placed = self.grid.is_model_already_placed('Destroyer')
        self.assertFalse(is_model_placed)
        coordinates = [
            Coordinates(location={'y':'A', 'x':'1'}),
            Coordinates(location={'y':'A', 'x':'2'})
        ]
        self.grid.add_ship('Destroyer', coordinates)
        self.assertEqual(self.grid.ships[0].coordinates[0].model, 'Destroyer')
        is_model_placed = self.grid.is_model_already_placed('Destroyer')
        self.assertTrue(is_model_placed)

    def test_if_ship_coordinates_are_occupied_in_grid(self):
        coordinates = [
            Coordinates(location={'y':'A', 'x':'1'}),
            Coordinates(location={'y':'A', 'x':'2'})
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
            Coordinates(location={'y':'A', 'x':'1'}),
            Coordinates(location={'y':'A', 'x':'2'})
        ]
        self.grid.add_ship('Destroyer', coordinates)
        coordinates = self.grid.get_all_ship_coordinates()
        self.assertEqual(len(coordinates), 2)

        coordinates = [
            Coordinates(location={'y':'A', 'x':'1'}),
            Coordinates(location={'y':'A', 'x':'2'}),
            Coordinates(location={'y':'A', 'x':'3'})
        ]
        self.grid.add_ship('Cruiser', coordinates)

        coordinates = self.grid.get_all_ship_coordinates()
        self.assertEqual(len(coordinates), 2)
    
    def test_can_get_location_coordinates(self):
        ship_coordinates_list = self.grid.get_location_coordinates(
            model = 'Destroyer', location = {'y':'A', 'x':'1'}, orientation = 'h'
            )
        self.assertEqual(len(ship_coordinates_list), 2)
        ship_coordinate_1 = ship_coordinates_list[0]
        self.assertEqual(ship_coordinate_1.y, 'A')
        self.assertEqual(ship_coordinate_1.x, '1')
        ship_coordinate_2 = ship_coordinates_list[1]
        self.assertEqual(ship_coordinate_2.y, 'A')
        self.assertEqual(ship_coordinate_2.x, '2')

    def test_can_get_location_coordinates_at_edge_of_grid(self):

        ship_coordinates_list = self.grid.get_location_coordinates(
            model = 'Destroyer', location = {'y':'J', 'x':'9'}, orientation = 'h'
            )
        self.assertEqual(len(ship_coordinates_list), 2)
        ship_coordinate_1 = ship_coordinates_list[0]
        self.assertEqual(ship_coordinate_1.y, 'J')
        self.assertEqual(ship_coordinate_1.x, '9')
        ship_coordinate_2 = ship_coordinates_list[1]
        self.assertEqual(ship_coordinate_2.y, 'J')
        self.assertEqual(ship_coordinate_2.x, '0')
    
    def test_can_not_get_location_coordinates_outside_edge_of_grid(self):

        ship_coordinates_list = self.grid.get_location_coordinates(
            model = 'Destroyer', location = {'y':'J', 'x':'9'}, orientation = 'v'
            )
        self.assertListEqual(ship_coordinates_list, [])

    def test_can_place_a_ship_given_xy_location_dictionary(self):
        
        location = {'y':'J', 'x':'9'}
        
        ship_coordinates_list = self.grid.get_location_coordinates(
            model = 'Destroyer', location = location, orientation = 'h'
            )
        self.grid.add_ship('Destroyer', ship_coordinates_list)
        self.assertEqual(len(self.grid.ships), 1)

    def test_can_not_add_ship_model_that_is_already_placed(self):
        
        location1 = {'y':'J', 'x':'9'}
        
        location2 = {'y':'A', 'x':'1'}
        
        ship_coordinates_list = self.grid.get_location_coordinates(
            model = 'Destroyer', location = location1, orientation = 'h'
            )
        self.grid.add_ship('Destroyer', ship_coordinates_list)
        self.assertEqual(len(self.grid.ships), 1)

        ship_coordinates_list = self.grid.get_location_coordinates(
            model = 'Destroyer', location = location2, orientation = 'h'
            )
        self.grid.add_ship('Destroyer', ship_coordinates_list)
        self.assertEqual(len(self.grid.ships), 1)

    def test_can_not_overlap_ships(self):
        
        location1 = {'y':'J', 'x':'9'}
        
        location2 = {'y':'J', 'x':'7'}
        
        ship_coordinates_list = self.grid.get_location_coordinates(
            model = 'Destroyer', location = location1, orientation = 'h'
            )
        self.grid.add_ship('Destroyer', ship_coordinates_list)
        self.assertEqual(len(self.grid.ships), 1)

        ship_coordinates_list = self.grid.get_location_coordinates(
            model = 'Cruiser', location = location2, orientation = 'h'
            )
        self.grid.add_ship('Cruiser', ship_coordinates_list)
        self.assertEqual(len(self.grid.ships), 1)

    def test_if_shot_is_taken(self):
        location = {'y':'A', 'x':'1'}
        coordinates = Coordinates(location = location)
        is_shot_taken = self.grid.is_shot_taken(coordinates)
        self.assertFalse(is_shot_taken)
        self.grid.add_shot(coordinates)
        location = {'y':'A', 'x':'1'}
        coordinates = Coordinates(location = location)
        is_shot_taken = self.grid.is_shot_taken(coordinates)
        self.assertTrue(is_shot_taken)
    
    def test_add_shot_if_not_taken(self):
        coordinates = Coordinates(location = {'y':'A', 'x':'1'})
        take_a_shot = self.grid.take_a_shot(coordinates)
        self.assertTrue(take_a_shot)
        self.assertEqual(len(self.grid.shots), 1)
        take_a_shot = self.grid.take_a_shot(coordinates)
        self.assertFalse(take_a_shot)
        
    def test_hit_recorded_when_shot_is_taken(self):
        location1 = {'y':'J', 'x':'9'}
        coordinates = Coordinates(location = location1)
        ship_coordinates_list = self.grid.get_location_coordinates(
            model = 'Destroyer', location = location1, orientation = 'h'
            )
        self.grid.add_ship('Destroyer', ship_coordinates_list)
        self.grid.take_a_shot(coordinates)
        is_hit = self.grid.ships[0].coordinates[0].hit
        self.assertTrue(is_hit)
        self.assertEqual(coordinates.model, 'Destroyer')

    def test_is_ship_sunk_returns_false_if_not_sunk(self):
        
        location = {'y':'A', 'x':'1'}
        ship_coordinates_list = self.grid.get_location_coordinates(
            model = 'Destroyer', location = location, orientation = 'h'
            )
        self.grid.add_ship('Destroyer', ship_coordinates_list)
        ship_sunk = self.grid.is_ship_sunk('Destroyer')
        self.assertEqual(ship_sunk, False)
        ship_coordinates_list[0].hit = True
        ship_coordinates_list[1].hit = True
        ship_sunk = self.grid.is_ship_sunk('Destroyer')
        self.assertTrue(ship_sunk)
       




if __name__ == '__main__':
    unittest.main()
