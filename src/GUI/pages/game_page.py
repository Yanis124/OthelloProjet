import tkinter as tk
from src.GUI.constantes import BUTTON_STYLE, PAGE_BG_COLOR, TITLE_TEXT_FONT, BORDER_COLOR, GRID_COLOR, CANVAS_WIDTH, CANVAS_HEIGHT, CIRCLE_RADIUS, NUMBER_CIRCLE_SIZE, BLACK_CIRCLE_X_CORDINATE, WHITE_CIRCLE_X_CORDINATE
from src.GUI.components.grid import Grid
from tkinter import simpledialog, messagebox
from src.Game.othello_game import OthelloGame

from src.GUI.constantes import SQUARE_SIZE,CANVAS_HEIGHT,GRID_COLOR, BORDER_COLOR, CANVAS_WIDTH, TITLE_TEXT_FONT, CIRCLE_RADIUS, NUMBER_CIRCLE_SIZE, BLACK_CIRCLE_X_CORDINATE, WHITE_CIRCLE_X_CORDINATE

class GamePage(tk.Frame):

    def __init__(self, parent, controller, HomePage):
        """Initialize GamePage

        Args:
            parent : the layout that containe this page
            controller : unable GamePage to interacte with the main app (passe information, change page, etc.)
        """
        tk.Frame.__init__(self, parent, bg=PAGE_BG_COLOR)  

        self.difficulty_text = "Easy"
        
        # add a label
        self.label = tk.Label(self, text="Difficulty: " + self.difficulty_text, font=TITLE_TEXT_FONT, bg='#2c3e50', fg='white')
        self.label.grid(row=0, column=0, pady=10, padx=10, sticky='ew')

        # add a button to go back to the MenuPage
        button = tk.Button(self, text="Go Back to the Menu", command=lambda: (controller.show_frame(HomePage), self.reset_page()), **BUTTON_STYLE)
        button.grid(row=1, column=0, pady=10, padx=10, sticky='ew')

        # add the canvas that will contain the grid
        self.canvas = tk.Canvas(self, bg=PAGE_BG_COLOR, highlightthickness=0)
        self.canvas.grid(row=2, column=0, pady=(10,10), sticky='nsew')

        self.game = OthelloGame(self.canvas)
        
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
         
    def set_difficulty(self, difficulty):
        """Change the difficulty of the game"""
        
        self.label.config(text="Difficulty: " + difficulty)
        
        if difficulty == "player_vs_player" :
            self.game.game_mode = "player_vs_player"
        else :
            self.game.difficulty = difficulty
            self.game.game_mode = "player_vs_ai"
            self.game.set_ai_parametres()
        
    def color_choice(self):
        """set the player color and the AI color"""
        
        player_color = simpledialog.askstring("Choix de la couleur", "Quelle couleur voulez-vous être ? (Noir/Blanc)", parent=self)
        if player_color is None:
            return  
        elif player_color.lower() in ["noir", "blanc"]:
            couleur_joueur = "black" if player_color.lower() == "noir" else "white"
            self.game.set_min_player_color(couleur_joueur)
        else:
            messagebox.showerror("Erreur", "Veuillez choisir entre Noir et Blanc.")
            self.color_choice()  # Try again if the entry is invalid
            
        self.game.game_loop(True)
                        
    def reset_page(self):
        """resest the game and the grid as a new game is started"""
        
        # add the canvas that will contain the grid
        self.canvas = tk.Canvas(self, bg=PAGE_BG_COLOR, highlightthickness=0)
        self.canvas.grid(row=2, column=0, pady=(10,10), sticky='nsew')
        self.game = OthelloGame(self.canvas)
            
        





        
        
        
        
                        
   