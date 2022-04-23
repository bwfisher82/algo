def suboptimal(numbers, target_sum):
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


def worst_case(numbers, target_sum):
    """Quadratic without early return. Ahhhhh run away!"""
    result = []
    if len(numbers) == 1:
        return result
    for number_index, number in enumerate(numbers):
        for addend_index, addend in enumerate(numbers):
            if target_sum - number == addend and number_index != addend_index:
                result = [number, addend]
    return result


def optimal(numbers, target_sum):
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


def median(numbers, target_sum):
    """Here we are O(n log(n)) due to the sort call.
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
    return []


def main():
    numbers = [3, 5, -4, 8, 11, 1, -1, 6]
    target_sum = 10
    # print(worst_case(numbers, target_sum))
    # print(suboptimal(numbers, target_sum))
    # print(median(numbers, target_sum))
    print(optimal(numbers, target_sum))


if __name__ == "__main__":
    main()
