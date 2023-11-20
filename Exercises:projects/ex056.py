older = 0
oldername = ''
age_sum = 0
age_mean = 0
Fnumbers = 0
for p in range(1,5):
    print("---Person #{}---".format(p))
    name = str(input("Name:").format(p)).strip()
    age = int(input("Age:").format(p))
    gender = str(input("Gender [M/F]:").format(p)).strip().upper()
    age_sum += age
    if p == 1 and gender == "M":
        older = age
        oldername = name
    if age > older and gender == "M":
        older = age
        oldername = name
    print(f"The name of the oldest man is {oldername}, and he is {older}!")
    if gender == 'F' and age < 20:
        Fnumbers += 1
        print(f"That is the number of females aged under 20yo: {Fnumbers}")

age_mean = age_sum/4
print("The age mean of the group of people is {} years.".format(float(age_mean)))

