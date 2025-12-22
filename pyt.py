height = int(input("Enter the height of the square: "))
width = int(input("Enter the width of the square: "))

print(width * "* ")
for x in range(0,height-2):
    print("*", width * " ", "*")
print(width * "* ")




import random

num1 = random.randint(0,10)
num2 = random.randint(0,10)

if num1 < num2:
    num1, num2 = num2, num1

correct_ans = num1 - num2

user_answer = int(input("What is ", num1, " - ", num2, "? ")

while user_answer != correct_ans:
    print("Wrong answer. Try again. What is ", num1, " - ", num2, "? ")
    user_answer = int(input("Wrong answer. Try again. What is ", num1, " - ", num2, "? ")
    
print("Your answer is correct!")
for x in range(0,4):
    num1 = random.randint(0,10)
    num2 = random.randint(0,10)
    correct_ans = num1 - num2
    
    question = f"What is {num1} - {num2}? "
    
    user_answer = int(input(question))
    
    if user_answer == correct_ans:
        print("You are correct!")
        
    elif user_answer == correct_ans:
        print("Your answer is wrong.")
    
    
