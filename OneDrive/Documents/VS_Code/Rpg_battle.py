import random
import tkinter as tk

class Game:
    def __init__(self, root):
        self.root = root
        self.player = Character("player", 50, 30, 5, mana=50, mag_atk=10, mag_def=10, \
                                light_acc=1, normal_acc=0.8, heavy_acc=0.65, crit_chance=0.2,\
                                skills=[Skill("fireball", 10, effects=[apply_damage(10), apply_burn(5,3)])])
        self.enemy = Character("goblin", 40, 10, 10, light_acc=1, normal_acc=0.8, heavy_acc=0.65, light_chance=0.4, normal_chance=0.4, heavy_chance=0.2, crit_chance=0.1)
        self.game_over = False
        self.turn = "player"

        self.setup_ui()

    def setup_ui(self):
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill="both", expand=True)

        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        main_frame.rowconfigure(0, weight=7)
        main_frame.rowconfigure(1, weight=3)
        main_frame.columnconfigure(0, weight=1)

        display_frame = tk.Frame(main_frame)
        display_frame.grid(row=0, column=0, sticky="nsew")
        display_frame.columnconfigure(0, weight=3)
        display_frame.columnconfigure(1, weight=7)
        display_frame.rowconfigure(0, weight=1)

        self.text_log = tk.Text(display_frame, height=10, wrap="word")
        self.text_log.grid(row=0, column=0)

        self.display_area = tk.Frame(display_frame, bg="black")
        self.display_area.grid(row=0, column=1, sticky="nsew")

        self.action_frame = tk.Frame(main_frame)
        self.action_frame.grid(row=1, column=0, sticky="nsew")
        self.action_frame.rowconfigure(0, weight=3)
        self.action_frame.rowconfigure(1, weight=7)
        self.action_frame.columnconfigure(0, weight=1)
    
        self.status_frame = tk.Frame(self.action_frame)
        self.status_frame.grid(row=0, column=0, sticky="nsew")

        self.enemy_hp = tk.Canvas(self.status_frame, height=20, bg="gray")
        self.enemy_hp.pack(fill="x")

        self.enemy_max_hp = self.enemy.hp

        self.player_hp = tk.Canvas(self.status_frame, height=20, bg="gray")
        self.player_hp.pack(fill="x")
        
        self.player_max_hp = self.player.hp

        self.buttons_frame = tk.Frame(self.action_frame)
        self.buttons_frame.grid(row=1, column=0, sticky="nsew")
        self.buttons_frame.columnconfigure((0,1,2), weight=1)
        self.buttons_frame.rowconfigure(0, weight=1)

        self.enemy_label = tk.Label(self.display_area, text="Goblin", fg="white", bg="black", font=("Arial", 24))
        self.enemy_label.pack(expand=True)
        
        self.update_ui()
        self.show_main_actions()
    
    def clear_buttons(self):
        for widget in self.buttons_frame.winfo_children():
            widget.destroy()

    def log(self, message):
        self.text_log.insert("end", message + '\n')
        self.text_log.see("end")

    def show_main_actions(self):
        self.clear_buttons()

        buttons = {
            "Attack": self.show_attack_options, 
            "Defend": self.defend,
            "Skills": self.show_skill_options
            }

        for i, (btn_text, btn_function) in enumerate(buttons.items()):
            btn = tk.Button(self.buttons_frame, text=btn_text, command=btn_function)
            btn.grid(row=0, column=i, sticky="nsew")

    def fireball(self, cost=25, damage=1):
        if "burn" in self.enemy.status_effects:
            burn = self.enemy.status_effects["burn"]
            burn.append({"turns": 3})

        else:
            self.enemy.status_effects["burn"] = [{"turns": 3}]

        self.player.mana -= cost
        
        self.turn = "enemy"
        self.update_ui()
        self.enemy_turn()

    def show_attack_options(self):
        self.clear_buttons()

        buttons = {"Light Attack": "light", "Normal Attack": "normal", "Heavy Attack": "heavy"}

        for i, (btn_text, attack_type) in enumerate(buttons.items()):
            btn = tk.Button(
                self.buttons_frame, 
                text=btn_text, 
                command=lambda attack_type=attack_type: self.attack_turn(attack_type)
                )
            
            btn.grid(row=0, column=i, sticky="nsew")

    def show_skill_options(self):
        self.clear_buttons()

        skill_buttons = {}
        
        for skill in self.player.skills:
            skill_buttons[skill.name] = skill
        
        for i, (text, skill) in enumerate(skill_buttons.items()):
            btn = tk.Button(self.buttons_frame, text=text, command=lambda skill=skill: self.use_skill(skill))
            btn.grid(row=0, column=i, sticky="nsew")

    def use_skill(self, skill):
        for effect in skill.effects:
            self.log(effect(self.player, self.enemy))

        self.turn = "enemy"
        self.update_ui()
        self.enemy_turn()

    def defend(self):
        if self.game_over or self.turn != "player":
            return
        
        self.defending = True
        self.turn = "enemy"
        self.set_buttons_state("disabled")
        self.root.after(500, self.enemy_turn)
    
    def attack_turn(self, type):
        if self.game_over or self.turn != "player":
            return
        
        if self.player.defending:
            self.player.defending = False

        result = self.player.attack(type)
        self.log(f"🗡 You used {type.upper()} ATTACK!")

        if result["hit"]:
            if result["crit"]:
                self.log(f"CRITICAL HIT!")
                
            damage = self.enemy.damage(result["damage"])
            self.log(f"💥 Enemy takes {damage} damage!")
        else:
            self.log("You missed!")
            
        self.update_ui()

        self.turn = "enemy"
        self.set_buttons_state("disabled")
        self.root.after(500, self.enemy_turn)
        
    def enemy_turn(self):
        status_msgs = self.enemy.update_status()
        
        for msg in status_msgs:
            self.log(msg)

        if self.game_over or self.turn != "enemy":
            return

        attack_types = ["light", "normal", "heavy"]
        attack_chance = [self.enemy.light_chance, self.enemy.normal_chance, self.enemy.heavy_chance]

        chosen_attack = random.choices(attack_types, weights=attack_chance)[0]
        damage = self.enemy.attack(chosen_attack)["damage"]

        self.player.damage(damage)

        self.log(f"The enemy used a {chosen_attack} attack!")
        self.log(f"You took {damage} damage!")

        self.update_ui()
        
        self.turn = "player"
        self.set_buttons_state("normal")
        
    def update_ui(self):
        self.draw_hp(self.enemy_hp, self.enemy.hp, self.enemy_max_hp)
        self.draw_hp(self.player_hp, self.player.hp, self.player_max_hp)

        self.check_game_over()

    def draw_hp(self, canvas, hp, max_hp):
        canvas.delete("all")
        width = int((hp / max_hp) * 200)
        canvas.create_rectangle(0, 0, width, 20, fill="green")

    def check_game_over(self):
        if self.player.hp <= 0:
            self.log("💀 You died!")
            self.set_buttons_state("disabled")
            self.game_over = True

        if self.enemy.hp <= 0:
            self.log("🏆 Enemy defeated!")
            self.set_buttons_state("disabled")
            self.game_over = True

    def set_buttons_state(self, state):
        for btn in self.buttons_frame.winfo_children():
            btn.config(state=state)

