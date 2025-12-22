'''
Program: pH calculation
Programmed by: CLARK JAO ALARCON
'''

import random
import math

pKa = float(input("Please enter a value for pKa: "))

cbc = random.random()
cac = random.random()

pH = pKa + math.log10(0.820/0.241)

print("Your pKa was ", round(pKa, 3))
print("Your randomly assigned conjugate base concentration is ", round(cbc, 3))
print("Your randomly assigned conjugate acid concentration is ", round(cac, 3))
print("The pH of this solution is ", round(pH, 3))


print(round(cbc, 3))