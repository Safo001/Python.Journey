Number = int(input('Enter a number between 0 and 9999:'))
Unit = Number // 1 % 10
Doz = Number // 10 % 10
Cent = Number // 100 % 10
Mil = Number // 1000 % 10
print("Units: {}".format(Unit))
print("Dozens: {}".format(Doz))
print("Hundreds: {}".format(Cent))
print("Thousands: {}".format(Mil))
