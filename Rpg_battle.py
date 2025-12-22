import random

class status():
    "HP" = 50
    "Attack" = 10
    "Defense"= 5
    "Mana"=50
    "Magic Attack"= 10
    "Magic Defense"= 10
    "Defending"= False

    "burning"= False
    "burn_turns"= 0
    "burn_damage" = 0

    "poisoned"= False
    "poison_turns"= 0
    "poison_damage"= 0

    "stunned"= False
    "stun_turns"= 0

    "Defend"= "You take a defensive stance and brace yourself for an incoming attack."
    

initial_status = {
    "HP": 50, 
    "Attack": 10, 
    "Defense": 5, 
    "Mana": 50, 
    "Magic Attack": 10, 
    "Magic Defense": 10,
    "Defending": False,

    "burning": False,
    "burn_turns": 0,
    "burn_damage": 0,

    "poisoned": False,
    "poison_turns": 0,
    "poison_damage": 0,

    "stunned": False,
    "stun_turns": 0,

    "Defend": "You take a defensive stance and brace yourself for an incoming attack."
    }

player_skills = {
    "Fireball": {
        "text": "You manifest a fireball and shoot it at your opponent.",
        "cost": 10,
        "damage": 10 + initial_status["Magic Attack"]*0.5
    }
}

level_1_monsters = [
    {
        "Name": "Goblin", 
        "HP": 40, 
        "Attack": 10, 
        "Defense": 10,
        "Charging": False,
        "Alive": True,

        "burning": False,
        "burn_turns": 0,
        "burn_damage": 0,
        
        "poisoned": False,
        "poison_turns": 0,
        "poison_damage": 0,

        "stunned": False,
        "stun_turns": 0,

        "SpecialMoves": {
            "Charge": "The goblin snarls and crouches low, getting ready to lunge.",
            "Smash": "The goblin lunges with great speed and wildly swings its dagger!"
        }
    },
    {
        "Name": "Skeleton", 
        "HP": 30, 
        "Attack": 10, 
        "Defense": 0,
        "Charging": False,
        "Alive": True,


        "burning": False,
        "burn_turns": 0,
        "burn_damage": 0,

        "poisoned": False,
        "poison_turns": 0,
        "poison_damage": 0,

        "stunned": False,
        "stun_turns": 0,

        "SpecialMoves": {
            "Charge": "The skeleton shudders violently, rattling and contorting as a dark power courses through it.",
            "Smash": "The dark power causes the skeleton to rush forward, thrashing its limbs around wildly."
        }
    },
    {
        "Name": "Zombie",
        "HP": 30, 
        "Attack": 10, 
        "Defense": 5,
        "Charging": False,
        "Alive": True,

        "burning": False,
        "burn_turns": 0,
        "burn_damage": 0,

        "poisoned": False,
        "poison_turns": 0,
        "poison_damage": 0,

        "stunned": False,
        "stun_turns": 0,

        "SpecialMoves": {
            "Charge": "The zombie gets on all fours and rushes at you with great speed.",
            "Smash": "The zombie leaps toward you and bites you!"
        }
    }
]

attack_types_dict = {
    "Weak": 0.8, 
    "Medium": 1, 
    "Strong": 1.4,
    }

attack_types = [
    "Weak", 
    "Medium", 
    "Strong"
    ]

monster_attack_types = [
    "Weak", 
    "Medium", 
    "Strong", 
    "Charge"
    ]

monster_attack_chance = {
    "Weak": 0.3, 
    "Medium": 0.3, 
    "Strong": 0.2, 
    "Charge": 1
    } 

accuracy = {
    'Weak': 0.95, 
    'Medium': 0.8, 
    'Strong': 0.6, 
    'Fireball': 0.8,
    'Smash': 1
    }

valid_inputs = [
    '1', 
    '2', 
    '3', 
    'q'
    ]


def show_attacks(attack_types):
    print("Pick the number of the attack you want to make:\n")
    for i, atk in enumerate(attack_types):
        print(f"{i+1}) {atk}")
    print("\nq) Back:")

