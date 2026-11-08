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

    def test_search(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")


    def test_search_team(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.team, "EDM")


    def test_search_unknown(self):
        player = self.stats.search("Kinnunen")
        self.assertIsNone(player)


    def test_team_equal(self):
        edm_team = self.stats.team("EDM")
        for player in edm_team:
            self.assertEqual(player.team, "EDM")


    def test_team_isnot(self):
        edm_team = self.stats.team("EDM")
        for player in edm_team:
            self.assertIsNot(player.team, "PIT")


    def test_top_returns_in_points_order(self):
        top_scorers = self.stats.top(2)

        self.assertEqual(top_scorers[0].name, "Gretzky")
        self.assertEqual(top_scorers[1].name, "Lemieux")
        self.assertEqual(top_scorers[2].name, "Yzerman")

    def test_top_returns_correct_number_of_players(self):
        top_scorers = self.stats.top(2)

        self.assertEqual(len(top_scorers), 3)


    def test_top_with_zero(self):
        top_scorers = self.stats.top(0)

        self.assertEqual(len(top_scorers), 1)
        self.assertEqual(top_scorers[0].name, "Gretzky")

