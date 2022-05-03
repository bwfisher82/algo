def suboptimal(array):
    return sorted([i ** 2 for i in array])
    # simple, but O(n log(n)) T, O(n) S


def optimal(array):
    head_index = 0
    tail_index = len(array) - 1
    result = [0] * len(array)
    result_index = tail_index

    while result_index >= 0:
        head = abs(array[head_index])
        tail = abs(array[tail_index])
        if head > tail:
            result[result_index] = head ** 2
            head_index += 1
        else:
            result[result_index] = tail ** 2
            tail_index -= 1
        result_index -= 1

    return result
    # we are now O(n) time as we are not running sorted(), and space is still O(n)
    # for big O, all of O(n) space is in line 12
    # for big O, all of O(n) time is in the while loop
    #
    # if this was real code, we may not use while, as it is slightly slower than if/for in Python
    # because reasons, but for the purposes of this example, it is fine


def main():
    array = [1, 2, 3, 5, 6, 8, 9]
    return optimal(array)


if __name__ == "__main__":
    main()
