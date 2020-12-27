def showProperties(number):
  print("Value: {}".format(number))
  print(f'Type of value: {type(number)}')


ınput1 = input("1- Enter a number: ")
ınput2 = int(input("2- Enter a integer number: "))
ınput3 = float(input("3- Enter a float number: "))
ınput4 = int(input("4- Enter a number: "))
ınput5 = input("5- Enter a text: ")
print()

showProperties(ınput1)
showProperties(ınput2)
showProperties(ınput3)
showProperties(ınput4)
showProperties(ınput5)
