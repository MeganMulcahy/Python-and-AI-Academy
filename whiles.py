import random

#guessed = False
#skipping while loop
guessed = True
num = random.randint(1,10)
while not guessed:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == num:
        print("YOU WIN!")
        guessed = True
    else:
        print("Wrong guess, try again!")


print("Rolling dice")
dice_roll = random.randint(1, 6)
print(dice_roll)

num_leaves = 3
for x in range(0, num_leaves):
    print("A leaf fell to the ground! " + str(x) + " leaves have fallen.")


useinput = ""
items = []

while useinput != "quit":
    useinput = input("Enter something: ")
    
    if useinput != "quit":
        items.append(useinput)
    
    print(items)