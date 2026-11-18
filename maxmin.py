number_list = input("Enter some numbers separated by a space: ")
numbers = number_list.split(" ")


smallest = numbers[0]
for n in numbers:
    if n < smallest:
        smallest = n

largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n

print([smallest, largest])
