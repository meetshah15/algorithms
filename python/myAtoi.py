class Solution:
    def myAtoi(self, s: str) -> int:

        if s == "":
            return 0
        answer = 0
        subtract = False
        positivity_decided = False
        number_started = False

        for item in s:
            if item == ' ':
                if positivity_decided or number_started:
                    break
                continue
            elif item == '-':
                if number_started:
                    break
                if positivity_decided:
                    return 0
                subtract = True
                positivity_decided = True
                continue
            elif item == '+':
                if number_started:
                    break
                if positivity_decided:
                    return 0
                positivity_decided = True
                continue
            if not item.isnumeric():
                break
            item = int(item)

            number_started = True
            if answer == 0 and item == 0:
                continue
            elif answer == 0:
                answer = item
            elif answer >= 1:
                answer = answer * 10 + item

        if subtract:
            answer *= -1
            if answer < -2147483648:
                return -2147483648

        if answer > 2147483647:
            return 2147483647

        return answer


if __name__ == '__main__':
    solution = Solution()
    print(solution.myAtoi("-5-"))