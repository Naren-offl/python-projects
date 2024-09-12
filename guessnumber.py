import random
num = random.randint(1,20)
guess = int(input("guess the number between 1 to 20,Here we go..."))
while num != guess:
    if(guess<num):
        print("your guess is lower")
    else:
        print("your guess is higher")
    guess = int(input("don't quit,Come Again!!!"))

print("you are won!!!")