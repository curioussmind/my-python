# The Python continue statement immediately terminates the current loop iteration. Execution jumps to the top of the loop, and the controlling expression is re-evaluated to determine whether the loop will execute again or terminate.
n = 5
while n >0:
    n -= 1
    if n == 2:
        continue # termination and python whill check the expression and continue the program
    print(n)
print("Loop ended!")