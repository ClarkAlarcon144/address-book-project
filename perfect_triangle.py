import random

num = random.randint(0,100)
guess = int(input("Guess a magic number between 0 and 100\nEnter your guess: "))

while guess != num:
	if guess > num:
		print("Your guess is too high")
		guess = int(input("Enter your guess: "))
		continue

	elif guess < num:
		print("Your guess is too low")
		guess = int(input("Enter your guess: "))
		continue

if guess == num:
	print("Yes, the number is ", num)