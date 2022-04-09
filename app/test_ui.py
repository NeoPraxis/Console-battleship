import unittest
from unittest.mock import patch
from ui import UI

class TestUI(unittest.TestCase):
    
    def setUp(self) -> None:
        self.ui = UI()

    def test_if_ui_can_instantiate(self):
        self.assertIsInstance(self.ui, UI)
        self.assertTrue(callable(self.ui.get_name))

    # TODO use pyinput to mock keystrokes for UI placements
    
    # def test_get_name(self):
    #     with patch('__builtin__.input', return_value='fakename') as :
    #         name = self.ui.get_name()
    #         self.assertIsInstance(name, str)
        