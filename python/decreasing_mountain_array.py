def check_if_mountain(data: []) -> bool:

    i = 1
    while i < len(data) and data[i] > data[i-1]:
        i += 1

    if i == len(data) or i == 1:
        return False

    while i < len(data) and data[i] < data[i-1]:
        i += 1

    return i == len(data)


if __name__ == '__main__':
    print(check_if_mountain([3, 5, 4]))
