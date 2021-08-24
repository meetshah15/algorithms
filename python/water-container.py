def calculate_max_water(heights: [int]) -> int:
    initial = 0
    final = len(heights) - 1
    water = 0

    while initial < final:
        water = max(water, min(heights[initial], heights[final]) * (final - initial))
        if heights[initial] <= heights[final]:
            initial += 1
        else:
            final -= 1

    return water


if __name__ == '__main__':
    print(calculate_max_water([1,8,6,2,5,4,8,3,7]))