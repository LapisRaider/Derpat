import tkinter as tk
import random

from vector2 import Vector2

class Notepad(): 
    def __init__(self, **kwargs):
        notes = [
            "Your CAP cannot even afford mentos.",
            "KEITH WAS HERE WOOOO.",
            "I couldn't think of anything to write.",
            "Your life is like poopoo.", "HEHEXD.",
            "Am I a Dog? A Cat? You'll never find out ;)",
            "Bark Bark Meow Meow",
            "Your mouse looking real good right now",
            "Doing work? Not when I'm here."
        ]
        note = notes[random.randint(0, len(notes) - 1)]

        self.window = tk.Toplevel()
        self.closing = False

        # default window width and height
        self.width = 300
        self.hisHeight = 300
        self.text_area = tk.Text(self.window)
        self.menu_bar = tk.Menu(self.window)

        # To add scrollbar
        self.scroll_bar = tk.Scrollbar(self.text_area)
        
        self.text_area.insert(tk.END, note)

        # Set icon
        try:
            self.window.wm_iconbitmap("Notepad.ico")
        except:
            pass

        # Set window size (the default is 300x300)
        try:
            self.width = kwargs['width']
        except KeyError:
            pass

        try:
            self.height = kwargs['height']
        except KeyError:
            pass

        # Set the window text
        self.window.title("You have a note!")

        # Center the window
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # For left-alling
        left = (screen_width / 2) - (self.width / 2)

        # For right-allign
        top = (screen_height / 2) - (self.height / 2)

        self.pos = Vector2(left,top)

        # For top and bottom
        self.window.geometry('%dx%d+%d+%d' % (self.width,
                                              self.height,
                                              left, top))

        # To make the textarea auto resizable
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        # Add controls (widget)
        self.text_area.grid(sticky=tk.N + tk.E + tk.S + tk.W)

        self.window.config(menu=self.menu_bar)

        self.scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

        # Scrollbar will adjust automatically according to the content
        self.scroll_bar.config(command=self.text_area.yview)
        self.text_area.config(yscrollcommand=self.scroll_bar.set)
        self.window.protocol("WM_DELETE_WINDOW",self.close)

    def update(self):
        self.window.geometry('+{x}+{y}'.format(x=str(round(self.pos.x)),y=str(round(self.pos.y))))
        self.window.update()

    def close(self):
        self.closing = True