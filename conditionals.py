"""
A section of code that compares two pieces of information is called a conditional statement. 
You can use conditionals to create different paths through the program. 
Using comparative operators, you can write a program that makes decisions.
"""

# Use the input() function to get information from the user:
userReply = input("Do you need to ship a package? (Enter yes or no) ")
# Use the if statement to print a response.
if userReply == "yes": # The == symbol is a comparative operator. It means is equal to.
    print("We can help you ship that package")
# To handle the condition where the user doesn't want to ship a package, use the else statement:
else:
     print("Please come back when you want to ship a pakage. Thank you.")


userReply = input("Would you like to buy stamps, buy an envolope or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamps to choose from.")
    # When you have multiple conditions, you can use the elif statement, which is short for else-if.
elif userReply == "envelope":
    print("We have many envelope izes to choose from")
elif userReply == "copy" :
    print("How many copies would you like? (Enter a number) ")
else:
    print("Thank you, please come again.")

# The elif statement always comes after an if statement and before the else statement.