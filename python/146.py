numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

if numbers:
    largest = max(numbers)
    print("Largest number:", largest)
else:
    print("The list is empty.")