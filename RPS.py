import random

choices = ["rock", "paper", "scissors"]
winning_order = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

scoreboard = {"player": 0, "ai": 0}

rps_number_chosen = {"rock": 0, "scissors": 0, "paper": 0}
rps_weights = {"rock": 1, "scissors": 1, "paper": 1}
reverse_rps_weights = {"rock": 1, "scissors": 1, "paper": 1}
player_choices_history = []
turn_count = {"count": 0}
last_choice = None


print("ROCK PAPER SCISSORS:\nChoose rock, paper, or scissors, and beat the AI!")


def print_result_of_battle_against(ai_choice): #shows the result of the choice of player versus the choice of ai
    if winning_order[player_input] == ai_choice:
        print(f"You chose {player_input}\nYour opponent chose {ai_choice}\nYou win!")
        scoreboard["player"] += 1
        print(f"\n{scoreboard['player']}: {scoreboard['ai']}")

    elif player_input == ai_input:
        print(f"You chose {player_input}\nYour opponent chose {ai_choice}\nYou draw!")
        print(f"\n{scoreboard['player']}: {scoreboard['ai']}")

    elif winning_order[ai_input] == player_input:
        print(f"You chose {player_input}\nYour opponent chose {ai_choice}\nYou lose!")
        scoreboard["ai"] += 1
        print(f"\n{scoreboard['player']}: {scoreboard['ai']}")

def update_trackers_with(user_input): #updates the trackers that keep track of the algorithm shit
    global last_choice
    rps_number_chosen[user_input] += 1
    
    player_choices_history.append(user_input)
    turn_count["count"] += 1
    
    rps_weights[user_input] = min(rps_weights[user_input] + 0.4, 2)
    
    reverse_rps_weights[user_input] = min(reverse_rps_weights[user_input] + 0.4, 2)
    reverse_rps_weights[winning_order[winning_order[user_input]]] = min(reverse_rps_weights[winning_order[winning_order[user_input]]] + 0.4, 2)
    



while scoreboard["player"] != 3 and scoreboard["ai"] != 3: #the actual program executing everything
    player_input = input("\n").strip().lower()

    if last_choice == None or player_input != last_choice:
        ai_input = random.choices(
            population=list(rps_weights.keys()), 
            weights=list(rps_weights.values()), 
            k=1
            )[0]

        print_result_of_battle_against(ai_input)

        update_trackers_with(player_input)
        last_choice = player_input

    elif player_input == last_choice:
        ai_input = random.choices(
            population=list(reverse_rps_weights.keys()), 
            weights=list(reverse_rps_weights.values()), 
            k=1
            )[0]
    
        print_result_of_battle_against(ai_input)

        update_trackers_with(player_input)
        last_choice = player_input

        
    if scoreboard["player"] == 3: #this shit is for ending the shit
        print("You win!")
    
    elif scoreboard["ai"] == 3:
        print("You lose!")

