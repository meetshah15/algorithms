
def isBadVersion(version) -> bool:
    return version >= 3


def first_bad_version(n: int) -> int:
    right = 0
    left = n
    while left >= right:
        mid = int((left + right) / 2)
        if isBadVersion(mid):
            if mid == 0 or not isBadVersion(mid - 1):
                return mid
            left = mid - 1
        else:
            right = mid + 1

    return -1


if __name__ == '__main__':
    print(first_bad_version(5))

