def contains_duplicate(nums: [int]) -> bool:
    seen = {}
    for item in nums:
        if item in seen:
            return True
        seen[item] = True

    return False


def contains_duplicate_v2(nums: [int], k: int) -> bool:
    seen = {}
    for index in range(0, len(nums)):
        if nums[index] in seen:
            if abs(seen[nums[index]] - index) <= k:
                return True
        seen[nums[index]] = index
    return False


def contains_duplicate_v3(nums: [int], k: int, t: int) -> bool:
    
    pass