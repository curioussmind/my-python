number = int(input("Enter your favorite number: "))

for n in range(1, number + 1):
    if number % n == 0:
        print(f"{n} is the factor of {number}.")
