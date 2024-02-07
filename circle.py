import pygame

class circle:
    def __init__(self,row,col,color):
        self.row=row
        self.col=col
        self.color=color
    
    def equals(self,other):
        return self.row==other.row and self.col==other.col and self.color==other.color
    
    def belong_to(self,list_circle):
        for i in list_circle:
            if(self.equals(i)):
                return True
            
    def display(self):
        print("row: ",self.row," col: ",self.col," color: ",self.color)
        
    def select_circle_same_row(self,list_circle):
        list_circle_same_row=[]
        for i in list_circle:
            if(i.row==self.row):
                list_circle_same_row.append(i)
        return list_circle_same_row
    