amount = int(input("Enter the amount: "))
cents = int(input("Enter cents: "))

total_in_cents = amount * 100 + cents 

five_pesos = total_in_cents // 500
fifty_cents = ((total_in_cents - five_pesos * 500) // 50)
twenty_five_cents = ((total_in_cents - five_pesos * 500 - fifty_cents * 50) // 25)
ten_cents = ((total_in_cents - five_pesos * 500 - fifty_cents * 50 - twenty_five_cents * 25) // 10)
one_cent = (total_in_cents - five_pesos * 500 - fifty_cents * 50 - twenty_five_cents * 25 - ten_cents * 10)

print("It is equivalent to")
print(five_pesos, "5pesos")
print(fifty_cents, "50c")
print(twenty_five_cents, "25c")
print(ten_cents, "10c")
print(one_cent, "1c")
print("\nProcess completed.")

