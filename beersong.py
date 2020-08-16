#!/usr/bin/env ipython3.8

word = "bugs" # Creating a variable named word and assigning the value "bottles"
for bugs_num in range(99, 0, -1): # creates a for loop that executes on a variable called beer_num from numarical
    print(f"{bugs_num} {word} in the code.") # prints a string that inserts beer_num variable and word
    print(f"{bugs_num} {word} code.")# prints another sentence
    print("Fix one up.") # Prints another sentence
    print("Patch it up.")
    if bugs_num == 1: # checks what number beer_num is, if it's 1 then do the following
        print("Infinety number of bug in the code.") #if beer_num = 1 then print statement
    else: #if beer_num is not 1, then do the following
        new_num = bugs_num - 1 # create new variable called new_num that is beer_num minus 1
        if new_num == 1:
            word = "bugs"
        print(f"{new_num} {word} in the code.\n")
