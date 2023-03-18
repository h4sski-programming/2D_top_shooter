import pygame as pg

from settings import *


class Bullet:
    def __init__(self, player) -> None:
        self.player = player
        self.game = self.player.game
        
        self.x, self.y = self.player.get_weapon_position()
        self.hit = False
        
        self.angle = self.player.angle
        self.sin_a = self.player.sin_a
        self.cos_a = self.player.cos_a
        
    
    def update(self):
        dx = self.cos_a * (BULLET_SPEED * self.game.delta_time)
        dy = self.sin_a * (BULLET_SPEED * self.game.delta_time)
        
        self.check_wall_colision(dx, dy)
    
    
    def hit_wall(self, dx, dy):
        return (dy, dx) in self.game.map.map_dict
        
    
    def check_wall_colision(self, dx, dy):
        if not self.hit_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        else:
            self.hit = True
        if not self.hit_wall(int(self.x), int(self.y + dy)):
            self.y += dy
        else:
            self.hit = True
    
    
    def position(self):
        return self.x, self.y
    
    
    def draw(self):
        pg.draw.circle(self.game.screen, 'white', 
                       self.player.position_on_map((self.x, self.y)), BULLET_RADIUS)