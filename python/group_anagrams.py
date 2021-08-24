class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        answer = {}
        for item in strs:
            temp = ''.join(sorted(item))
            if temp in answer:
                answer[temp].append(item)
            else:
                answer[temp] = [item]

        final_answer = []
        for key in answer:
            final_answer.append(answer[key])

        return final_answer


if __name__ == '__main__':
    solution = Solution()
    print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
