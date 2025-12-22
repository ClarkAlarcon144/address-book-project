'''
Program: Area of a trapezoid
Programmed by: CLARK JAO ALARCON
'''

height = int(input("Enter the height of the trapezoid: "))
tbase = int(input("Enter the length of the top base of the trapezoid: "))
bbase = int(input("Enter the length of the bottom base of the trapezoid: "))

area = float(0.5 * (tbase + bbase) * height)

print("The area of the trapezoid is: ", area)