from random import randint


def suboptimal(input):
    return sorted([i**2 for i in input])
    # simple, but O(n log(n)) T, O(n) S


def optimal(input):
    head_index = 0
    tail_index = len(input) - 1
    result = [0] * len(input)
    result_index = tail_index

    while result_index >= 0:
        head = abs(input[head_index])
        tail = abs(input[tail_index])
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


def generate_input(type = None):
    if type is None:
        type = randint(1, 10)
    if type == 1:
        return [randint(-20, 20) for i in range(20)]
    elif type == 2:
        return []
    elif type == 3:
        return [randint(0,20) for i in range(10)]
    elif type == 4:
        return [randint(-20, 20) for i in range(500)]
    elif type == 5:
        return [randint(-100, 100) for i in range(100)]
    elif type == 6:
        return [randint(-2, 2) for i in range(2)]
    elif type == 7:
        return [randint(-1000, 1000) for i in range(20)]
    elif type == 8:
        return [randint(-50, 50) for i in range(1_000)]
    elif type == 9:
        return ""
    elif type == 10:
        return [randint(-1000, 1000) for i in range(1_000)]


def main():
    # print(suboptimal(generate_input()))
    # for i in range(1_000):
    #     print(optimal(generate_input()))
    print(optimal(sorted(generate_input(1))))


if __name__ == "__main__":
    main()
