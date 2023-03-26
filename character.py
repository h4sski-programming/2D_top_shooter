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
        self.sin_a = math.sin(0)
        self.cos_a = math.cos(0)
        
    
    def update(self):
        self.check_events()
    
    
    def hit_wall(self, dx, dy):
        return self.game.map.is_wall(position_yx=(dy, dx))
        # return (dy, dx) in self.game.map.map_dict
        
    
    def check_wall_colision(self, dx, dy):
        if not self.hit_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if not self.hit_wall(int(self.x), int(self.y + dy)):
            self.y += dy
    
    
    def draw(self):
        for bullet in self.bullets_list:
            bullet.draw()
        # pg.draw.line(self.game.screen, 'white', 
        #              self.position_on_map(self.position()), 
        #              self.position_on_map(self.get_weapon_position()), 
        #              5)
        pg.draw.circle(self.game.screen, self.color, 
                       self.position_on_map(self.position()), 
                       self.radius)
        
        
    def position(self):
        return self.x, self.y
    
    
    def position_on_map(self, position):
        return position[0] * self.game.map.cell_width, position[1] * self.game.map.cell_height
    
    
    def convert_to_coordinates(self, pos_pixels):
        return pos_pixels[0] / self.game.map.cell_width, pos_pixels[1] / self.game.map.cell_height
    
    
    def get_hypotenuse(self, dx, dy):
        return math.sqrt(dx*dx + dy*dy)
    
    
    def get_distance_to(self, x, y):
        dx = x - self.x
        dy = y - self.y
        return math.sqrt(dx*dx + dy*dy)