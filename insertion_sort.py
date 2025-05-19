def insertion_sort(arr):
    """
    Sorts the input list in-place in monotonically decreasing order using insertion sort.
    """
    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        current = arr[i]    # Current element to be sorted/positioned
        j = i - 1       # Index of the element before the current element being sorted

        # Shift all the previous elements - arr[0..i-1] - that are less than the current element to one position ahead
        while j >= 0 and arr[j] < current:
            arr[j + 1] = arr[j]   # Move the element one position ahead
            j -= 1                # Move to the previous element

        arr[j + 1] = current


# Example
if __name__ == "__main__":
    print("----- EXAMPLE 1 -----")
    numbers = [11, 14, 8, 19, 11, 16]
    print("Original array:", numbers)
    insertion_sort(numbers)
    print("Sorted array:", numbers)
    print("\n----- EXAMPLE 2 -----")
    numbers = [10, 9, 8, 7, 6]
    print("Original array:", numbers)
    insertion_sort(numbers)
    print("Sorted array:", numbers)
    print("\n----- EXAMPLE 3 -----")
    numbers = [6, 7, 8, 9, 10]
    print("Original array:", numbers)
    insertion_sort(numbers)
    print("Sorted array:", numbers)