def monster_choose_action(monster):
    if monster["Charging"] == True:
        return "Smash"

    elif monster["Charging"] == False:
        weights = list(monster_attack_chance.values())
        return random.choices(
            monster_attack_types, 
            weights=weights, 
            k=1
            )[0]

def monster_attacks_player(monster):
    move = monster_choose_action(monster)
    if move == "Smash":
        print(monster["SpecialMoves"]["Smash"])

        if initial_status["Defending"] == True:
            monster_final_attack = monster["Attack"]/2
            initial_status["HP"] -= monster_final_attack
        
            initial_status["Defending"] = False

        elif initial_status["Defending"] == False:
            monster_final_attack = monster["Attack"]*2
            initial_status["HP"] -= monster_final_attack
        
        if initial_status["HP"] < 0:
            initial_status["HP"] = 0

        print(
            f"You take {monster_final_attack} damage!\nYou have {initial_status['HP']} HP left!"
            )
        monster["Charging"] = False

    elif move == "Charge":
        monster["Charging"] = True
        print(monster["SpecialMoves"]["Charge"])

    else:
        if random.random() <= accuracy[move]:
            monster_chosen_attack_percentage = attack_types_dict[move]
            monster_initial_attack = monster_chosen_attack_percentage*monster["Attack"]
            monster_final_attack = max(0, monster_initial_attack - int(0.8*initial_status["Defense"]))
            
            if initial_status["Defending"] == True:
                monster_final_attack = monster_final_attack/2
                initial_status["HP"] -= monster_final_attack

            elif initial_status["Defending"] == False:
                monster_final_attack = monster_final_attack*2.5
                initial_status["HP"] -= monster_final_attack
            
            if initial_status["HP"] < 0:
                initial_status["HP"] = 0

            print(
                f"The {monster['Name']} used a {move} Attack.\nYou take {monster_final_attack} damage!\nYou have {initial_status['HP']} HP left!"
                )
    
        else:
            print(
                f"The {monster['Name']} used a {move} Attack, but missed!"
                )


def apply_burn(character, damage, turns):
    character["burn_damage"] = damage
    character["burn_turns"] = turns

def apply_poison(character, damage, turns):
    character["poison_damage"] = damage
    character["poison_turns"] = turns

def apply_stun(character, turns):
    character["stun_turns"] = turns
    
def update_status(character):
    if character["burn_turns"] > 0:
        character["HP"] -= int(character["burn_damage"])
        character["burn_turns"] -= 1
        print(
            f"{character['Name']} takes {character['burn_damage']} burn damage.\n"
            f"The {character['Name']} has {character['HP']} HP.\n"
            f"Burn will wear off in {character['burn_turns']} turns."
            )
        
    if character["poison_turns"] > 0:
        character["HP"] -= int(character["poison_damage"])
        character["poison_turns"] -= 1
        print(
            f"{character['Name']} takes {character['poison_damage']} poison damage.\n"
            f"The {character['Name']} has {character['HP']} HP.\n"
            f"Poison will wear off in {character['poison_turns']} turns."
            )
        
    if character["stun_turns"] > 0:
        character["stun_turns"] -= 1
        print(
            f"{character['Name']} is stunned!"
            f"The {character['Name']} will get back to their senses in {character['stun_turns']} turns."
            )


def fireball(player_status, monster):
    cost = 10
    damage = 10 + player_status["Magic Attack"]*0.5
    burn_chance = 1

    if player_status['Mana'] >= cost:
        player_status["Mana"] = player_status["Mana"] - cost
        mana = player_status["Mana"]

        if random.random() <= accuracy["Fireball"]:
            monster["HP"] -= damage
            print(
                "\n"
                f"You manifest a fireball and shoot it at your opponent."
                )
            
            if monster['HP'] <= 0:
                monster['HP'] = 0
            print(
                f"The {monster['Name']} takes {damage} damage.\n"
                f"It has {monster['HP']} HP left."
                )

            if random.random() <= burn_chance:
                monster["Burning"] = True
                apply_burn(
                    monster, 
                    damage=int(initial_status["Magic Attack"]*0.2),
                    turns=3
                    )
                
                print(
                    f"The fireball sets the {monster['Name']} on fire for {monster['burn_turns']} turns!"
                )

            print(
                f"You have {mana} mana left."
                )

        else:
            print(
                f"You shoot a Fireball at your opponent, but it misses!\n"
                f"You have {mana} left"
            )

    else:
        print("You don\'t have enough mana.")

