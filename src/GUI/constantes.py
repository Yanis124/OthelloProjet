#general constants for the GUI
WINDOW_HEIGHT = "1000"
WINDOW_WIDTH = "600"
TITLE = "Othello"

#pages constantes
PAGE_BG_COLOR = "#2c3e50"
TITLE_TEXT_FONT = ("Arial", 25)
BUTTON_TEXT_FONT = ("Arial", 14)
GAMEPAGE_BUTTON_BG_COLOR = "#34495e"
BUTTON_STYLE = {
            'font': BUTTON_TEXT_FONT,
            'background': GAMEPAGE_BUTTON_BG_COLOR,  
            'foreground': "white",    
            'borderwidth': 3,         
            'relief': "ridge",        
            'width': 15,              
            'height': 2,              
            'bd': 0,                  
            'highlightthickness': 0,  
            'highlightbackground': "#34495e" 
        }
HOMEPAGE_BUTTON_BG_COLOR = "#4CAF50"


#canvas constants
BORDER_COLOR = "#000000"
GRID_COLOR = "#20C997"
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 800
CIRCLE_RADIUS = ((CANVAS_WIDTH / 8) / 2 )
NUMBER_CIRCLE_SIZE = 40
BLACK_CIRCLE_X_CORDINATE = (CANVAS_WIDTH / 8) * 2
WHITE_CIRCLE_X_CORDINATE = (CANVAS_WIDTH / 8) * 6
SQUARE_SIZE = CANVAS_WIDTH / 8

