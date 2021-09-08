data = ((1, 2), (3, 4))
row = 0
for n in data:
    total = n[0] + n[1]
    row += 1
    print(f"Row {row} sum: {total}")
