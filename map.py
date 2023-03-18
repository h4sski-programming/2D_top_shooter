import pygame as pg
from math import ceil


from settings import *


_ = False

mini_map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
            [1, _, _, _, _, _, _, _, _, 1, _, _, 1, _, _, _, _, 1, _, _, _, 1], 
            [1, _, _, _, 1, _, _, _, _, 1, _, _, 1, _, _, _, _, 1, _, _, _, 1], 
            [1, _, _, _, 1, 1, 1, _, _, _, _, _, 1, _, _, _, _, _, _, 1, 1, 1], 
            [1, _, _, _, _, _, 1, _, _, _, _, 1, 1, 1, 1, 1, _, _, _, _, _, 1], 
            [1, 1, 1, 1, _, _, 1, _, 1, _, _, _, _, _, _, _, _, _, 1, _, _, 1], 
            [1, _, _, _, _, _, 1, _, 1, _, _, _, _, _, _, _, _, _, 1, _, _, 1], 
            [1, _, _, _, _, _, _, _, 1, _, 1, _, _, 1, 1, 1, 1, 1, 1, _, _, 1], 
            [1, _, _, _, 1, 1, 1, 1, 1, _, 1, 1, _, _, 1, _, _, _, _, _, 1, 1], 
            [1, 1, 1, _, _, 1, _, _, _, _, _, 1, _, _, 1, _, _, _, _, _, _, 1], 
            [1, _, _, _, _, 1, _, _, 1, _, _, 1, _, _, _, _, _, _, 1, _, _, 1], 
            [1, _, _, _, _, _, _, _, 1, _, _, _, _, 1, _, _, _, _, 1, _, _, 1], 
            [1, _, _, _, _, _, _, _, 1, _, _, _, _, 1, _, _, _, _, 1, _, _, 1], 
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
            ]

class Map:
    def __init__(self, game) -> None:
        self.game = game
        self.mini_map = mini_map
        self.cell_height = ceil(HEIGHT / len(self.mini_map))
        self.cell_width = ceil(WIDTH / len(self.mini_map[0]))
        self.map_dict = {}
        self.get_map()
        
    
    def get_map(self):
        for i, row in enumerate(self.mini_map):
            for j, value in enumerate(row):
                if value:
                    self.map_dict[(i, j)] = value
    
    
    def draw(self):
        for position in self.map_dict:
            pg.draw.rect(self.game.screen, 'darkgray', 
                         (position[1] * self.cell_width, 
                          position[0] * self.cell_height, 
                          self.cell_width, 
                          self.cell_height))
    
    
    