import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
        
    def test_search_no_player(self):
        player = self.stats.search("Kurrp")
        self.assertEqual(player, None)
    
    def test_search_player(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")
        
    def test_players_of_team(self):
        players = self.stats.team("EDM")
        self.assertEqual(len(players), 3)
    
    def test_top(self):
        top = self.stats.top(2)
        self.assertEqual(len(top), 3)
        self.assertEqual(top[0].name, "Gretzky")
        self.assertEqual(top[1].name, "Lemieux")
