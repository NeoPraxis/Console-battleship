import unittest, io
from unittest import mock
from unittest.mock import patch
from session import Session
from player import Player
from shot import Shot
from turn import Turn
from coordinates import Coordinates
from grid import Grid
from ai import AI
from threading import Timer
from ui import UI



class TestSession(unittest.TestCase):

    def setUp(self) -> None:
        self.session = Session()

    def test_if_session_can_instantiate(self):
        self.assertIsInstance(self.session, Session)
        self.assertIsInstance(self.session.ai, AI)
        self.assertIsInstance(self.session.ui, UI)
        self.assertTrue(callable(self.session.set_player_name))
        self.assertTrue(callable(self.session.add_player))
        self.assertTrue(callable(self.session.set_up_game))
        self.assertTrue(callable(self.session.add_turn))
        self.assertTrue(callable(self.session.number_of_players))
        self.assertTrue(callable(self.session.number_of_turns))
        self.assertTrue(callable(self.session.get_coordinates_from_player))
        self.assertTrue(callable(self.session.place_ship_on_player_grid))
        self.assertTrue(callable(self.session.play_a_round))
        self.assertTrue(callable(self.session.play_a_turn))
        self.assertTrue(callable(self.session.get_shot_from_player))
        self.assertTrue(callable(self.session.get_verified_shot))
        self.assertTrue(callable(self.session.verify_a_shot))
        self.assertTrue(callable(self.session.record_a_shot))
        self.assertTrue(callable(self.session.is_game_over))
        self.assertTrue(callable(self.session.play_a_game))
        self.assertTrue(callable(self.session.start_new_game))
        self.assertTrue(callable(self.session.get_winner))

    def get_player_with_shot(self):
        player = Player('Bob', is_ai = False)
        coordinates = Coordinates(location={'y':'A', 'x':'1'})
        shot = Shot(coordinates)
        return player, shot
    
    def get_player_and_opponent(self):
        player, opponent = Player('Bob', is_ai = False), Player('aI', is_ai = True)
        return player, opponent
    
    def set_up_game(self):
        player, opponent = self.get_player_and_opponent()
        self.session.add_player(player)
        self.session.add_player(opponent)
        
        def get_coordinates_from_player(self, player, model):
            return Grid.get_random_coordinates()

        with mock.patch.object(Session, 'get_coordinates_from_player', get_coordinates_from_player):
            session = Session()
            session.place_ships(player)
            session.place_ships(opponent)
        return player, opponent

    @patch('sys.stdout', new_callable=io.StringIO)  
    def test_if_can_set_player_name(self, mock_out):
        player = Player(' ', is_ai = False)
        opponent = Player(' ', is_ai = True)
        def set_response():
            self.session.ui.console_ui.accepted_input = 'Bob'
        Timer(0.2, set_response).start()
        self.session.set_player_name(player)
        self.assertTrue(len(player.name) >1)
        self.assertIsInstance(player.name, str)
        output = mock_out.getvalue()
        self.assertIn('What is your name?: ', output)
        self.session.set_player_name(opponent)
        self.assertEqual(opponent.name, 'AI', 'opponent name should == AI')
        

    def test_if_can_add_player(self):
        player = Player(name = 'bob', is_ai = False)
        self.session.add_player(player)
        number_of_players = self.session.number_of_players() 
        self.assertEqual(number_of_players, 1)

        player2 = Player(name = 'AI', is_ai = True)
        self.session.add_player(player2)
        number_of_players = self.session.number_of_players() 
        self.assertEqual(number_of_players, 2)

        player2 = Player(name = 'AI', is_ai = True)
        self.session.add_player(player2)
        number_of_players = self.session.number_of_players() 
        self.assertEqual(number_of_players, 2)

    def test_set_up_game(self):
        def fake_set_player_name(self, player):
            player.name = 'fakename'
        def get_coordinates_from_player(self, player, model):
            return Grid.get_random_coordinates()
        with mock.patch.object(Session, 'set_player_name', fake_set_player_name):
            with mock.patch.object(Session, 'get_coordinates_from_player', get_coordinates_from_player):
                session = Session()
                session.set_up_game()
                self.assertEqual(session.number_of_players(), 2)
        
    def test_if_can_add_turn(self):
        coordinates = Coordinates(location={'y':'A', 'x':'1'})
        shot = Shot(coordinates)
        player = Player(name = 'bob', is_ai = False)
        turn = Turn(shot, player)
        self.session.add_turn(turn)
        self.assertEqual(self.session.number_of_turns(), 1)

    def test_if_can_place_ship_on_player_grid(self):
        player = Player(name = 'bob', is_ai = False)
        model = 'Destroyer'
        ship_placed = self.session.place_ship_on_player_grid(player, model)
        self.assertTrue(ship_placed)
        self.assertEqual(len(player.grid.ships), 1)

    def test_place_all_ships(self):
        player = Player(name = 'bob', is_ai = False)
        opponent = Player(name = 'AI', is_ai = True)
        def get_coordinates_from_player(self, player, model):
            return Grid.get_random_coordinates()

        with mock.patch.object(Session, 'get_coordinates_from_player', get_coordinates_from_player):
            session = Session()
            session.place_ships(player)
            self.assertEqual(len(player.grid.ships), 5)
        self.session.place_ships(opponent)
        self.assertEqual(len(opponent.grid.ships), 5)

    def test_get_shot_from_player(self):
        player, opponent = self.get_player_and_opponent()
        player_shot = self.session.get_shot_from_player(player, opponent)
        self.assertIsInstance(player_shot, dict)


    def test_is_shot_verified(self):
        player, shot = self.get_player_with_shot()
        is_shot_verified = self.session.verify_a_shot(shot, player)
        self.assertTrue(is_shot_verified)

    def test_if_can_record_a_shot(self):
        player, shot = self.get_player_with_shot()
        is_shot_recorded = self.session.record_a_shot(shot, player)
        self.assertTrue(is_shot_recorded)

    def test_play_a_turn(self):
        player, opponent = self.get_player_and_opponent()
        play_a_turn = self.session.play_a_turn(player, opponent)
        self.assertFalse(play_a_turn)
        self.assertEqual(self.session.number_of_turns(), 1)

    def test_get_verified_shot(self):
        player, opponent = self.get_player_and_opponent()
        verified_shot = self.session.get_verified_shot(player, opponent)
        self.assertIsInstance(verified_shot, Shot)
        
    def test_play_a_round(self):
        player, opponent = self.get_player_and_opponent()
        self.session.add_player(player)
        self.session.add_player(opponent)
        
        def get_coordinates_from_player(self, player, model):
            return Grid.get_random_coordinates()

        with mock.patch.object(Session, 'get_coordinates_from_player', get_coordinates_from_player):
            session = Session()
            session.place_ships(player)
            session.place_ships(opponent)
        is_game_over = self.session.play_a_round()
        self.assertEqual(is_game_over, False)

    def test_is_game_over(self):
        player, opponent = self.set_up_game()
        game_over = self.session.is_game_over()
        self.assertFalse(game_over)

        def hit(c):
            c.hit = True
        [[hit(c) for c in ship.coordinates] for ship in player.grid.ships]

        game_over = self.session.is_game_over()
        self.assertTrue(game_over)
    
    def test_play_a_game(self):
        player, opponent = self.set_up_game()
        game_played = self.session.play_a_game()
        self.assertEqual(game_played, True)

    def test_start_new_game(self):
        def fake_set_player_name(self, player):
            player.name = 'fakename'
        def get_coordinates_from_player(self, player, model):
            return Grid.get_random_coordinates()
        with mock.patch.object(Session, 'set_player_name', fake_set_player_name):
            with mock.patch.object(Session, 'get_coordinates_from_player', get_coordinates_from_player):
                session = Session()
                winner = session.start_new_game()
                game_over = session.is_game_over()
                self.assertTrue(game_over)
                self.assertIsInstance(winner, Player)

    def test_get_winner(self):
        def fake_set_player_name(self, player):
            player.name = 'fakename'
        def get_coordinates_from_player(self, player, model):
            return Grid.get_random_coordinates()
        with mock.patch.object(Session, 'set_player_name', fake_set_player_name):
            with mock.patch.object(Session, 'get_coordinates_from_player', get_coordinates_from_player):
                session = Session()
                session.start_new_game()
                game_over = session.is_game_over()
                self.assertTrue(game_over)
                winner = session.get_winner()
                self.assertIsInstance(winner, Player)
                self.assertFalse(winner.is_defeated())
        
        

