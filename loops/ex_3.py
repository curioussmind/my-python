# and doubles that number. Then use the doubles() function in a loop to double the number 2 three times, displaying each result on a separate line. Here is some sample output:
def doubles(number):
    """Return the result of multiplying an input number by 2."""
    return number * 2

# call doubles function to double numbers three times
my_num = int(input("Enter a number: "))
for i in range(0, 3):
    my_num = doubles(my_num)
    print(my_num)