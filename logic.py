import pygame
from assets import variables

file = open("./settings.txt", "a")

def generate_pieces(surface, mouse_pos, get_pieces, create_piece):

    if create_piece and variables.is_piece >= 3:
        
        if set_position(set_position_in_table(mouse_pos), get_pieces):
            get_pieces[variables.is_piece].position_in_table(set_position_in_table(mouse_pos))
        #check color
            variables.is_piece += 1
        create_piece = False
            
    if create_piece and variables.is_piece < 3:
        variables.is_piece += 1
        create_piece = False 
        
        surface.blit(get_pieces[0].get_circular_surface(), get_pieces[0].get_position_in_table())
        surface.blit(get_pieces[1].get_circular_surface(), get_pieces[1].get_position_in_table())
        surface.blit(get_pieces[2].get_circular_surface(), get_pieces[2].get_position_in_table())
        surface.blit(get_pieces[3].get_circular_surface(), get_pieces[3].get_position_in_table())
            
    if variables.is_piece >= 3:
        for piece in get_pieces:
            file.write(f"{piece.get_position_in_table()}\n")
            surface.blit(piece.get_circular_surface(), piece.get_position_in_table())
            
    
def set_position(position1, get_pieces):
    for piece in get_pieces[0 : variables.is_piece + 1]:
            #in x
        x_piece = variables.position.index(position1[0])
        x_reference = variables.position.index(piece.get_position_in_table()[0])
            
            #in y
        y_piece = variables.position.index(position1[1])
        y_reference = variables.position.index(piece.get_position_in_table()[1])
        
        if x_reference == x_piece:
            if (y_reference + 1 == y_piece) or (y_reference - 1 == y_piece):
                if not(piece.color == get_pieces[variables.is_piece + 1].color):
                    piece.is_color()
                    return True
        
        elif y_reference == y_piece:
            if (x_reference + 1 == x_piece) or (x_reference - 1 == x_piece):
                if not(piece.color == get_pieces[variables.is_piece + 1].color):
                    piece.is_color()
                    return True
            
        elif (x_reference + 1 == x_piece or x_reference - 1 == x_piece) and (y_reference + 1 == y_piece or y_reference - 1 == y_piece):
            if not(piece.color == get_pieces[variables.is_piece + 1].color):
                    piece.is_color()
                    return True

def set_position_in_table(mouse_pos):
    x, y =  mouse_pos 
    position = variables.position
        
    for i in range(len(position) - 1):
        if x in range(position[i], position[i + 1]):
            x = position[i]
                
    for j in range(len(position) - 1):
        if y in range(position[j], position[j + 1]):
            y = position[j]
                
    return (x, y)
        