def player_attacks_monster(monster):
    user_input_chosen_attack = input("\n")

    if user_input_chosen_attack == 'q':
        return 'back'

    try:
        user_input_chosen_attack = int(user_input_chosen_attack)
        chosen_attack = attack_types[user_input_chosen_attack-1]

    except (ValueError, IndexError):
        print("Invalid attack choice!")
        return

    if random.random() <= accuracy[chosen_attack]:
        
        chosen_attack_percentage = float(attack_types_dict[chosen_attack])
        
        initial_attack = int(initial_status["Attack"] * chosen_attack_percentage)

        monster_defense = int(monster["Defense"])
        
        final_attack = max(0, initial_attack - int(0.8*monster_defense))

        monster["HP"] -= final_attack
        if monster['HP'] < 0:
            monster['HP'] = 0
        print(
            "\n"
            f"You used a {chosen_attack} Attack.\n"
            f"You deal {final_attack} damage to the {monster['Name']}!\n"
            f"The {monster['Name']} has {monster['HP']} HP left!"
            )
        
    else:
        print(
            f"You used a {chosen_attack} Attack, but you missed!")
    
def go_to_battle(level_1_monsters):
    enemy_number(level_1_monsters)
    encounter = choose_target()
    
    while initial_status["HP"] > 0 and any(enemy["HP"] > 0 for enemy in enemies_in_battle):
        

        choice = input(
            "\n" \
            "Choose action: "
            "(1) Attack, "
            "(2) Defend, "
            "(3) Skills, "
            )
        
        if choice == '1':
            show_attacks(attack_types)
            target = choose_target()
            if not target:
                break

            result = player_attacks_monster(encounter)
            if result == 'back':
                continue

            if encounter['HP'] > 0:
                monster_choose_action(encounter)
                monster_attacks_player(encounter)
                

            
        elif choice == '2':
            print(
                f"\n{initial_status['Defend']}"
                )
            
            initial_status["Defending"] = True

            monster_choose_action(encounter)
            monster_attacks_player(encounter)
            
        
            
        elif choice == '3':
            target = choose_target()
            if not target:
                break

            skill_choice = input(
                "Skills: "
                "(1) Fireball, "
                "(q) Back: "
                )
            
            if skill_choice == '1':
                fireball(initial_status, encounter)
                if encounter['HP'] > 0:
                    monster_choose_action(encounter)
                    monster_attacks_player(encounter)
                    
                    

        if choice not in valid_inputs:
            print("Invalid choice!")
            continue
        

        if encounter["HP"] <= 0:
            encounter['HP'] = 0
            print(f"You defeated the {encounter['Name']}!")
            break

        elif initial_status["HP"] <= 0:
            initial_status['HP'] = 0
            print("You have been defeated...")
            break

        update_status(encounter)


enemies_in_battle = []
enemy_count = [1,2,3]
enemy_count_chance = [0.4,0.4,0.2]


def enemy_number(monster_level):
    num_of_enemies = random.choices(enemy_count, weights=enemy_count_chance, k=1)[0]
    for _ in range(num_of_enemies):
        encounter = random.choice(monster_level)
        enemies_in_battle.append(encounter.copy())

def choose_target():
    while True:
        alive_enemies = [enemy for enemy in enemies_in_battle if enemy["HP"] > 0]

        if not alive_enemies:
            return None
        

        print("Enemies encountered:")
        for i, enemy in enumerate(enemies_in_battle):
            print(f"{i+1}) {enemy['Name']} {enemy['HP']} HP")
        print("\nChoose a target:\n")

        try:
            monster_choice = int(input(""))
            chosen_enemy = alive_enemies[monster_choice-1]
            print(f"You target the {chosen_enemy['Name']}.")
            return chosen_enemy
        
        except (ValueError, IndexError):
            print("Invalid choice! Pick again.")
            continue
        

go_to_battle(level_1_monsters)
