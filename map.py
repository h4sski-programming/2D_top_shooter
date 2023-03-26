import pygame as pg
from math import ceil


from settings import *


_ = False

mini_map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],     # 0
            [1, _, _, _, _, _, _, _, _, 1, _, _, 1, _, _, _, _, 1, _, _, _, 1],     # 1
            [1, _, _, _, 1, _, _, _, _, 1, _, _, 1, _, _, _, _, 1, _, _, _, 1],     # 2
            [1, _, _, _, 1, 1, 1, _, _, _, _, _, 1, _, _, _, _, _, _, 1, 1, 1],     # 3
            [1, _, _, _, _, _, 1, _, _, _, _, 1, 1, 1, 1, 1, _, _, _, _, _, 1],     # 4
            [1, 1, 1, 1, _, _, 1, _, 1, _, _, _, _, _, _, _, _, _, 1, _, _, 1],     # 5
            [1, _, _, _, _, _, 1, _, 1, _, _, _, _, _, _, _, _, _, 1, _, _, 1],     # 6           [1, _, _, _, _, _, _, _, 1, _, 1, _, _, 1, 1, 1, 1, 1, 1, _, _, 1],     # 8
            [1, _, _, _, 1, 1, 1, 1, 1, _, 1, 1, _, _, 1, _, _, _, _, _, 1, 1],     # 7
            [1, 1, 1, _, _, 1, _, _, _, _, _, 1, _, _, 1, _, _, _, _, _, _, 1],     # 8
            [1, _, _, _, _, 1, _, _, 1, _, _, 1, _, _, _, _, _, _, 1, _, _, 1],     # 9
            [1, _, _, _, _, _, _, _, 1, _, _, _, _, 1, _, _, _, _, 1, _, _, 1],     # 10
            [1, _, _, _, _, _, _, _, 1, _, _, _, _, 1, _, _, _, _, 1, _, _, 1],     # 11
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],     # 12
            ]
        #    0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 

class Map:
    def __init__(self, game) -> None:
        self.game = game
        self.mini_map = mini_map
        self.cell_height = ceil(HEIGHT / len(self.mini_map))
        self.cell_width = ceil(WIDTH / len(self.mini_map[0]))
        self.map_dict = {}
        self.get_map()
        
    
    def get_map(self):
        for y, row in enumerate(self.mini_map):
            for x, value in enumerate(row):
                if value:
                    self.map_dict[(y, x)] = value
    
    
    def is_wall(self, position_yx):
        # if False:
        if self.map_dict.get(position_yx) == 1:
            return True
        else:
            return False
    
    
    def draw(self):
        for position in self.map_dict:
            pg.draw.rect(self.game.screen, 'darkgray', 
                         (position[1] * self.cell_width, 
                          position[0] * self.cell_height, 
                          self.cell_width, 
                          self.cell_height))
    
    
    