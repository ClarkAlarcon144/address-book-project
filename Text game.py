import difflib
import sys

def interpret_choice(user_input):
    user_input = user_input.lower().strip()
    
    yes_words = ["yes", "yeah", "yup", "yep", "yas", "sure", "ok"]
    no_words =   ["no", "nah", "nope", "naw", "not really", "I'm good", "good"]

    for word in yes_words:
        if word in user_input:
            return "yes"

    for word in no_words:
        if word in user_input:
            return "no"
        
    all_words = yes_words + no_words
    closest = difflib.get_close_matches(user_input, all_words, n=1, cutoff=0.6)

    if closest:
        if closest[0] in yes_words:
            return "yes"
        elif closest[0] in no_words:
            return "no"
        
    return "unknown"

scenes = [
    {
    "question": "\nDo you climb the tree and rest for the night? \n\n",
    "y": "You try to climb the tree, but you quickly realize that you do not know how to climb a fucking tree. In your stubborness, you finally managed to climb up a few feet. You think you're doing something, until your foot slips from the tree and you fall backwards. Your head somehow manages to hit the one rock in the vicinity and you fucking die. \n\nGame over.",
    "n": "You consider it for a second, until you remember you don't know how to climb a fucking tree. You keep walking. As you walk, you come across a cave. It looks pretty creepy, but it should be enough to sleep in for the night."
    },
    {
    "question": "\nDo you decide to stay in the cave for the night? \n\n",
    "y": "\nYou stay in the cave for the night. It's very fucking cold, so you take a some leaves to try and act as a very primitive blanket. It works somehow, and you fall asleep. \nThe next day, you wake up feeling a bit better. You get out of the cave. You're feeling a bit hungry.",
    "n": "\nYou decide not to sleep in the cave. You keep walking and walking. It's morning now and you haven't found shit. In your state of infocusness, you don't notice a slightly protruding tree root in the ground. As you take a step, your foot gets caught in the tree root and you trip over. You fall face first into a pointy rock. You bleed out and die. \n\nGame over."
    },
    {
    "question": "\nDo you go out to look for food? Surely there's nothing in the forest... hopefully... \n\n",
    "y": "You go out to look for food.",
    "n": "You don't look for food and you stay inside the cave. Days go by without any food. You die of starvation. I don't know what you were expecting to happen. \n\nGame over"
    }]


print("You're lost in a forest in the middle of nowhere. As you tredge through the woods, you come across a tree. It's pretty fucking big, and \nthere's a pretty sturdy looking branch. Sturdy enough to sustain a human... probably...")

scene_index = 0
while scene_index < len(scenes):
    scene = scenes[scene_index]

    while True:
        choice = input(scene["question"])
        result = interpret_choice(choice)

        if result == "yes":
            print(scene["y"])
            if "Game over" in scene["y"]:
                sys.exit()
            break
        elif result == "no":
            print(scene["n"])
            if "Game over" in scene["n"]:
                sys.exit()
            break
        else:
            print("\nWhat the hell does that mean? You stand there for a good minute looking like an idiot.")
    scene_index += 1



        
   
    