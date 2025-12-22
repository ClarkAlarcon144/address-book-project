import json
import os
import tkinter as tk
from tkinter import messagebox

def hello():
    messagebox.showinfo("Hi", "You clicked the button bro!")

root = tk.Tk()
root.title("Novel Tracker")

btn = tk.Button(root, text="Click me", command=hello)
btn.pack()

root.mainloop()

class Novel:
    def __init__(self, name, chapter, status, rating, thoughts):
        self.name = name
        self.chapter = chapter
        self.status = status
        self.rating = rating
        self.thoughts = thoughts
    
    def update(self, chapter=None, status=None, rating=None, thoughts=None):
        if chapter is not None:
            self.chapter = chapter
        if status is not None:
            self.status = status
        if rating is not None:
            self.rating = rating
        if thoughts is not None:
            self.thoughts = thoughts
    
Demon_Prince = Novel(
    "Demon Prince Goes to the Academy", 
    "702", 
    "Finished", 
    "10/10", 
    "Fucking incredible. I still remember this shit to this day."
    )

Academy_Genius_Blinker = Novel(
    "Academy's Genius Blinker", 
    "250", 
    "Dropped", 
    "6.5/10", 
    "It's pretty fine"
    )

Villain_Way_to_Live = Novel(
    "A Villain's Way to Live", 
    "19", 
    "Dropped", 
    "6.5/10", 
    "It's fine, I wanted to read more but didn't have the time. Kinda jsut got bored of it too."
    )

The_Extra_Academy_Survival_Guide = Novel(
    "The Extra's Academy Survival Guide", 
    "100", 
    "Dropped", 
    "6.5/10", 
    "Haven't read enough or gotten invested enough to feel that strongly about it."
    )

I_Killed_the_Academy_Player = Novel(
    "I Killed the Academy Player", 
    "245", 
    "Reading", 
    "7.5/10", 
    "Pretty good, though I don't get why they had to make Marie homophobic HAHAHAH. " \
    "Anyway, I need to keep reading to form a proper rating." 
    )

Problem_Child_of_the_Mage_Tower = Novel(
    "Problem Child of the Mage Tower",
    "10"
    "Reading"
    "??"
    "??"
)


novels = [Demon_Prince, Academy_Genius_Blinker, Villain_Way_to_Live, The_Extra_Academy_Survival_Guide, I_Killed_the_Academy_Player]

novel_data = []

for novel in novels:
    novel_data.append({
        "name": novel.name,
        "chapter": novel.chapter,
        "status": novel.status,
        "rating": novel.rating,
        "thoughts": novel.thoughts
    })

with open("novels.json", "w") as fucker:
    json.dump(novel_data, fucker, indent=4)

os.system("notepad novels.json")

with open("novels.json", "r") as fucker:
    data = json.load(fucker)

for i, novel in enumerate(novels):
    if novel == None:
        novels.append()

    novel.update(
        name=data[i]["name"],
        chapter=data[i]["chapter"],
        status=data[i]["status"],
        rating=data[i]["rating"],
        thoughts=data[i]["thoughts"]
        )
