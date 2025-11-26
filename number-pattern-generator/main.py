# Build a Number Pattern Generator

def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."

    numbers = []

    for num in range(1, n+1):
        numbers.append(str(num))

    string = " ".join(numbers)
    return string

print(number_pattern(4))
