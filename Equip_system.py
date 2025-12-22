armor_display = [
    {
        "Equipment": "Leather Armor", 
        "HP": 10, 
        "Attack": +2, 
        "Defense": +2
    },
    {
        "Equipment": "Light Armor", 
        "HP": +15, 
        "Attack": 0,
        "Defense": +5
    }
]
weapons_display = [
    {
        "Equipment": "Wooden Sword", 
        "HP": 0, 
        "Attack": +3, 
        "Defense": +1
    },
    {
        "Equipment": "Knife", 
        "HP": 0, 
        "Attack": +4, 
        "Defense": 0
    }
]

equipments = []

def equipment_choice(equipment_type):
    print("")
    for i, eq in enumerate(equipment_type):
        print(
            f"{i+1}) {eq['Equipment']}  HP: {eq['HP']}  Attack: {eq['Attack']}  Defense: {eq['Defense']}")
    
def show_status(status):
    print(
    f"\nStats:\n"
    f"HP: {status.get('HP')}\n"
    f"Attack: {status.get('Attack')}\n"
    f"Defense: {status.get('Defense')}\n")

def show_equipment(equipments):
    print(f"Equipment: {equipments}\n")

def equip(equipment_type):
    equipment_choice(equipment_type)
    user_input = int(
        input("\nType the number of the item you wish to wear: \n")) - 1
    
    equipment_item = equipment_type[user_input]

    equipments.append(equipment_item["Equipment"])
    
    initial_status["HP"] += int(
        equipment_item.get("HP")
        )
    
    initial_status["Attack"] += int(
        equipment_item.get("Attack")
        )
    
    initial_status["Defense"] += int(
        equipment_item.get("Defense")
        )
    
    show_status(initial_status)






encounter = random.choice(level_1_monsters)
    print(
        f"A wild", encounter['Name'],"appears!"
        )