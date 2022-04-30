import random
import pytest

from enum import Enum

from main import non_constructible_change


class TestNonBuildingChange:
    @classmethod
    def _get_sample_coins(cls) -> list:
        return [5, 7, 1, 1, 2, 3, 22]

    @classmethod
    def _get_coins_small_size(cls) -> list:
        return [29, 33, 19, 37, 5, 43, 27, 29, 35, 47, 3, 28, 11, 36, 45, 3, 8, 14, 33, 11,
                28, 4, 21, 29, 24, 33, 21, 32, 35, 5, 2, 9, 4, 14, 2, 42, 11, 39, 21, 41, 49,
                48, 2, 33, 14, 20, 1, 4, 23, 5]

    @classmethod
    def _get_coins_medium_size(cls) -> list:
        return cls._get_coins_small_size() * 200

    @classmethod
    def _get_coins_large_size(cls) -> list:
        return cls._get_coins_medium_size() * 25

    def test_no_change_returns_one(self):
        assert non_constructible_change([]) == 1

    def test_change_of_1_returns_2(self):
        assert non_constructible_change([1]) == 2

    def test_change_of_1_2_returns_4(self):
        assert non_constructible_change([1, 2]) == 4

    def test_change_of_1_2_3_returns_7(self):
        assert non_constructible_change([1, 2, 3]) == 7

    def test_change_of_3_2_1_returns_7(self):
        assert non_constructible_change([3, 2, 1]) == 7

    def test_change_using_sample_coins(self):
        assert non_constructible_change(self.__class__._get_sample_coins()) == 20

    @pytest.mark.parametrize("size, expected_result", [
        ("small", 1113),
        ("medium", 222401),
        ("large", 5560001)
    ])
    def test_larger_coin_sizes(self, size: str, expected_result: int):
        coins = []
        if size == "small":
            coins = self.__class__._get_coins_small_size()
        elif size == "medium":
            coins = self.__class__._get_coins_medium_size()
        elif size == "large":
            coins = self.__class__._get_coins_large_size()
        assert non_constructible_change(coins) == expected_result
