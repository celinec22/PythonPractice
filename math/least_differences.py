# runs in O(1)


def least_differences(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.

    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(c - a)
    return min(diff1, diff2, diff3)


# 1 - 2 = 1
# 2 - 3 = 1
# 3 - 1 = 2

# 1 should be the least difference

print(f"Least difference simple function : {least_differences(1, 2, 3)}")

# my though process is while this runs in o(1) what if we have an array and we need to calculate
# the least difference

# we need to test every variation - we have the combiantion formula
# n(n-1)/2


def least_diff2(arr1, arr2):
    arr = sorted(set(arr1 + arr2))

    if len(arr) < 2:
        return None
    min_diff = float(
        "inf"
    )  # we want this to be high so any value we calcuate will be smaller to set to the smallest difference
    for i in range(len(arr) - 1):
        min_diff = min(min_diff, abs(arr[i] - arr[i + 1]))
    return min_diff


arr1 = [1, 2, 3]
arr2 = [3, 4, 5]


print(f"Least difference with array: {least_diff2(arr1,arr2)}")
