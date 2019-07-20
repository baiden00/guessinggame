import time
from random import*


print("Guessing Game Time!!! ")
print("Can you guess the secret number? ")
print("Please choose Easy, Medium or Hard")

def easy_level():
    guessesleft = 15
    secretnum = randint(1,101)
    
    while True:
        try:
           guess = input("Guess the secret number ")
           while guess < 0:
               print("Type in a positive number ")
               break
           break
        except NameError:
            print "Please input a number "
            print ""
        
    
    
    while True:
        if guess == secretnum:
            print("You guessed the right number! ")
            break
        
        elif guess > 100 and guess not < 0:
            print("Your range is from 1-100, try again")
            print("")
            guess = input("Guess the secret number ")
            continue
        
        elif guess != secretnum and guess > secretnum:
            guessesleft = guessesleft -1
            print("Wrong guess, please guess lower")
            print("You have" + " " + str(guessesleft) + " guesses left")
            print("")
            guess = input("Guess the secret number ")
            
            if guessesleft == 0:
                print("Sorry you ran out of guesses ")
                print("The secret number was" + " " + str(secretnum) + "!")
                break
            continue
        
        elif guess != secretnum and guess < secretnum:
            guessesleft = guessesleft -1
            print("Wrong guess, please guess higher")
            print("You have" + " " + str(guessesleft) + " guesses left")
            print("")
            guess = input("Guess the secret number ")
            
            if guessesleft == 0:
                print("Sorry you ran out of guesses ")
                print("The secret number was" + " " + str(secretnum) + "!")
                break
            continue
       
    
def medium_level():
    guessesleft = 10
    secretnum = randint(1,301)
    
    while True:
        try:
           guess = input("Guess the secret number ")
           break
        except NameError:
            print "Please input a number "
            print ""
    
    while True:
        if guess == secretnum:
            print("You guessed the right number! ")
            break
        
        elif guess > 300:
            print("Your range is from 1-300, try again")
            print("")
            guess = input("Guess the secret number ")
            continue
        
        elif guess != secretnum and guess > secretnum:
            guessesleft = guessesleft -1
            print("Wrong guess, please guess lower")
            print("You have" + " " + str(guessesleft) + " guesses left")
            print("")
            guess = input("Guess the secret number ")
            
            if guessesleft == 0:
                print("Sorry you ran out of guesses ")
                print("The secret number was" + " " + str(secretnum) + "!")
                break
            continue
        
        elif guess != secretnum and guess < secretnum:
            guessesleft = guessesleft -1
            print("Wrong guess, please guess higher")
            print("You have" + " " + str(guessesleft) + " guesses left")
            print("")
            guess = input("Guess the secret number ")
            
            if guessesleft == 0:
                print("Sorry you ran out of guesses ")
                print("The secret number was" + " " + str(secretnum) + "!")
                break
            continue  
   
        
def hard_level():
    guessesleft = 5
    secretnum = randint(1,501)
    
    while True:
        try:
           guess = input("Guess the secret number ")
           break
        except NameError:
            print "Please input a number "
            print ""
    
    while True:
        if guess == secretnum:
            print("You guessed the right number! ")
            break
        
        elif guess > 500:
            print("Your range is from 1-500, try again")
            print("")
            guess = input("Guess the secret number ")
            continue
        
        elif guess != secretnum and guess > secretnum:
            guessesleft = guessesleft -1
            print("Wrong guess, please guess lower")
            print("You have" + " " + str(guessesleft) + " guesses left")
            print("")
            guess = input("Guess the secret number ")
            
            if guessesleft == 0:
                print("Sorry you ran out of guesses ")
                print("The secret number was" + " " + str(secretnum) + "!")
                break
            continue
        
        elif guess != secretnum and guess < secretnum:
            guessesleft = guessesleft -1
            print("Wrong guess, please guess higher")
            print("You have" + " " + str(guessesleft) + " guesses left")
            print("")
            guess = input("Guess the secret number ")
            
            if guessesleft == 0:
                print("Sorry you ran out of guesses ")
                print("The secret number was" + " " + str(secretnum) + "!")
                break
            continue    
    
        
    
    
    
    
time.sleep(.5)

while True:
    difficulty = raw_input("Please enter the difficulty you would like to play ")
    if difficulty == "easy" or difficulty == "Easy":
        print("Your secret number is from 1-100 and you have 15 guesses ")
        time.sleep(.5)
        easy_level()
        break
    
    elif difficulty == "medium" or difficulty == "Medium":
        print("Your secret number is from 1-300 and you have 10 guesses ")
        medium_level()
        break
    
    elif difficulty == "hard" or difficulty == "Hard":
        print("Your secret number is from 1-500 and you have 5 guesses")
        hard_level()
        break
    else:
        print("Invalid choice, please choose easy, medium or hard")
        continue


        
