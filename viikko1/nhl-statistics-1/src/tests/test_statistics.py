import unittest
from statistics import Statistics
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

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_player_in(self):
        player = self.statistics.search("Semenko")
        self.assertEqual(player.name, "Semenko")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.goals, 4)
        self.assertEqual(player.assists, 12)
    
    def test_search_player_not_in(self):
        player = self.statistics.search("Selänne")
        self.assertIsNone(player)

    def test_team_in(self):
        teamlist = self.statistics.team("EDM")
        self.assertEqual(len(teamlist), 3)

    def test_top_scorers(self):
        scorer_list = self.statistics.top_scorers(2)
        self.assertEqual(scorer_list[0].name, "Gretzky")
        self.assertEqual(scorer_list[1].name, "Lemieux")
