def find_first_and_last_occurence(nums: [int], target: int):
    left = 0
    right = len(nums) - 1
    first = -1
    final = -1

    while left <= right:
        mid = int((left + right) / 2)
        if nums[mid] == target:
            if mid == 0 or nums[mid - 1] != target:
                first = mid
                break
            right = mid - 1
        else:
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = int((left + right) / 2)
        if nums[mid] == target:
            if mid == len(nums) - 1 or nums[mid + 1] != target:
                final = mid
                break
            left = mid + 1
        else:
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
    return [first, final]


if __name__ == '__main__':
    print(find_first_and_last_occurence([5,7,7,8,8,8,8,8,10], 8))
