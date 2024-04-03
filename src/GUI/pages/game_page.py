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
        
        left_padding_frame = tk.Frame(self, width=20, bg=PAGE_BG_COLOR)
        left_padding_frame.grid(row=0, column=0, rowspan=3, sticky='ns')
        
        # add a label
        self.label = tk.Label(self, text="Difficulty: " + self.difficulty_text, font=TITLE_TEXT_FONT, bg='#2c3e50', fg='white')
        self.label.grid(row=0, column=0, pady=10, padx=10, sticky='ew')

        # add a button to go back to the MenuPage
        button = tk.Button(self, text="Go Back to the Menu", command=lambda: (controller.show_frame(HomePage), self.reset_page()), **BUTTON_STYLE)
        button.grid(row=1, column=0, pady=10, padx=10, sticky='ew')

        # add the canvas that will contain the grid
        self.canvas = tk.Canvas(self, bg=PAGE_BG_COLOR, highlightthickness=0)
        self.canvas.grid(row=0, column=1, pady=(10,10), sticky='nsew')
        

        self.game = OthelloGame(self.canvas, self)
        
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        
        self.message_box = tk.Text(self, height=20, width=30)
        self.message_box.grid(row=2, column=1, padx=(10,0), sticky='nsew')
        self.message_box.config(
            state='normal', 
            background='#34495e',  
            foreground='white', 
            font=('Arial', 12),  
            borderwidth=2,  
            relief="solid",  
            padx=10,  
            pady=10, 
        )
        self.message_box.config(state='disabled')  

        scrollbar = tk.Scrollbar(self, orient="vertical", command=self.message_box.yview)
        scrollbar.grid(row=2, column=2, sticky='ns') 

        self.message_box.config(yscrollcommand=scrollbar.set)


        self.canvas.grid(row=2, column=0, pady=(10,10), sticky='nsew')



    def add_message(self, message):
        self.message_box.config(state='normal') 
        self.message_box.insert(tk.END, message + "\n")  
        self.message_box.config(state='disabled')
        self.message_box.see(tk.END) 
        
        
        
    def set_difficulty(self, difficulty):
        """Change the difficulty of the game"""
        
        self.label.config(text="Difficulty: " + difficulty)
        self.game.difficulty = difficulty
        self.game.set_ai_parametres()

    def color_choice(self):
        """set the player color and the AI color"""
        
        player_color = simpledialog.askstring("Choix de la couleur", "Quelle couleur voulez-vous être ? (Noir/Blanc)", parent=self)
        if player_color is None:
            return  
        elif player_color.lower() in ["noir", "blanc"]:
            couleur_joueur = "black" if player_color.lower() == "noir" else "white"
            self.game.set_max_player_color(couleur_joueur)
        else:
            messagebox.showerror("Erreur", "Veuillez choisir entre Noir et Blanc.")
            self.color_choice()  # Try again if the entry is invalid
            
        self.game.game_loop(True)
                        
    def reset_page(self):
        """resest the game and the grid as a new game is started"""
        
        self.game = OthelloGame(self.canvas)
            
        





        
        
        
        
                        
   