class Character:
    def __init__(self, name, hp, atk, defense, mana=None, mag_atk=None, mag_def=None, light_chance=None, normal_chance=None, \
                 heavy_chance=None, light_acc=None, normal_acc=None, heavy_acc=None, crit_chance=None, skills=None):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense

        self.mana = mana
        self.mag_atk = mag_atk
        self.mag_def = mag_def

        self.light_chance = light_chance
        self.normal_chance = normal_chance
        self.heavy_chance = heavy_chance

        self.light_acc = light_acc
        self.normal_acc = normal_acc
        self.heavy_acc = heavy_acc

        self.crit_chance = crit_chance

        self.defending = False
        self.charging = False
        self.status_effects = {}

        self.skills = skills

    def attack(self, type):
        result = {
            "hit": False,
            "crit": False,
            "damage": 0,
            "type": type
        }

        if self.charging:
            self.charging = False
            result["hit"] = True
            result["damage"] = self.atk * 2.5
            return result
        
        if type == "charge":
            self.charging = True
            return result
        
        base_damage = self.atk

        if random.random() < self.crit_chance:
            result["crit"] = True
            base_damage *= 2

        acc = {
            "light": self.light_acc,
            "normal": self.normal_acc,
            "heavy": self.heavy_acc
        }[type]

        if random.random() < acc:
            result["hit"] = True

            multiplier = {
                "light": 0.8,
                "normal": 1,
                "heavy": 1.2
            }[type]

            result["damage"] = base_damage * multiplier
        else:
            result["damage"] = 0
        
        return result

    def damage(self, initial_damage):
        final_damage = max(0, initial_damage - self.defense)
        
        if self.defending:
            final_damage = final_damage//2
            self.defending = False

        self.hp = max(0, self.hp - final_damage)
        return final_damage

    def update_status(self):
        messages = []

        for name, status in self.status_effects.items():
            turns = []

            for turn_dict in status:
                turns.append(turn_dict["turns"])
            
            max_turns = max(turns)

            if max_turns <= 0: 
                del status
                messages.append(f"🔥 {name.capitalize()} wore off!")
            
            turn_list = []

            for turn_dict in status:
                turn_dict["turns"] -= 1
            
                if turn_dict["turns"] > 0:
                    turn_list.append(turn_dict)
            
            self.status_effects[name] = turn_list

        return messages
            
class Skill:
    def __init__(self, name, cost, effects):
        self.name = name
        self.cost = cost
        self.effects = effects

def apply_damage(damage):
    def effect(user, target):
        target.hp -= damage

        return f"{target.name.capitalize()} took {damage} damage"
    return effect

def apply_burn(damage, turns):
    def effect(user, target):
        if "burn" not in target.status_effects:
            target.status_effects["burn"] = []

        target.status_effects["burn"].append({"turns": turns})
        target.hp -= damage * len(target.status_effects["burn"])
        
        return f"🔥 Burn deals {damage} damage!\n{target.name.capitalize()} is burning for {turns} turns"
    return effect

Skill("fireball", 30,
      effects=[
          apply_damage(30),
          apply_burn(5, 3)
          ]
      )

root = tk.Tk()
game = Game(root)
root.mainloop()




