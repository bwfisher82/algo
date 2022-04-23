NUMBERS = [3, 5, -4, 8, 11, 1, -1, 6]
TARGET_SUM = 10


def algo(numbers, target_sum):
    # print(algo_linear_time_and_space(numbers, target_sum))
    # print(algo_quadratic(numbers, target_sum))
    print(algo_nlogn_time_constant_space_recursion(numbers, target_sum))
    # print(algo_nlogn_time_constant_space_no_recursion(numbers, target_sum))


def algo_quadratic(numbers, target_sum):
    """Quadratic by nature of the double nested loop, or
    O(n^2).
    """
    if len(numbers) == 1:
        return []
    for number_index, number in enumerate(numbers):
        for addend_index, addend in enumerate(numbers):
            if target_sum - number == addend and number_index != addend_index:
                return [number, addend]
    return []


def algo_linear_time_and_space(numbers, target_sum):
    """Hash table lookup is O(1), allowing to reduce the need for
    a double-nested loop, which is O(n^2). The time complexity is
    linear O(n) due to the one for loop.
    """
    if len(numbers) == 1:
        return []
    hash_table = {}
    for number in numbers:
        addend = target_sum - number
        if addend in hash_table:
            return [number, addend]
        hash_table[number] = True
    return []


def algo_nlogn_time_constant_space_recursion(numbers, target_sum):
    """Here we use left and right pointers for the list so that
    we can traverse it once, but also not need the hash table
    to store anything. So we are still at O(n) time, but we
    are now at O(1) space instead of O(n) space.
    Sort is O(n log(n)), like typical not-bubble sort algorithms, such
    as quick, merge, heap, etc. Python actually uses a 'timsort' method,
    a derivation of merge and insertion sort shown to work well with
    real world data. This is faster than O(n), so overall time complexity
    remains at O(n), or linear.
    The len(list) is constant because a Python list, and probably all
    dynamic arrays (I think?) keep track of its size with a counter and
    thus does not traverse the list to find the size.
    If we could assume a sorted input, this and the no-recursion version
    would be constant time complexity.
    """
    if len(numbers) == 1:
        return []
    numbers.sort()
    return recurse(numbers, target_sum, 0, len(numbers) - 1)


def recurse(numbers, target_sum, head_index, tail_index):
    head = numbers[head_index]
    tail = numbers[tail_index]
    if head + tail > target_sum:
        tail_index -= 1
    elif head + tail < target_sum:
        head_index += 1
    elif head + tail == target_sum:
        return [head, tail]

    if tail_index == head_index:
        return []
    else:
        return recurse(numbers, target_sum, head_index, tail_index)


def algo_nlogn_time_constant_space_no_recursion(numbers, target_sum):
    """Here we are similar to algo_nlogn_time_constant_space_recursion,
    but we do not use recursion.
    """
    if len(numbers) == 1:
        return []
    numbers.sort()
    head_index = 0
    tail_index = len(numbers) - 1

    for i in range(len(numbers) - 1):
        head = numbers[head_index]
        tail = numbers[tail_index]
        if head + tail == target_sum:
            return [head, tail]
        if head + tail > target_sum:
            tail_index -= 1
        elif head + tail < target_sum:
            head_index += 1
        if tail_index == head_index:
            return []


def main():
    algo(NUMBERS, TARGET_SUM)


if __name__ == "__main__":
    main()
