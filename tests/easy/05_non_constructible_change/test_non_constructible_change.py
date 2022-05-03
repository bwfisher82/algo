import pytest

from main import non_constructible_change


class TestNonBuildingChange:
    @pytest.mark.parametrize("coins, expected_result", [
        ([5, 7, 1, 1, 2, 3, 22], 20),
        ([1, 1, 1, 1, 1], 6),
        ([1, 5, 1, 1, 1, 10, 15, 20, 100], 55),
        ([6, 4, 5, 1, 1, 8, 9], 3),
        ([], 1),
        ([87], 1),
        ([5, 6, 1, 1, 2, 3, 4, 9], 32),
        ([5, 6, 1, 1, 2, 3, 43], 19),
        ([1, 1], 3),
        ([2], 1),
        ([1], 2),
        ([109, 2000, 8765, 19, 18, 17, 16, 8, 1, 1, 2, 4], 87),
        ([1, 2, 3, 4, 5, 6, 7], 29)
    ])
    def test_larger_coin_sizes(self, coins: list, expected_result: int):
        assert non_constructible_change(coins) == expected_result
