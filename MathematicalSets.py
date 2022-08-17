#/**
 #* *Copyright (C), 2022-2023, Sara Echeverria (bl33h)
    # *@author Sara Echeverria
    # *FileName: Mathemical Sets
    # @version: I
    #- Creation: 01/08/2022
    #- Last modification: 16/08/2022

# Universe set
U = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

# Empty sets
set1 = []
set2 = []

# Size for each set
size = 10

# File reading and elements added by console
for i in range(size):
    print("\nEnter 10 respective elements for each set, remember that they are only the letters of the alphabet and the digits on your keyboard", i + 1)
    item1 = input("Item for the first set: ")
    item2 = input("Item for the second set: ")

    set1.append(item1)
    set2.append(item2)

# Print of each set
for i in range(1):
    print("\nFirst set (A):", set1[0], set1[1], set1[2], set1[3], set1[4], set1[5], set1[6], set1[7], set1[8], set1[9])
    print("Second set (B):", set2[0], set2[1], set2[2], set2[3], set2[4], set2[5], set2[6], set2[7], set2[8], set2[9])

# Change from mutable to immutable
A = {set1[0], set1[1], set1[2], set1[3], set1[4], set1[5], set1[6], set1[7], set1[8], set1[9]}
B = {set2[0], set2[1], set2[2], set2[3], set2[4], set2[5], set2[6], set2[7], set2[8], set2[9]}

# Operations
# Union
unionOperation = A.union(B)
print("\nA union B :")
print(unionOperation)

# Intersection
intersectionOperation = A.intersection(B)
print("\nA intersection B :")
print(intersectionOperation)

# Difference from A to B
differenceOperation = A.difference(B)
print("\nA-B :")
print(differenceOperation)

# Difference from B to A
differenceOperation1 = B.difference(A)
print("\nB-A :")
print(differenceOperation1)

# Complement from A to U
differenceOperation = U.difference(A)
print("\nA∁ :")
print(differenceOperation)

# Complement from B to U
differenceOperation1 = U.difference(B)
print("\nB∁ :")
print(differenceOperation1)

# Search for a specific element in one of the sets
# Boolean       
keepGoing = True

# While cycle
while keepGoing:
    print("\n--- Would you like to search for a specific element in one of the sets? ---\n")
    print("1. Yes")
    print("2. No")
    
    options = input("Type the number that corresponds to the option you wanna execute: ")
    
    # First option
    if options == "1": # Search for a specific element in one of the sets
        cont = True
        print("\nIn what set would you like to check the existence of the element?")
        while cont:
            print("1. First set.")
            print("2. Second set.")
            choice = input(" ")
            if choice == "1":
                searchableElement = input("Type element you would like to search: ")
                if (searchableElement in set1):
                    print("\nThe first set contains this element.")
                    keepGoing = False
                else:
                    print("\nThe element was NOT found in the first set.")
                break
            if choice == "2":
                print()
                searchableElement = input("Type element you would like to search: ")
                if (searchableElement in set2):
                    print("\nThe second set contains this element.")
                else:
                    print("\nThe element was NOT found in the second set.")
            else:
                print("\nERROR: Please type a valid option.")

    
    elif options == "2":
        keepGoing = False
    
    else:
            print("\nERROR: Please type a valid option.")