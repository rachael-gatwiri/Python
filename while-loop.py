# A loop is a segment of code that repeats. 

# You will use the import command to include code that someone else wrote.
import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")


# Place the cursor on the next line after the second print() statement. Next, enter a statement that will generate a random number between 1 and 10 by using the randint() function of the random module.
number = random.randint(1,10)
#Track whether the user guessed your number by creating a variable called isGuessRight:
isGuessRight = False

# A while loop makes a section of code repeat until a certain condition is met.
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, this isn't it. Try again.".format(guess))

"""
The while loop will repeat the code inside the loop until the number is guessed correctly, which is represented by the condition isGuessRight != True in the code. 
Additionally, Python uses indentation to determine logic blocks, or what statements are considered to be part of the while loop.
You can indent a line by placing the cursor next to a statement and pressing TAB.
"""