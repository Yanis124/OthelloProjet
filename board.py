import pygame
from constants import *
from circle import *

class GridDrawer:
    def __init__(self, rows, cols, cell_size, screen_size, screen):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.screen_size = screen_size
        self.screen=screen
        self.current_color = CIRCLE_FIRST_COLOR
        self.list_circle=[]
        self.list_clickable_circle=[]
        self.list_available_circle=[] #list of list of circle that has not been drawn yet
        
            
    #initilise the grid
    def init_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.draw_rectangle_with_filling(row,col)
                self.draw_rectangle(row,col)
                color=None
                if((row==3 and col==3) or (row==3 and col==4) or (row==4 and col==3) or (row==4 and col==4)):
                    
                    color = CIRCLE_FIRST_COLOR if (row == 3 and col == 3) or (row == 4 and col == 4) else CIRCLE_SECOND_COLOR if (row == 3 and col == 4) or (row == 4 and col == 3) else None #select the right color
                    self.draw_circle(row,col,color)
                else:
                    self.list_available_circle.append(circle(row,col,color))
        self.get_clickable_circler()
        
    #draw a rectangle          
    def draw_rectangle(self,row,col):
        pygame.draw.rect(self.screen, SQUARE_BORDER, pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size), 1)
    
    def draw_rectangle_with_filling(self,row,col):
        pygame.draw.rect(self.screen, GRID_COLOR, pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size))
    
    #draw a filled circle            
    def draw_circle(self,row,col,color,added=True):
        center_square=(col * self.cell_size + self.cell_size//2,row * self.cell_size + self.cell_size//2)
        pygame.draw.circle(self.screen,color,center_square,self.cell_size//(2.2))
        pygame.display.flip()
        
        if added:
            for c in self.list_circle:
                if(c.row==row and c.col==col):
                    return
            self.list_circle.append(circle(row,col,color))
            
        else :
            for c in self.list_circle:
                if(c.row==row and c.col==col):
                    c.color=color
                    return
        
        
    #draw a potential circle
    def draw_potential_circle(self,row,col,color):
        center_square=(col * self.cell_size + self.cell_size//2,row * self.cell_size + self.cell_size//2)
        pygame.draw.circle(self.screen,color,center_square,self.cell_size//(2.2), width=2)
        
    
    #get the list of clickable circle
    def get_clickable_circler(self):
        self.list_clickable_circle=[]
        self.check_horizontal()
        self.check_vertical()
        self.check_diagonal()
        for c in self.list_clickable_circle:
            self.draw_potential_circle(c.row,c.col,c.color)
        
                    
    #get the list of clickable circle horizentaly           
    def check_horizontal(self):
        
        for potential_circle in self.list_available_circle:
            for c in self.list_circle:
                has_same_color_in_row = any(c.row == potential_circle.row and c.color == self.current_color for c in self.list_circle) # check if there is a circle with the same color in the same row
                
                if(c.row==potential_circle.row and c.col==potential_circle.col-1 and c.color!=self.current_color ): #check left
                    potential_circle.color=self.current_color
                    self.list_clickable_circle.append(potential_circle)
                elif(c.row==potential_circle.row and c.col==potential_circle.col+1 and c.color!=self.current_color ): #check right
                    potential_circle.color=self.current_color
                    self.list_clickable_circle.append(potential_circle)
                    
    #get the list of clickable circle vertically
    def check_vertical(self):
        
        for potential_circle in self.list_available_circle:
            for c in self.list_circle:
                has_same_color_in_row = any(c.col == potential_circle.col and c.color == self.current_color for c in self.list_circle) # check if there is a circle with the same color in the same col
                if(c.col==potential_circle.col and c.row==potential_circle.row-1 and c.color!=self.current_color and has_same_color_in_row): #check down
                    potential_circle.color=self.current_color
                    self.list_clickable_circle.append(potential_circle)
                elif(c.col==potential_circle.col and c.row==potential_circle.row+1 and c.color!=self.current_color and has_same_color_in_row): #check up
                    potential_circle.color=self.current_color
                    self.list_clickable_circle.append(potential_circle)
                    
    #get the list of clickable circle in the same diagonal   
    def check_diagonal(self):
        
        for potential_circle in self.list_available_circle:
            for c in self.list_circle:
                has_same_color_in_row = any((abs(c.col-potential_circle.col)-abs(c.row-potential_circle.row)==0) and c.color == self.current_color for c in self.list_circle) # check if there is a circle with the same color in the same diagonal
                
                if(c.col==potential_circle.col-1 and c.row==potential_circle.row-1 and c.color!=self.current_color and has_same_color_in_row): #check down
                    potential_circle.color=self.current_color
                    self.list_clickable_circle.append(potential_circle)
                    
                elif(c.col==potential_circle.col+1 and c.row==potential_circle.row+1 and c.color!=self.current_color and has_same_color_in_row): #check up
                    potential_circle.color=self.current_color
                    self.list_clickable_circle.append(potential_circle)
                    
                    
    def handle_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:  # Left mouse button click
            mouse_pos = event.pos
            x, y = mouse_pos
            row=y//self.cell_size
            col=x//self.cell_size
            for c in self.list_clickable_circle:
                if(c.row==row and c.col==col):
                    self.draw_circle(row,col,self.current_color)                    
                    list_between_circle=self.get_between_circle(c) #color the circle between the clicked circle and the other circle with the same color

                    
                    for colored_between_circle in list_between_circle: # change the color of the circles between the clicked circle and the other circle with the same color
                        self.draw_circle(colored_between_circle.row,colored_between_circle.col,self.current_color,added=False)
                    
                    
                    for available_circle in self.list_available_circle:     #remove the clicked circle from the list of available circle
                        if(available_circle.row==row and available_circle.col==col):
                            self.list_available_circle.remove(available_circle)
                            
                    for clickable_circle in self.list_clickable_circle:     #remove the clicked circle from the list of clickable circle
                        if(clickable_circle.row==row and clickable_circle.col==col):
                            self.list_clickable_circle.remove(clickable_circle)
                            
                    self.next_player_turn()
                    
    #get the list of circle that should change color after the player clicked     
    def get_between_circle(self,clicked_circle):
        list_between_circle=[]
        
        left=True #all circle are at the left of the clicked circle
        up=True #all circle are at the top of the clicked circle
        diagonal_up=True #all circle are at the top diagonal of the clicked circle
        
        for c in self.list_circle:
            if(c.row==clicked_circle.row and c.col-1==clicked_circle.col):
                left=False #there is a circle at the right of the clicked circle 
            if(c.col==clicked_circle.col and c.row-1==clicked_circle.row):
                up=False #there is something at the top of the circle
            if(c.row-1==clicked_circle.row and c.col!=clicked_circle.col):
                diagonal_up=False #there is something at the top diagonal of the circle
                
        if(left): list_between_circle+=self.get_between_circle_horizontal_left(clicked_circle)
        else: list_between_circle+=self.get_between_circle_horizontal_right(clicked_circle)
        
        if(up): list_between_circle+=self.get_between_circle_vertical_up(clicked_circle)
        else:  list_between_circle+=self.get_between_circle_vertical_down(clicked_circle)
        
        if(diagonal_up): list_between_circle+=self.get_between_circle_diagonal_up(clicked_circle)
        else:  list_between_circle+=self.get_between_circle_diagonal_down(clicked_circle)
        
        
        #list_between_circle+=self.get_between_circle_diagonal(clicked_circle)
        
        return list_between_circle
                    
    def get_between_circle_horizontal_left(self, clicked_circle):

        list_circle_condidate = []

        # Get the list of all circles in the same column
        sorted_circles = sorted(self.list_circle, key=lambda x: x.col)
        for c in sorted_circles:
            if c.row == clicked_circle.row and c.col != clicked_circle.col:
                list_circle_condidate.append(c)

        last_color_index = -1
        for i, c in enumerate(list_circle_condidate):
            if c.color == clicked_circle.color:
                last_color_index = i

        # Get the sublist starting from the last occurrence of the same color
        list_circle_between=list_circle_condidate[last_color_index+1:]
    
        return list_circle_between

    def get_between_circle_horizontal_right(self, clicked_circle):
        list_circle_condidate = []

        # Get the list of all circles in the same column
        sorted_circles = sorted(self.list_circle, key=lambda x: x.col)
        for c in sorted_circles:
            if c.row == clicked_circle.row and c.col != clicked_circle.col:
                list_circle_condidate.append(c)

        last_color_index = -1
        for i, c in enumerate(list_circle_condidate):
            if c.color == clicked_circle.color:
                last_color_index = i
                break
            

        # Get the sublist starting from the last occurrence of the same color
        list_circle_between=list_circle_condidate[:last_color_index+1]
        return list_circle_between
            
            
    def get_between_circle_vertical_up(self, clicked_circle):
        list_circle_condidate = []

        # Get the list of all circles in the same column
        sorted_circles = sorted(self.list_circle, key=lambda x: x.row)
        for c in sorted_circles:
            if c.col == clicked_circle.col and c.row != clicked_circle.row:
                list_circle_condidate.append(c)

        last_color_index = -1
        for i, c in enumerate(list_circle_condidate):
            if c.color == clicked_circle.color:
                last_color_index = i

        # Get the sublist starting from the last occurrence of the same color
        list_circle_between = list_circle_condidate[last_color_index+1:]

        return list_circle_between
    
    def get_between_circle_vertical_down(self, clicked_circle):
        list_circle_condidate = []

        # Get the list of all circles in the same column
        sorted_circles = sorted(self.list_circle, key=lambda x: x.row)
        for c in sorted_circles:
            if c.col == clicked_circle.col and c.row != clicked_circle.row:
                list_circle_condidate.append(c)

        last_color_index = -1
        for i, c in enumerate(list_circle_condidate):
            if c.color == clicked_circle.color:
                last_color_index = i
                break

        # Get the sublist starting from the last occurrence of the same color
        list_circle_between = list_circle_condidate[:last_color_index+1]

        return list_circle_between
    
    def get_between_circle_diagonal_up(self,clicked_circle):
        
        list_circle_condidate = []
        sorted_circles = sorted(self.list_circle, key=lambda x: (x.row, x.col))
        
        for c in sorted_circles:
            if (abs(c.col-clicked_circle.col)==(abs(c.row-clicked_circle.row))) and (c.row != clicked_circle.row and c.col != clicked_circle.col):
                list_circle_condidate.append(c)

        last_color_index = -1
        for i, c in enumerate(list_circle_condidate):
            if c.color == clicked_circle.color:
                last_color_index = i

        # Get the sublist starting from the last occurrence of the same color
        list_circle_between = list_circle_condidate[last_color_index+1:]

        return list_circle_between


    
    def get_between_circle_diagonal_down(self,clicked_circle):
        
        list_circle_condidate = []
        sorted_circles = sorted(self.list_circle, key=lambda x: (x.row, x.col))
        
        for c in sorted_circles:
            if (abs(c.col-clicked_circle.col)==(abs(c.row-clicked_circle.row))) and (c.row != clicked_circle.row and c.col != clicked_circle.col):
                list_circle_condidate.append(c)

        last_color_index = -1
        for i, c in enumerate(list_circle_condidate):
            if c.color == clicked_circle.color:
                last_color_index = i
                break

        # Get the sublist starting from the last occurrence of the same color
        list_circle_between = list_circle_condidate[:last_color_index+1]

        return list_circle_between
    
    #alternate between first and second player
    def next_player_turn(self):
        
        self.current_color = CIRCLE_FIRST_COLOR if self.current_color == CIRCLE_SECOND_COLOR else CIRCLE_SECOND_COLOR
        
        for c in self.list_clickable_circle:
            self.draw_rectangle_with_filling(c.row,c.col) #remove the clicked circle except the one that the player clicked
            self.draw_rectangle(c.row,c.col)
        pygame.display.flip()       
        
        self.get_clickable_circler()
                    
            
                        
                        
            
            
        
        
                    
    

                
                    
   

