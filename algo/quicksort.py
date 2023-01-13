# First, partition the array into two groups
# Elements on the left are smaller, on the right are bigger than the pivot
def partition(arr: list[int], left: int, right: int):
    # Take the last element as the pivot
    pivot = arr[right]
    i = left - 1

    for j in range(left, right):
        # If current element is smaller than the pivot
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap them

    # Swap with the last element iterated
    pos = i + 1
    arr[right], arr[pos] = arr[pos], arr[right]

    return pos


def quick_sort(arr: list[int], left: int, right: int):
    if left < right:
        pi = partition(arr, left, right)
        quick_sort(arr, left, pi - 1)
        quick_sort(arr, pi + 1, right)
    pass


sample_array = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(sample_array, 0, len(sample_array) - 1)
print(sample_array)
