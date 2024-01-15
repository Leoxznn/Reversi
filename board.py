#File to store the board of the game and its options

import pygame
from assets import variables
from pieces import Piece

#Create the grid
class Grid:
    def __init__(self):
        #define the dimension of the square
        self.size = variables.SIZE[0] / 8
        #loops over horizontaly in 12
        self.piece = Piece(variables.BLACK)
    
    def build(self, surface):
        for i in range(12):
            pygame.draw.line(surface, variables.WHITE, start_pos=(0, i * self.size), end_pos=(variables.SIZE[0], i * self.size), width=5)
            #loops over verticaly in 12
            for j in range(12):
                pygame.draw.line(surface, variables.WHITE, start_pos=(j * self.size, 0), end_pos=(j * self.size, variables.SIZE[1]), width=5)
        surface.blit(self.piece.get_circular_surface(60), (15, 15))
        pygame.display.update()
        
    def position_pieces()