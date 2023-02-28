City = str(input('City name:')).strip().lower().title()
print('Does this town name starts with Santo?')
CitySplit = City.split()
print("Santo" in CitySplit[0])
