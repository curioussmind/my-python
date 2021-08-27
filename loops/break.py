# The Python break statement immediately terminates a loop entirely. Program execution proceeds to the first statement following the loop body.
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print("Loop ended!")
