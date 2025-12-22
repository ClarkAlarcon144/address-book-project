us_citizen = False
age_req = False
resident_req = False

citizenship_input = input("Are you a citizen of the United States?\n").lower().strip()
age_input = int(input("\nWhat is your age?\n"))
residency_time_input = int(input("\nHow many years have you been a resident? (Type just the number)\n"))

citizenship_valid_inputs = ["yes","no"]

if citizenship_input in citizenship_valid_inputs and citizenship_input == "yes":
    us_citizen = True

if age_input >= 35:
    age_req = True

if residency_time_input >= 14:
    resident_req = True

if us_citizen and age_req and resident_req:
    print("You are eligible for presidendcy!")

else:
    print("You are not eligible for presidency.")



    


#Write a program that determines whether you can run for president. To run for president the constitution states: No Person except a natural born Citizen, or a
# Citizen of the United States, at the time of the Adoption of this Constitution, shall be
# eligible to the Office of President; neither shall any Person be eligible to that Office
# who shall not have attained to the Age of thirty five Years, and been fourteen Years a
# Resident within the United States [7]. Ask three questions of the user and use the
# guess and check pattern to determine if they are eligible to run for President