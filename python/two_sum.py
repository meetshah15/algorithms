def two_sum(nums: [int], target: int) -> [int]:

    seen = {}

    for index in range(0, len(nums)):
        residue = target - nums[index]

        if residue in seen:
            return [seen[residue], index]

        seen[nums[index]] = index
        index += 1


if __name__ == '__main__':
    print(two_sum([3, 4, 9, 8, 6, 10], 10))
