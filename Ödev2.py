d = {}
d["Name"] = name = input("Please enter your name :")
d["Surname"] = surname = input("Please enter  your last name: ")
d["Age"] = age = int(input("Please enter your age: "))
d["Date of birth"] = date_year = input(
    "Please enter your date of birth year: ")
print()
for keys, values in d.items():
  print(keys, " : ", values)
print()
if age < 18 and age > 0:
  print("You cannot go out. It is so dangerous. Home is safe for you. # StayAtHome")
elif age >= 18:
  print("You can go out but you must wear mask. have a good days.")
else:
  print("Invalıd age!")
