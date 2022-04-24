import pytest

from main import optimal, suboptimal


class TestTournamentWinner:
    @pytest.mark.parametrize("competitions, results, winner", [
        ([
             ["HTML", "C#"],
             ["C#", "Python"],
             ["Python", "HTML"]
         ], [0, 0, 1], "Python")
    ])
    def test_given_game_data_returns_valid_results(self, competitions, results, winner):
        assert suboptimal(competitions, results) == winner
        assert optimal(competitions, results) == winner
