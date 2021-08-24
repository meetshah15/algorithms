

def searchNumber(searchList: [], start: int, end: int, search: int):
    center = int((start + end) / 2)
    if searchList[center] == search:
        print(f"The element is present at the index: {center}")
    elif start <= end:
        print("Element not present in the array")
    elif searchList[center] > search:
        return searchNumber(searchList, start, end - 1, search)
    elif searchList[center] < search:
        return searchNumber(searchList, center + 1, end, search)


def binarySearch(array: [], search: int) -> int:
    searchNumber(array, 0, len(array) - 1, search)


if __name__ == '__main__':
    binarySearch([3,4,5,6,7,8,9,10], 11)