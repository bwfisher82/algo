import pytest


from main import is_valid_subsequence


class TestValidateSubsequence:
    @pytest.mark.parametrize("array, sequence, isFound", [
        ([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10], True),
        ([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 1], False),
        ([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 44], False),
        ([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10, 15, 38, 29, 38, 5, 8, 1], False),
        ([5, 1, 22, 25, 6, -1, 8, 10], [], False),
        ([], [1, 6, -1, 10], False),
        ([], [], False),
        ([5, 1, 22, 25, 6, -1, 8, 10], [1], True),
        ([1], [1], True),
        ([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10], True)
    ])
    def test_subsequence(self, array, sequence, isFound):
        assert is_valid_subsequence(array, sequence) == isFound
