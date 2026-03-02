from random import randint
import random
import time

range1 = int(input("what is the lowest number in your range?: "))
range2 = int(input("what is the biggest number in your range?: ")) 
winning_num =  random.randint(range1, range2)

print("Selecting random number...")
time.sleep(random.randint(1,5))
print("Random Number Selected!")

def run_guess():
    Guess = int(input("What is your guess?: "))
    if Guess > winning_num:
        print("Guessed number is too large!")
        run_guess()
    else:
        if Guess == winning_num:
            print("Congrats you win!")
        else:
            print("Guessed number too low!")
            run_guess()


run_guess()
