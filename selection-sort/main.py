# Implement the Selection Sort Algorithm

def selection_sort(array):
    n = len(array)

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

    return array

if __name__ == "__main__":
    numbers = [33, 1, 89, 2, 67, 245]

    print("Unsorted array: ")
    print(numbers)

    selection_sort(numbers)

    print("Sorted array: ")
    print(numbers)
