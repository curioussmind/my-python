# As long as you indent the code correctly, you can even put loops inside of other loops.

for n in range(1, 4):
    for j in range(4, 7):
        print(f"n = {n} and j = {j}")

a = ["foo", 'bar']
while len(a):
    print(a.pop(0))
    b = ['baz', 'qux']
    while len(b):
        print('>', b.pop(0))
