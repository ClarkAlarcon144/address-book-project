import tkinter as tk
import winsound

class GUI:
    def __init__(self, root):
        self.root = root

        self.load_gui()

    def load_gui(self):
        top_frame = tk.Frame(self.root)
        top_frame.pack(expand=True)

        bottom_frame = tk.Frame(self.root)
        bottom_frame.pack(expand=True)

        self.text = tk.StringVar()

        self.top_text = tk.Entry(top_frame, textvariable=self.text)
        self.top_text.pack(fill="both", expand=True)

        self.top_text.bind("<KeyRelease>",self.update_ui)
        self.top_text.bind("<Key>", self.update_ui)

        self.sound_button = tk.Button(top_frame, width=50, command=self.play_sound)
        self.sound_button.pack(side="right", fill="y", expand=True)

        self.bottom_text = tk.Text(bottom_frame)
        self.bottom_text.pack(fill="both", expand=True)

        
    def text_to_morse(self):
        dictionary = {
            'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
            'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
            'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
            'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
            'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
            'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
            'y': '-.--', 'z': '--..', '1': '.----', '2': '..---',
            '3': '...--', '4': '....-', '5': '.....', '6': '-....',
            '7': '--...', '8': '---..', '9': '----.', '0': '-----',
            '?': '..--..', '!': '-.-.--', '.': '.-.-.-', ',': '--..--'
        }

        word_list = self.text.get().split()
        self.translated_words = []

        for word in word_list:
            morse_word = []

            for char in word:
                morse_word.append(dictionary.get(char.lower()))

            self.translated_words.append(" ".join(morse_word))

        return " / ".join(self.translated_words)
    
    def update_ui(self, e):
        text = self.text_to_morse()

        self.bottom_text.delete("1.0", "end")
        self.bottom_text.insert("1.0", text)

    def play_sound(self):
        text = self.bottom_text.get("1.0", "end-1c")

        for word in text:
            for char in word:
                if char == '-':
                    winsound.Beep(1000, 450)
                elif char == '.':
                    winsound.Beep(1000, 150)
                elif char == '/':
                    winsound.Beep(37, 600)
                else:
                    continue
                

root = tk.Tk()
program = GUI(root)
root.mainloop()