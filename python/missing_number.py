def missing_number(n: [int]) -> int:
    length = len(n)
    actual_sum = length * (length + 1) / 2
    current_sum = sum(n)

    return actual_sum - current_sum


if __name__ == '__main__':
    print(missing_number([0,1,2,4,5,6]))