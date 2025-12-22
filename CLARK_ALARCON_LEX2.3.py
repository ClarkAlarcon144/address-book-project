'''
Program: Time and Distance Calculation
Programmed by: CLARK JAO ALARCON
'''

distance = float(input("What is the distance between the two trains (in miles)? "))
t1speed = float(input("What is the speed of the first train (in miles per hour)? "))
t2speed = float(input("What is the speed of the second train (in miles per hour)? "))

time = distance / (t1speed/60 + t2speed/60)

# distance = time * speed

distance1 = time/60 * t1speed
distance2 = time/60 * t2speed

print("The trains will meet in ", time, " minutes.")
print("The first train will travel ", distance1, " miles and the second train will travel ", distance2, " miles.")
