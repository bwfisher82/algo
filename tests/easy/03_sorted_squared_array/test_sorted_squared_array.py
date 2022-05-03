import pytest

from main import optimal, suboptimal


class TestSortedSquaredArray:

    @classmethod
    def _is_result_sorted(cls):
        array = [-7, -3, 1, 9, 22, 30]
        result_optimal = optimal(sorted(array))
        result_suboptimal = suboptimal(sorted(array))
        return result_optimal == sorted(result_optimal) and \
            result_suboptimal == sorted(result_suboptimal)

    def test_result_is_sorted(self):
        for i in range(1, 101):
            assert TestSortedSquaredArray._is_result_sorted()

    @pytest.mark.parametrize("array, expected_result", [
        ([1, 2, 3, 5, 6, 8, 9], [1, 4, 9, 25, 36, 64, 81]),
        ([1], [1]),
        ([1, 2], [1, 4]),
        ([1, 2, 3, 4, 5], [1, 4, 9, 16, 25]),
        ([0], [0]),
        ([10], [100]),
        ([-1], [1]),
        ([-2, -1], [1, 4]),
        ([-5, -4, -3, -2, -1], [1, 4, 9, 16, 25]),
        ([-10], [100]),
        ([-10, -5, 0, 5, 10], [0, 25, 25, 100, 100]),
        ([-7, -3, 1, 9, 22, 30], [1, 9, 49, 81, 484, 900]),
        ([-50, -13, -2, -1, 0, 0, 1, 1, 2, 3, 19, 20],
            [0, 0, 1, 1, 1, 4, 4, 9, 169, 361, 400, 2500]),
        ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
        ([-1, -1, 2, 3, 3, 3, 4], [1, 1, 4, 9, 9, 9, 16]),
        ([-3, -2, -1], [1, 4, 9]),
        ([-3, -2, -1], [1, 4, 9]),
        ([], [])
    ])
    def test_given_arrays_return_valid_results(self, array, expected_result):
        assert optimal(array) == expected_result
