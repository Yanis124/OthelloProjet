import tkinter as tk
from src.GUI.constantes import TITLE_TEXT_FONT, WINDOW_HEIGHT, WINDOW_WIDTH, BUTTON_STYLE, HOMEPAGE_BUTTON_BG_COLOR, PAGE_BG_COLOR

class HomePage(tk.Frame):
    def __init__(self, parent, controller, GamePage):
        """Initialize HomePage 

        Args:
            parent : the layout that containe this page
            controller : unable HomePage to interacte with the main app (passe information, change page, etc.)
        """
        tk.Frame.__init__(self, parent, bg = PAGE_BG_COLOR )
        label = tk.Label(self, text = "Othello Game", font = TITLE_TEXT_FONT, width = WINDOW_WIDTH )
        label.pack(pady = 10,padx = 10)

        button_easy = tk.Button(self, text = "Easy", command = lambda : controller.show_frame(GamePage, "Easy"), **BUTTON_STYLE)
        button_easy.config(bg = HOMEPAGE_BUTTON_BG_COLOR)
        button_easy.pack(pady = (150, 10))

        button_normal = tk.Button(self, text = "Normal", command=lambda : controller.show_frame(GamePage, "Normal"), **BUTTON_STYLE)
        button_normal.pack(pady = 10)
        button_normal.config(bg = HOMEPAGE_BUTTON_BG_COLOR)

        button_hard = tk.Button(self, text = "Hard", command = lambda : controller.show_frame(GamePage, "Hard"), **BUTTON_STYLE)
        button_hard.pack(pady = 10)
        button_hard.config(bg = HOMEPAGE_BUTTON_BG_COLOR)
        
        button_hard = tk.Button(self, text = "player vs player", command = lambda : controller.show_frame(GamePage, "player_vs_player"), **BUTTON_STYLE)
        button_hard.pack(pady = 10)
        button_hard.config(bg = HOMEPAGE_BUTTON_BG_COLOR)