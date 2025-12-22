'''
Program: Storage Space Caclulation
Programmede by: CLARK JAO ALARCON
'''

gb_num = int(input("How many gigabytes can your thumb drive store? "))
width = int(input("What is the width of each picture in pixels? "))
height = int(input("What is the height of each picture in pixels? "))

total_pixels = width * height

bytes = gb_num * 1024 * 1024 * 1024
pictures = int(bytes/(total_pixels*3))

print(pictures)