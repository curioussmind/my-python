def invest(amount, rate, years):
    """display year on year growth of an initial investment"""
    for year in range(1, years + 1):
        amount = amount * (1 + rate)
        print(f"year {year}: ${amount:,.2f}")

amount = float(input("Enter a principle amount: "))
rate = float(input("Enter an annual rate of return: "))
years = int(input("Enter a number of years: "))

invest(amount, rate, years)
