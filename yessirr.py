def maxval(num1, num2, num3):
    return max(num1, num2, num3)
    
def minval(num1, num2, num3):
    return min(num1, num2, num3)

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

print("Smallest number:", minval(num1, num2, num3))
print("Largest number:", maxval(num1, num2, num3))