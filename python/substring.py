# Difficult To solve

def find_uncommon_substring(s: str) -> int:
    right = 0
    left = 0
    answer = 0
    n = len(s)
    m = {}

    while right < n and left < n:
        el = s[right]
        if el in m:
            left = max(left, m[el] + 1)
        m[el] = right
        answer = max(answer, right - left + 1)
        right += 1
    return answer


if __name__ == '__main__':
    print(find_uncommon_substring('abcabcbb'))
