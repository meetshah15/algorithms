class Solution:
    def getLetter(self, s):
        number_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        return number_map[s]

    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []

        small_op = self.letterCombinations(digits[1:])
        string = self.getLetter(digits[0])
        ans = []
        if len(small_op) == 0:
            for i in string:
                ans.append(i)
        else:
            for i in string:
                for j in range(len(small_op)):
                    ans.append(i + small_op[j])

        return ans


if __name__ == '__main__':
    solution = Solution()
    solution.letterCombinations('234')