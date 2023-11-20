from datetime import date

totover = 0
totunder = 0
for a in range(7):
    year = int(input(f'In what year the person #{a+1} was born?'))
    age = date.today().year - year

    if age >= 18:
        totover += 1
    else:
        totunder += 1

print(f"Overage people {totover}\nUnder age people {totunder}.")



