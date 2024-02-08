import pygame
from src.constants import CIRCLE_FIRST_COLOR, CIRCLE_SECOND_COLOR, GRID_COLOR, SQUARE_BORDER_COLOR
from src.grid.circle import *

class Grid:
    """ Grid class represente the game board"""
    
    def __init__(self, rows, cols, cell_size, screen_size, screen):
        """initialize the object Grid"""
        
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.screen_size = screen_size
        self.screen = screen
        self.current_color = CIRCLE_FIRST_COLOR
        self.list_circle=[] #list of circle in grid
        self.list_clickable_circle=[] # list of circle that the user can click
        self.list_available_circle=[] #list of circle that has not been taken yet
        self.init_grid()

        
            
    
    def init_grid(self):
        """draw the grid and the initial circles in the grid"""
        
        for row in range(self.rows):
            for col in range(self.cols):
                self.draw_rectangle_with_filling(row, col)
                self.draw_rectangle(row, col)
                color = None
                if((row == 3 and col == 3) or (row == 3 and col == 4) or (row == 4 and col == 3) or (row == 4 and col == 4)):
                    
                    color = CIRCLE_FIRST_COLOR if (row == 3 and col == 3) or (row == 4 and col == 4) else CIRCLE_SECOND_COLOR if (row == 3 and col == 4) or (row == 4 and col == 3) else None #select the right color
                    self.draw_circle(row, col, color)
                else:
                    self.list_available_circle.append(circle(row, col, None))
        self.get_clickable_circler()
             
    def draw_rectangle(self, row, col):
        """daraw the border of a rectangle in the grid"""
        
        pygame.draw.rect(self.screen, SQUARE_BORDER_COLOR, pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size), 1)
    
    def draw_rectangle_with_filling(self, row, col):
        """daraw the inside of a rectangle in the grid"""
        
        pygame.draw.rect(self.screen, GRID_COLOR, pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size))
                
    def draw_circle(self, row, col, color):
        """draw a circle in the grid at the given row and col with the given color"""
        
        center_square=self.get_center_circle(row, col)
        pygame.draw.circle(self.screen, color, center_square, self.cell_size // 2.2)
        pygame.display.flip()
        
        for c in self.list_circle:
            if(c.row == row and c.col == col):
                return
        
        self.list_circle.append(circle(row, col, color))
            
    def draw_potential_circle(self, row, col, color):
        """draw a potential circle in the grid at the given row and col with the given color"""
        
        center_square=self.get_center_circle(row, col)
        pygame.draw.circle(self.screen, color, center_square, self.cell_size // 2.2, width = 2)
        
    def get_center_circle(self, row, col):
        """return the center of the circle at the given row and col"""
        
        return (col * self.cell_size + self.cell_size // 2, row * self.cell_size + self.cell_size // 2)
    
    def change_color_circle(self, row, col, color):
        """change the color of the circle at the given row and col"""
        
        for c in self.list_circle:
            if(c.row == row and c.col == col):
                c.color = color
                self.draw_circle(row, col, color)
                return
        
    def get_clickable_circler(self):
        """get the list of circle that the user can click"""
        
        self.list_clickable_circle = []
        self.check_horizontal()
        self.check_vertical()
        self.check_diagonal()
        for c in self.list_clickable_circle:
            self.draw_potential_circle(c.row, c.col, c.color)
                 
    def check_horizontal(self):
        """
        Get clickable circles horizontally.

        Identifies circles that can be clicked based on the current color 
        and the presence of circles of the same color in the same row.
        """
        
        for potential_circle in self.list_available_circle:
            has_same_color_in_row = any(c.row == potential_circle.row and c.color == self.current_color and c.col != potential_circle.col for c in self.list_circle) # check if there is a circle with the same color in the same row
            
            if not has_same_color_in_row:
                continue  # No circles with the same color in the same row, skip
                
             # Check left
            left_circle = next((c for c in self.list_circle if c.row == potential_circle.row and c.col == potential_circle.col - 1), None)
            if left_circle and left_circle.color != self.current_color:
                clickable_circle = circle(potential_circle.row, potential_circle.col, self.current_color)
                self.list_clickable_circle.append(clickable_circle)

            # Check right
            right_circle = next((c for c in self.list_circle if c.row == potential_circle.row and c.col == potential_circle.col + 1), None)
            if right_circle and right_circle.color != self.current_color:
                clickable_circle=circle(potential_circle.row, potential_circle.col, self.current_color)
                self.list_clickable_circle.append(clickable_circle)
                    
    def check_vertical(self):
        """
        Finds clickable circles vertically.

        Identifies circles that can be clicked based on the current color 
        and the presence of circles of the same color in the same column.
        """
        for potential_circle in self.list_available_circle:
            # Check if there's a circle of the same color in the same column
            has_same_color_in_col = any(c.col == potential_circle.col and c.color == self.current_color for c in self.list_circle)
            if not has_same_color_in_col:
                continue  # No circles with the same color in the same column, skip

            # Check above
            above_circle = next((c for c in self.list_circle if c.col == potential_circle.col and c.row == potential_circle.row - 1), None)
            if above_circle and above_circle.color != self.current_color:
                clickable_circle = circle(potential_circle.row, potential_circle.col, self.current_color)
                self.list_clickable_circle.append(clickable_circle)

            # Check below
            below_circle = next((c for c in self.list_circle if c.col == potential_circle.col and c.row == potential_circle.row + 1), None)
            if below_circle and below_circle.color != self.current_color:
                clickable_circle = circle(potential_circle.row, potential_circle.col, self.current_color)
                self.list_clickable_circle.append(clickable_circle)

                     
    def check_diagonal(self):
        """
        Finds clickable circles diagonally.

        Identifies circles that can be clicked based on the current color 
        and the presence of circles on the same diagonal.
        """
        for potential_circle in self.list_available_circle:
            # Check if there's a circle of the same color diagonally
            has_same_color_diagonal_ul = any(c.color == self.current_color and c.row - potential_circle.row == c.col - potential_circle.col for c in self.list_circle )
            has_same_color_diagonal_ur = any(c.color == self.current_color and c.row - potential_circle.row == potential_circle.col - c.col for c in self.list_circle )
            has_same_color_diagonal_ll = any(c.color == self.current_color and potential_circle.row - c.row == c.col - potential_circle.col for c in self.list_circle )
            has_same_color_diagonal_lr = any(c.color == self.current_color and potential_circle.row - c.row == potential_circle.col - c.col for c in self.list_circle )
            
            if (not has_same_color_diagonal_ul) and (not has_same_color_diagonal_ur) and (not has_same_color_diagonal_ll) and ( not has_same_color_diagonal_lr):
                continue
            
            # Check upper-left diagonal
            ul_diagonal_circle = next((c for c in self.list_circle if c.row == potential_circle.row - 1 and c.col == potential_circle.col - 1), None)
            if(ul_diagonal_circle):
                if has_same_color_diagonal_ul and ul_diagonal_circle.color != self.current_color:
                    clickable_circle = circle(potential_circle.row, potential_circle.col, self.current_color)
                    self.list_clickable_circle.append(clickable_circle)

            # Check upper-right diagonal
            ur_diagonal_circle = next((c for c in self.list_circle if c.row == potential_circle.row - 1 and c.col == potential_circle.col + 1), None)
            if(ur_diagonal_circle):
                if has_same_color_diagonal_ur and ur_diagonal_circle.color != self.current_color:
                    clickable_circle=circle(potential_circle.row, potential_circle.col, self.current_color)
                    self.list_clickable_circle.append(clickable_circle)

            # Check lower-left diagonal
            ll_diagonal_circle = next((c for c in self.list_circle if c.row == potential_circle.row + 1 and c.col == potential_circle.col - 1 ), None)
            if(ll_diagonal_circle):
                if has_same_color_diagonal_ll and ll_diagonal_circle.color != self.current_color:
                    clickable_circle = circle(potential_circle.row,potential_circle.col, self.current_color)
                    self.list_clickable_circle.append(clickable_circle)

            # Check lower-right diagonal
            lr_diagonal_circle = next((c for c in self.list_circle if c.row == potential_circle.row + 1 and c.col == potential_circle.col + 1), None)
            if(lr_diagonal_circle):
                if has_same_color_diagonal_lr and lr_diagonal_circle.color != self.current_color:
                    clickable_circle = circle(potential_circle.row, potential_circle.col, self.current_color)
                    self.list_clickable_circle.append(clickable_circle)
                    
                    
    def handle_click(self, event):
        """handle the click event when the user click on a clickable_circle""" 
        
        if event.type == pygame.MOUSEBUTTONDOWN:  # Left mouse button click
            x, y = event.pos
            row = y // self.cell_size
            col = x // self.cell_size
            clicked_circle = circle(row, col, self.current_color)
            
            for c in self.list_clickable_circle:
                if (c.row == clicked_circle.row and c.col == clicked_circle.col and c.color == clicked_circle.color):
            
                    self.draw_circle(row, col, self.current_color)                    
                    list_between_circle = self.get_between_circle(clicked_circle) 

                    for colored_between_circle in list_between_circle:    #change the color of the circle between the clicked circle and another circle with the same color
                        self.change_color_circle(colored_between_circle.row, colored_between_circle.col, self.current_color)
                    
                    for available_circle in self.list_available_circle:     #remove the clicked circle from the list of available circle
                        if(available_circle.row == row and available_circle.col == col):
                            self.list_available_circle.remove(available_circle)
                            
                    for clickable_circle in self.list_clickable_circle:     #remove the clicked circle from the list of clickable circle
                        if(clickable_circle.row == row and clickable_circle.col == col):
                            self.list_clickable_circle.remove(clickable_circle)
                            
                    self.next_player_turn()
                    
                    
    #get the list of circle that should change color after the player clicked     
    def get_between_circle(self, clicked_circle):
        list_between_circle = []
        
        direction_horizental = "left" #all circle are at the left of the clicked circle
        direction_vertical = "up" #all circle are at the top of the clicked circle
        direction_diagonal = "up" #all circle are at the top diagonal of the clicked circle
        
        for c in self.list_circle:
            if(c.row == clicked_circle.row and c.col-1 == clicked_circle.col):
                direction_horizental = "right" #there is a circle at the right of the clicked circle 
            if(c.col == clicked_circle.col and c.row-1 == clicked_circle.row):
                direction_vertical = "down" #there is something at the top of the circle
            if(c.row-1 == clicked_circle.row and c.col != clicked_circle.col):
                direction_diagonal = "down" #there is something at the top diagonal of the circle
                
        list_between_circle += self.get_between_circle_horizontal(clicked_circle, direction_horizental)
        list_between_circle += self.get_between_circle_vertical(clicked_circle, direction_vertical)
        list_between_circle += self.get_between_circle_diagonal(clicked_circle, direction_diagonal)
                
        return list_between_circle
                    
    def get_between_circle_horizontal(self, clicked_circle, direction):
        

        list_circle_condidate = []

        # Get the list of all circles in the same column
        sorted_circles = sorted(self.list_circle, key=lambda x: x.col)
        for c in sorted_circles:
            if c.row == clicked_circle.row and c.col != clicked_circle.col:
                list_circle_condidate.append(c)

        last_color_index = -1
        
        if(direction == "left"):
            for i, c in enumerate(list_circle_condidate):
                if c.color == clicked_circle.color:
                    last_color_index = i

            if(last_color_index == -1): return []
            return list_circle_condidate[last_color_index+1:]
        
        else:
            for i, c in enumerate(list_circle_condidate):
                if c.color == clicked_circle.color:
                    last_color_index = i
                    break
            if(last_color_index == -1): return []
            return list_circle_condidate[:last_color_index+1]
            
    def get_between_circle_vertical(self, clicked_circle, direction):
        """
        Finds circles vertically that are located between circles of opposit color.

        Args:
            clicked_circle (Circle): The clicked circle.
            direction (str): The direction ('up' or 'down') to search for circles diagonally.

        Returns:
            list: The list of circles found vertically that their color should change.
        """
        list_circle_condidate = []

        # Get the list of all circles in the same column
        sorted_circles = sorted(self.list_circle, key=lambda x: x.row)
        for c in sorted_circles:
            if c.col == clicked_circle.col and c.row != clicked_circle.row:
                list_circle_condidate.append(c)
            
        last_color_index = -1    
        if(direction == "up"):
            
            for i, c in enumerate(list_circle_condidate):
                if c.color == clicked_circle.color:
                    last_color_index = i
                    
            if(last_color_index ==-1): return []
            return list_circle_condidate[last_color_index + 1:]
        
        else :
            for i, c in enumerate(list_circle_condidate):
                if c.color == clicked_circle.color:
                    last_color_index = i
                    break
            if(last_color_index == -1): return []
            return list_circle_condidate[:last_color_index + 1]
                
    def get_between_circle_diagonal(self, clicked_circle, direction):
        """
        Finds circles diagonally that are located between circles of opposit color.

        Args:
            clicked_circle (Circle): The clicked circle.
            direction (str): The direction ('up' or 'down') to search for circles diagonally.

        Returns:
            list: The list of circles found diagonally that their color should change.
        """
        list_circle_condidate = []
        sorted_circles = sorted(self.list_circle, key = lambda x: (x.row, x.col))
        
        for c in sorted_circles:
            if (abs(c.col-clicked_circle.col) == (abs(c.row-clicked_circle.row))) and (c.row != clicked_circle.row and c.col != clicked_circle.col):
                list_circle_condidate.append(c)
        
        last_color_index = -1
            
        if(direction == "up"):
            for i, c in enumerate(list_circle_condidate):
                if c.color == clicked_circle.color:
                    last_color_index = i
            if(last_color_index == -1): return []
            return list_circle_condidate[last_color_index + 1:]
                    
        else :
            for i, c in enumerate(list_circle_condidate):
                if c.color == clicked_circle.color:
                    last_color_index = i
                    break
            if(last_color_index == -1): return []
            return list_circle_condidate[:last_color_index + 1]

    def next_player_turn(self):
        """alternate turns to the other player"""
        
        self.current_color = CIRCLE_FIRST_COLOR if self.current_color == CIRCLE_SECOND_COLOR else CIRCLE_SECOND_COLOR
        
        for c in self.list_clickable_circle:
            self.draw_rectangle_with_filling(c.row, c.col) #remove the clicked circle except the one that the player clicked
            self.draw_rectangle(c.row, c.col)
        pygame.display.flip()       
        
        self.get_clickable_circler() #get the list of circle that the user can click
        
                    
            
                        
                        
            
            
        
        
                    
    

                
                    
   

