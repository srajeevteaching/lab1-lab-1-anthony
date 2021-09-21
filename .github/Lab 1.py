# Programmers: Anthony DelVecchio
# Course: CS151, Dr. Rajeev
# Date: 9/16/21
# Lab Number: 1
# Program Inputs: An amount of milliliters
# Program Outputs: Convert milliliter amount to teaspoons and tablespoons

mil=float(input("Input Milliliters: "))
tsp=mil/5
tbs=tsp/3
print("Value in teaspoons: "+ str(tsp))
print("Value in tablespoons: "+ str(tbs))
