numbers = [2, 4, 1, 0, 2, -1]

smallest = numbers[0]
for n in numbers:
    if n < smallest:
        smallest = n

largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n

print([smallest, largest])
