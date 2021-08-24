def convert_cel_to_far(celcius=float):
    fahrenheit = celcius * (9/5) + 32
    return fahrenheit

def convert_far_to_cel(fahrenheit=float):
    celcius = (fahrenheit - 32) * (5/9)
    return celcius

cel = float(input("enter a temperature in degree C:"))
cel_in_fah=convert_cel_to_far(cel)
print(f"{cel} degrees C = {cel_in_fah} degrees F.")

fah = float(input("Enter a temperature in degree F: "))
fah_in_cel = convert_far_to_cel(fah)
print(f"{fah} degress F = {fah_in_cel} degrees C.")