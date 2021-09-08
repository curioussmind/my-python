data = ((1, 2), (3, 4))
row = 0
for n in data:
    total = n[0] + n[1]
    row += 1
    print(f"Row {row} sum: {total}")

numbers = [4, 3, 2, 1]
numbers_copy = numbers[:]
numbers.sort()
print(numbers)
print(numbers_copy)
