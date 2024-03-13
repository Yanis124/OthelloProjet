import tkinter as tk
from src.GUI.pages.home_page import HomePage
from src.GUI.pages.game_page import GamePage

from src.GUI.constantes import WINDOW_HEIGHT, WINDOW_WIDTH, TITLE
import tkinter as tk

class MainLayout(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry(WINDOW_WIDTH + "x" + WINDOW_HEIGHT)
        self.title(TITLE)
        self.resizable(False, False)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        

        self.frames = {}
        pages = {HomePage: GamePage, GamePage: HomePage}

        # Add HomePage and GamePage to the layout
        for F in (HomePage, GamePage):
            
            frame = F(container, self, pages[F])

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

        # Create a dropdown menu for selecting the game mode
        self.game_mode_var = tk.StringVar(self)
        self.game_mode_var.set("Player vs Player")  # Default game mode
        game_mode_menu = tk.OptionMenu(self, self.game_mode_var,
                                       "Player vs Player", "Player vs AI",
                                       command=self.set_game_mode)
        game_mode_menu.pack()

        # Start the game when the application starts
        self.start_game()

    def show_frame(self, cont, difficulty=None):
        frame = self.frames[cont]
        if difficulty:
            frame.set_difficulty(difficulty)
            frame.color_choice()
        frame.tkraise()
        

    def set_game_mode(self, mode):
        # Set the game mode based on the selection from the dropdown menu
        print("Selected game mode:", mode)
        if mode == "Player vs Player":
            self.game_mode = "player_vs_player"
        elif mode == "Player vs AI":
            self.game_mode = "player_vs_naive_ai"
        else:
            raise ValueError("Unknown game mode selected")
        

    def start_game(self):
        # Start the game based on the selected game mode
        if hasattr(self, "game_mode"):
            if self.game_mode == "player_vs_player":
                pass
            elif self.game_mode == "player_vs_naive_ai":
                pass
            elif self.game_mode == "player_vs_minimax_ai":
                pass
            else:
                raise ValueError("Unknown game mode")
            


