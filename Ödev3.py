import random as rnd 

def arrayBack(animal, line):
  newLine=""
  for a in range(0,len(animal)):
    newLine=newLine+line[a]+" "
  print(newLine)
  print() 
print("The game is so easy to play. There is a word(It is an animal) you cannot see but you can see how many letters have that word. You have to find that word. You can enter a letter or you can enter that word if you know the word. When there is only one empty character which didn't find by player. Then you have to find the word but you have only one chance to find. Good luck <3.\n")

name=input("Please enter your name: ")
print("Welcome ",name,"\n")

animals=[	"DUCK",	"PIG",	"GOAT",	"BEE",	"SHEEP",	"FISH",	"TURKEY",	"LION",	"CHICKEN","MOUSE","SNAKE","DOG","CAT"]

number=rnd.randint(0,len(animals)-1)
animal=animals[number]
print(f'The word has {len(animal)} letters.')
line=[]
for a in range(0,len(animal)) :
  line.append("_")

hasIt=False
while True:
  arrayBack(animal, line)
  number=line.count("_")
  if number == 1:
    theWord=input("You have to find that word now(Be careful you only have one chance!!): ")
    if theWord.upper()==animal:
      print(animal)
      print(f'Congratulations {name}, You are right !!')
      break
    else:
      print("You couldn't find the animal :( ")
      break
  else:
    character=input("Please enter a letter: ")
    characterUpper=character.upper()
    if animal==characterUpper :
      print(animal)
      print(f'Congratulations.{name} You found the word.!!')
      break
    for a in range(0,len(animal)):
      if characterUpper==animal[a]:
        line[a]=animal[a] 
        hasIt=True
        print("Yeaaa , you found a correct letter : ",characterUpper)
    if not hasIt:
     print("Ahhh ,try again to find a correct word.")  
print("The aplication has finished")