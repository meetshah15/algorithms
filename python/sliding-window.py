
def slidingWindow(listData: [], slide: int) -> int:
    sum = -999999

    for i in range(0, len(listData) - 1):
        currentSum = 0
        for item in range(0, slide):
            currentSum += listData[i + item]
        sum = max(sum, currentSum)

    print(f"Max sum is: {sum}")


if __name__ == '__main__':
    listData = [20, 40, -10, 100, 55, -24, 180, 10, 56, 290]
    slidingWindow(listData, 2)
