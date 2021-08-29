for n in range(3):
    password = input("Password: ")
    if password == "okay12345":
        break
    print("Password is incorrect.")
else:
    print("Suspicious activity!")