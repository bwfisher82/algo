def is_valid_subsequence(array, sequence):
    if len(array) < len(sequence) or len(sequence) < 1 or len(array) < 1:
        return False
    sequence_pointer = 0
    for element in array:
        if element == sequence[sequence_pointer]:
            sequence_pointer += 1
        if sequence_pointer == len(sequence):
            break
    return sequence_pointer == len(sequence)


def main():
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]
    return is_valid_subsequence(array, sequence)


if __name__ == "__main__":
    main()
