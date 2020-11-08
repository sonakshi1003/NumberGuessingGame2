import random

value = random.randint(1,9)
Guess=int(input("Guess which number will come between 1 to 9 ?"))

if(Guess>value):
    print("Sorry you are wrong :(")
elif(Guess<value):
    print("Sorry you are wrong :(")
else:
    print("You are right!:)")
