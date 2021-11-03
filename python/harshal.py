print("Hello, world! This is Python 3!")

"""
Knapsack 0/1 -- O(n) unless pre-sorting is required

You are a farmer. You are harvesting apples.
There are sections in the farm.
Your apples are very sensitive. You cannot harvest adjacent sections.

[50, 10, 20, 30, 5] => 75? 80?

Your goal is to harvest maximum apples.

you can only carry 70 maximum harvest at a time
k = 70

meeting rooms
airplane landing schedules
number of runways needed to land airplanes
invert binary tree
number of islands
word search
two sum
three sum
four sum
"""


def max_apples(sections):
    # previous 2 maximum harvests

    prev1 = 0
    prev2 = 0
    for harvest in sections:
        temp = prev1;
        prev1 = max(prev2 + harvest, prev1)
        prev2 = temp
        val = harvest

    return prev1


sections = [50, 10, 20, 30, 5]
print(max_apples(sections))