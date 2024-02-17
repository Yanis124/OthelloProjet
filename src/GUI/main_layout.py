import tkinter as tk
from src.GUI.pages.home_page import HomePage
from src.GUI.pages.game_page import GamePage
from src.GUI.constantes import WINDOW_HEIGHT, WINDOW_WIDTH, TITLE

class MainLayout(tk.Tk):
    def __init__(self, *args, **kwargs):
        """Initialize a layout that containe 2 pages """
        
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry(WINDOW_WIDTH + "x" + WINDOW_HEIGHT)
        self.title(TITLE)
        self.resizable(False, False)

        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}
        pages={HomePage : GamePage, GamePage : HomePage }

        # add HomePage and GamePage to the layout
        for F in (HomePage, GamePage):
            frame = F(container, self, pages[F])
            
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont, difficulty = None):
        """navigate beween pages 

        Args:
            cont : the page we want to navigate to
            difficulty : set a difficulty to the game if GamePage is the page we navigate to
        """
        frame = self.frames[cont]
        if difficulty:
            frame.set_difficulty(difficulty)
        frame.tkraise()

