class Solution:
    def fourSumCount(self, nums1: [int], nums2: [int], nums3: [int], nums4: [int]) -> int:
        temp = {}
        answer = 0
        for i in nums1:
            for j in nums2:

                if i+j in temp:
                    temp[i+j] += 1
                else:
                    temp[i + j] = 1

        for i in nums3:
            for j in nums4:
                if (i + j) * -1 in temp:
                  answer += temp[(i + j) * -1]

        return answer


if __name__ == '__main__':
    solution = Solution()
    print(solution.fourSumCount([1,2], [-2,-1], [-1, 2], [0,2]))