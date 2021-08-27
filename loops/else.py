a = ["foo", "bar", "baz", "qux"]
s = input("enter the name of an item you're trying to find: ")

i = 0
while i < len(a):
    if a[i] == s:
        # processing for item found
        break
    i += 1
else:
    # processing for item not found
    print(s, "not found in the list!")
