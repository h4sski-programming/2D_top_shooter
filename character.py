import pygame as pg
import math


from settings import *


class Character:
    def __init__(self, game, position, hp, speed, color, radius) -> None:
        self.game = game
        self.x, self.y = position
        self.hp = hp
        self.speed = speed
        self.color = color
        self.radius = radius
        
        self.dx, self.dy = (0, 0)
        self.angle = 0
        self.sin_a = math.sin(self.angle)
        self.cos_a = math.cos(self.angle)
        
    
    def update(self):
        self.sin_a = math.sin(self.angle)
        self.cos_a = math.cos(self.angle)
        self.check_events()
    
    
    def hit_wall(self, dx, dy):
        return (dy, dx) in self.game.map.map_dict
        
    
    def check_wall_colision(self, dx, dy):
        if not self.hit_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if not self.hit_wall(int(self.x), int(self.y + dy)):
            self.y += dy
    
    
    def draw(self):
        pg.draw.circle(self.game.screen, 'orange', 
                       self.position_on_map(self.position()), 
                       self.radius)
        
        
    def position(self):
        return self.x, self.y
    
    
    def position_on_map(self, position):
        return position[0] * self.game.map.cell_width, position[1] * self.game.map.cell_height