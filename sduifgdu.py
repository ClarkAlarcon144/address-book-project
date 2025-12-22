import random


play = input("Do you want to play? Yes or No\n").strip().lower()

while play == "yes":
    num1 = random.randint(0,10)
    num2 = random.randint(0,10)

    if num1 < num2:
        num1, num2 = num2, num1

    correct_ans = num1 - num2
    
    question = f"What is {num1} - {num2}? "
    
    user_answer = int(input(question))

    while user_answer != correct_ans:
        print("Wrong answer. Try again. What is ", num1, " - ", num2, "? ")
        user_answer = int(input("Wrong answer. Try again. What is ", num1, " - ", num2, "? "))

    print("Your answer is correct!")
    play = input("You want to try again? (yes/no)")





