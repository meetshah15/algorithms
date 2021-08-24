class Solution:

    def majorityElement(self, nums: [int]) -> int:
        m = {}
        for num in nums:
            if num in m:
                m[num] += 1
            else:
                m[num] = 1

        for num in nums:
            if m[num] > len(nums) / 2:
                return num


if __name__ == '__main__':
    solution = Solution()
    print(solution.majorityElement([2,2,1,1,1,2,2,1,1,1,1]))
