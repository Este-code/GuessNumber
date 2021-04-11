import random

#defining the range
a=int(input("Insert where the range starts: "))
b=int(input("Insert where the range ends: "))

guess=random.randint(a,b)

try_guess=int(input("Guess the number: "))

while(try_guess!=guess):
    if(try_guess>guess):
        print("Number too high!")
    elif(try_guess<guess):
        print("Number too low!!")
    else:
        print("Out of range!")
    try_guess=int(input("Guess again: "))

print("You won! The number is: ",try_guess)
