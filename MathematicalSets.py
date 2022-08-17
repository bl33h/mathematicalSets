#/**
 #* *Copyright (C), 2022-2023, Sara Echeverria (bl33h)
    # *@author Sara Echeverria
    # *FileName: Mathemical Sets
    # @version: I
    #- Creation: 01/08/2022
    #- Last modification: 16/08/2022

# Imports
import random

# Universe set
u = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Empty sets
set1 = []
set2 = []

# Size for each set
size = 10

# File reading and elements added by console
for i in range(size):
    print("Enter 10 respective elements for each set, remember that they are only the letters of the alphabet and the digits on your keyboard", i + 1)
    item1 = input("Item for the first set: ")
    item2 = input("Item for the second set: ")

    set1.append(item1)
    set2.append(item2)

# Print of each set
for i in range(size):
    #print("Mostrando los datos de la persona", i + 1)

    print("First set:", set1[i])
    print("Second set:", set2[i])