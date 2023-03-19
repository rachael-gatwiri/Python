"""
String concatenation is the process of combining two strings into one string. 
The plus sign (+) is used to concatenate strings. 
When the plus sign (+) is used with strings, it behaves differently than when you use it for numbers. 
"""
myString="This is a string."
print(myString)
print(type(myString))
print(str(myString) + " is of the data type" + str(type(myString)))

firstString="water"
secondString="fall"
thirdString=firstString + secondString
print(thirdString)

name= input("what is your name? ")
print(name)
color=input("What is your favorite color? ")
animal=input("What is your favorite animal ")
print("{}, you like a {} {}!".format(name,color,animal))

