import tkinter as tk
import random

from vector2 import Vector2

class CustomWindow():
    def __init__(self):
        self.pos = Vector2()
        self.closing = False
        self.window = tk.Toplevel()
        self.window.protocol("WM_DELETE_WINDOW", self.close) # The X button now calls self.close

    # Do not destroy window immediately to prevent update from crashing due to null reference.
    def close(self):
        self.closing = True

    def is_closed(self):
        return self.closing

    def set_position(self, x_pos, y_pos):
        self.pos.x = x_pos
        self.pos.y = y_pos

    def set_position_vec2(self, pos):
        self.pos = pos

    def translate(self, x_offset, y_offset):
        self.pos.x += x_offset
        self.pos.y += y_offset

    def translate_vec2(self, offset):
        self.pos = self.pos + offset

    def get_position(self):
        return self.pos

    def update(self):
        self.window.geometry('+%d+%d' % (round(self.pos.x), round(self.pos.y)))
        self.window.update()

    def get_height(self):
        return self.window.winfo_height()

    def get_width(self):
        return self.window.winfo_width()

class ImageWindow(CustomWindow):
    TITLE = "Meme"

    def __init__(self, imagePath):
        super().__init__()

        # Set window attributes.
        self.window.title(ImageWindow.TITLE)
        self.window.attributes('-topmost', True)

        # Set image.
        self.img = tk.PhotoImage(file=imagePath)
        self.label = tk.Label(self.window, image=self.img, bd=0, bg='black')
        self.label.pack()

        # Set icon.
        try:
            self.window.wm_iconbitmap("assets/ico/image.ico")
        except:
            pass

        # Set window dimensions. (This has to go last.)
        self.window.geometry('+%d+%d' % (round(self.pos.x), round(self.pos.y)))
        self.window.update() # This is required to update the window width, otherwise it returns 1.

class NoteWindow(CustomWindow):
    TITLE = "You have a note!"

    def __init__(self, width=400, height=300):
        super().__init__()

        note = random.choice([
            "Your GPA cannot even afford mentos.",
            "I couldn't think of anything to write.",
            "Your life is like poo-poo.",
            "HEHE XD.",
            "てへぺろ :P",
            "Am I a Dog? A Cat? You'll never find out. ;)",
            "Bark Bark! Meow Meow?",
            "Your mouse looking real tasty right now.",
            "Doing work? Not when I'm here."
        ])

        # Set window attributes.
        self.window.title(NoteWindow.TITLE)

        # Text area.
        self.text_area = tk.Text(self.window)
        self.text_area.insert(tk.END, note)

        # Scrollbar.
        self.scroll_bar = tk.Scrollbar(self.text_area)

        # Set icon.
        try:
            self.window.wm_iconbitmap("assets/ico/note.ico")
        except:
            pass

        # Make the text area auto resizable.
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        # Add controls (widget).
        self.text_area.grid(sticky=tk.N + tk.E + tk.S + tk.W)
        self.scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

        # Scrollbar will adjust automatically according to the content.
        self.scroll_bar.config(command=self.text_area.yview)
        self.text_area.config(yscrollcommand=self.scroll_bar.set)

        # Set window dimensions. (This has to go last.)
        self.window.geometry('%dx%d+%d+%d' % (width, height, round(self.pos.x), round(self.pos.y)))
        self.window.update() # This is required to update the window width, otherwise it returns 1.