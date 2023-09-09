import numpy as np

#Initialize variables
total = 0
maxCal = 0
file = open("input.txt")


for line in file:
    #Strip \n
    strippedLine = line.rstrip('\n')

    #If new elf, check for max calories
    if not strippedLine:
        maxCal = max(total, maxCal)
        total = 0
        continue

    #Add Calories to running total 
    total += int(strippedLine)


print("Max Calories: " + str(maxCal))
