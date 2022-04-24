import pytest

from random import randint

from main import optimal, suboptimal


class TestSortedSquaredArray:
    @classmethod
    def _generate_input(cls, input_type=None):
        if input_type is None:
            input_type = randint(1, 10)
        if input_type == 1:
            return [randint(-20, 20) for i in range(20)]
        elif input_type == 2:
            return []
        elif input_type == 3:
            return [randint(0, 20) for i in range(10)]
        elif input_type == 4:
            return [randint(-20, 20) for i in range(500)]
        elif input_type == 5:
            return [randint(-100, 100) for i in range(100)]
        elif input_type == 6:
            return [randint(-2, 2) for i in range(2)]
        elif input_type == 7:
            return [randint(-1000, 1000) for i in range(20)]
        elif input_type == 8:
            return [randint(-50, 50) for i in range(1_000)]
        elif input_type == 9:
            return ""
        elif input_type == 10:
            return [randint(-1000, 1000) for i in range(1_000)]

    @classmethod
    def _is_result_sorted(cls):
        array = TestSortedSquaredArray._generate_input(1)
        result_optimal = optimal(sorted(array))
        result_suboptimal = suboptimal(sorted(array))
        return result_optimal == sorted(result_optimal) and \
            result_suboptimal == sorted(result_suboptimal)

    def test_result_is_sorted(self):
        for i in range(1, 101):
            assert TestSortedSquaredArray._is_result_sorted()

    @pytest.mark.parametrize("array, expected_result", [
        ([1, 2, 3, 5, 6, 8, 9], [1, 4, 9, 25, 36, 64, 81]),
        ([-12, -4, -1, 0, 1, 5, 10, 13], [0, 1, 1, 16, 25, 100, 144, 169]),
        ([], [])
    ])
    def test_given_arrays_return_valid_results(self, array, expected_result):
        assert optimal(array) == expected_result
