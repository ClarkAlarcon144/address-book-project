import re

while True:
    try:
        expression_o = input("").strip().replace("x", "*")
        if not re.fullmatch(r"[0-9+\-/*. ]+", expression_o):
            raise ValueError
        answer = eval(expression_o)
        print(round(answer, 4))

    except ZeroDivisionError:
        print("Dividing by zero")
    except SyntaxError:
        print("Syntax Error")
    except ValueError:
        print("Invalid Characters")



def infix_to_postfix(expression):

if not re.fullmatch(r"[0-9+\-+/* .()]+", expression):
    print(("Invalid characters in expression"))


def interpret_result(result): #interprets the result that you got and links the yes or no to the text it corresponds to. If yes, prints yes text; if no, prints the no text.
    current_scene = text[0]

    if result == "yes":
        print(current_scene.get("y"))
        if "Game Over" not in str(current_scene.get("y")):
            current_scene = text.pop(0)
            current_choice = input(questions.pop(0))

    elif result == "no":
        print(current_scene.get("n"))
        if "Game Over" not in str(current_scene.get("n")):
            current_scene = text.pop(0)
            current_choice = input(questions.pop(0))

    else:
        print("\nWhat the hell does that mean? You stand there for a good minute looking like an idiot.")
        input("")

for current_choice in questions:
    interpret_result(result)





if not re.fullmatch("Game Over", final):
    current_scene = text.pop(0)
    current_choice = input(questions.pop(0))
    result = interpret_choice(current_choice)
    interpret_result(result)

   
i need it to run once, and then take the input and intepret it and intepret result. Then if it was a game over, it asks again. But, if it wasn't,
it will pop from the list and intepret choice and interpret result. loop this until the choices are exhausted.






while "Game Over" in str(interpret_result(result)):
    current_choice = input(questions[0])
    result = interpret_choice(current_choice)
    interpret_result(result)

   


while "Game Over" not in str(interpret_result(result)):
    try:
        current_scene = text[0]
        current_choice = input(questions[0])
        result = interpret_choice(current_choice)
        interpret_result(result)

        elif ""
            current_choice = input(questions.pop(0))
            result = interpret_choice(current_choice)
            interpret_result(result)
    except:



current_choice = input(questions.pop(0))
result = interpret_choice(current_choice)
interpret_result(result)




level_2_monsters = [{"Name": "Orc", "HP": "50", "Attack": "20", "Defense": "20"},
                    {"Name": "Skeleton", "HP": "15", "Attack": "10", "Defense": "5"},
                    {"Name": "Ghoul", "HP": "40", "Attack": "10", "Defense": "0"}]









player_input = input("\n").strip().lower()
ai_input = random.choice(choices)

print_result_of_battle_against(ai_input)

update_trackers_with(player_input)