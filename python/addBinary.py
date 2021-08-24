def process_answer(carry, temp_answer, final_answer):
    if carry and temp_answer == 1:
        final_answer += "0"
    elif carry and temp_answer == 0:
        final_answer += "1"
        carry = False
    elif not carry:
        final_answer += str(temp_answer)

def addBinary(a, b) -> str:

    i = len(a) - 1
    j = len(b) - 1
    result = ""
    carry = 0

    while i >= 0 or j >= 0 or carry:
        total = carry

        if i >= 0:
            total += int(a[i])
            i -= 1

        if j >= 0:
            total += int(b[j])
            j -= 1

        result += str(total % 2)
        carry = total // 2

    return result[::-1]


if __name__ == '__main__':
    print(addBinary("11", "1"))
