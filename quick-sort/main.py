# Implement the Quick Sort Algorithm

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]

    left = [val for val in array if val < pivot]
    middle = [val for val in array if val == pivot]
    right = [val for val in array if val > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    numbers = [20, 3, 14, 1, 5]

    print("Unsorted array: ")
    print(numbers)

    sorted_numbers = quick_sort(numbers)

    print("Sorted array: ")
    print(sorted_numbers)
