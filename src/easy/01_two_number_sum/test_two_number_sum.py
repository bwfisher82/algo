import pytest

from main import optimal, suboptimal, median, worst_case


class TestTwoNumberSum:
    @pytest.mark.parametrize(
        "numbers, target_sum, possible_results",
        [
            ([], 10, [[]]),
            ([10], 10, [[]]),
            ([1, 2], 3, [[2, 1], [1, 2]]),
            ([1, 2, 3], 5, [[3, 2], [2, 3]]),
            ([1, 2, 3], 4, [[3, 1], [1, 3]]),
            ([1, 2, 3], 3, [[2, 1], [1, 2]]),
            ([1, 2, 3], 5, [[3, 2], [2, 3]]),
            ([-3, -1, 0, 2, 7], 4, [[7, -3], [-3, 7]]),
            ([-3, -1, 0, 2, 7], -1, [[0, -1], [-1, 0], [-3, 2], [2, -3]]),
            ([-3, -1, 0, 2, 7], -3, [[0, -3], [-3, 0]]),
            ([-3, -1, 0, 2, 7], -4, [[-1, -3], [-3, -1]]),
            ([-3, -1, 0, 2, 7], 1, [[2, -1], [-1, 2]]),
            ([-3, -1, 0, 2, 7], 6, [[7, -1], [-1, 7]]),
            ([-3, -1, 0, 2, 7], 2, [[2, 0], [0, 2]]),
            ([-3, -1, 0, 2, 7], 7, [[7, 0], [0, 7]]),
            ([-3, -1, 0, 2, 7], 9, [[7, 2], [2, 7]])
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
