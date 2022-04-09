import unittest
from ai import AI


class TestAI(unittest.TestCase):
    
    def setUp(self) -> None:
        self.ai = AI()

    def test_if_ai_can_instantiate(self):
        
        self.assertIsInstance(self.ai, AI)
        self.assertTrue(callable(self.ai.get_name))
        self.assertTrue(callable(self.ai.place_ship))
        self.assertTrue(callable(self.ai.get_shot))

    def test_get_name(self):
        name = self.ai.get_name()
        self.assertIsInstance(name, str)
        self.assertEqual(name, 'AI')
        
    def test_place_ship(self):
        location, orientation = self.ai.place_ship()
        self.assertIsInstance(location, dict)
        self.assertIsInstance(orientation, str)

    def test_get_shot(self):
        shot = self.ai.get_shot()
        self.assertIsInstance(shot, dict)