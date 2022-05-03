import pytest

algo = __import__("algo.easy.01_two_number_sum")
import algo.main


class TestTwoNumberSum:
    @pytest.mark.parametrize(
        "numbers, target_sum, possible_results",
        [
            ([3, 5, -4, 8, 11, 1, -1, 6], 10, [[-1, 11], [11, -1]]),
            ([4, 6], 10, [[6, 4], [4, 6]]),
            ([4, 6, 1], 5, [[1, 4], [4, 1]]),
            ([4, 6, 1, -3], 3, [[-3, 6], [6, -3]]),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9], 17, [[9, 8], [8, 9]]),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18, [[15, 3], [3, 15]]),
            ([-7, -5, -3, -1, 0, 1, 3, 5, 7], -5, [[0, -5], [-5, 0]]),
            ([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 163, [[-47, 210], [210, -47]]),
            ([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 164, [[]]),
            ([3, 5, -4, 8, 11, 1, -1, 6], 15, [[]]),
            ([14], 15, [[]]),
            ([15], 15, [[]])
        ]
    )
    def test_expected_results_test_cases(self,
        numbers, target_sum, possible_results
    ):
        assert optimal(numbers, target_sum) in possible_results
        assert median(numbers, target_sum) in possible_results
        assert suboptimal(numbers, target_sum) in possible_results
        assert worst_case(numbers, target_sum) in possible_results

    @pytest.mark.parametrize(
        "numbers, target_sum",
        [
            ([1, 2, 3], None),
            (None, 10),
            (None, None)
        ]
    )
    def test_passing_none_raises_exception(self, numbers, target_sum):
        with pytest.raises(TypeError):
            optimal(numbers, target_sum)
            median(numbers, target_sum)
            suboptimal(numbers, target_sum)
            worst_case(numbers, target_sum)
