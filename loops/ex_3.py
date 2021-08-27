# and doubles that number. Then use the doubles() function in a loop to double the number 2 three times, displaying each result on a separate line. Here is some sample output:
def doubles(number):
    for number in range(1, 4):
        number = number ** 2
        print(number)

doubles(input("Enter a number: "))