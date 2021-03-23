# Write an if statement to determine whether a variable holding a year is a leap year.

year = int(input("Introduce un año: "))

if (year%4 == 0 and year%100 == 0) or (year%4 == 0 and year%400 != 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")