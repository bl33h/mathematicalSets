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
differenceOperation = B.difference(A)
print("\nB-A :")
print(differenceOperation)

# Complement from A to U
differenceOperation = U.difference(A)
print("\nA∁ :")
print(differenceOperation)

# Complement from B to U
differenceOperation = U.difference(B)
print("\nB∁ :")
print(differenceOperation)

# Search for a specific element in one of the sets