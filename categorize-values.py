myMixedList=[12, 3456789, 1.234, True, False, "My dog is on the bed.", "12"]
for item in myMixedList: # traverse the list and print the data type for each item in the list:
    print("{} is for the data type {}".format (item,type(item)))