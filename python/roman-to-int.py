def mainFunction(number):
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0

    for i, no in enumerate(number):
        if i < len(number) - 1 and roman[no] < roman[number[i+1]]:
            total -= roman[no]
        else:
            total += roman[no]
    print("Final total is " + str(total))

mainFunction("MCMLXVI")