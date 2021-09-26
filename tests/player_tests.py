import unittest
from models.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("player1", "rock")

    def test_player_exists(self):
        self.assertEqual("player1", self.player1.name)
