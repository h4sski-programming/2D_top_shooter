import pygame as pg
import math

from settings import *
from character import Character
from bullet import Bullet


class Player(Character):
    def __init__(self, game) -> None:
        super().__init__(game=game, position=PLAYER_INITIAL_POSITION,
                       hp=PLAYER_HP, speed=PLAYER_SPEED,
                       color='orange', radius=10)
        self.weapon_lenght = 0.4
        self.bullets_list = []
        self.last_time_shoot = 0
        
    
    def check_events(self):
        self.dx = 0
        self.dy = 0
        speed = self.speed * self.game.delta_time
        
        keys = pg.key.get_pressed()
        mouse = pg.mouse
        
        # moving
        if keys[pg.K_w]:
            self.dy += -speed
        if keys[pg.K_s]:
            self.dy += speed
        if keys[pg.K_a]:
            self.dx += -speed
        if keys[pg.K_d]:
            self.dx += speed
        self.check_wall_colision(self.dx, self.dy)
        
        # turning with keys
        # if keys[pg.K_LEFT]:
        #     self.angle -= PLAYER_ROTATION_SPEED * self.game.delta_time
        # if keys[pg.K_RIGHT]:
        #     self.angle += PLAYER_ROTATION_SPEED * self.game.delta_time

        # turning with mouse
        mouse_position = self.convert_to_coordinates(mouse.get_pos())
        mouse_dx = mouse_position[0] - self.x
        mouse_dy = mouse_position[1] - self.y
        c = math.sqrt(mouse_dx * mouse_dx + mouse_dy * mouse_dy)
        self.sin_a = mouse_dy / c
        self.cos_a = mouse_dx / c
        
        # shooting
        if keys[pg.K_SPACE] or mouse.get_pressed()[0]:
            if len(self.bullets_list) < PLAYER_BULLETS_NUMBER and \
                pg.time.get_ticks() - self.last_time_shoot >= PLAYER_FIRE_RATE:
                self.bullets_list.append(Bullet(self))
                self.last_time_shoot = pg.time.get_ticks()
        
        
    
    def update(self):
        super().update()
        
        for i, bullet in enumerate(self.bullets_list):
            if bullet.hit:
                self.bullets_list.pop(i)
            if self.bullet_hit_enemy(bullet):
                self.bullets_list.pop(i)
            bullet.update()
    
    
    def bullet_hit_enemy(self, bullet):
        for enemy in self.game.enemys.enemys_list:
            if enemy.collide_circle(bullet.position(), 0.1):
                enemy.got_hit()
                return True
        return False
    
    
    def draw(self):
        # for bullet in self.bullets_list:
        #     bullet.draw()
        pg.draw.line(self.game.screen, 'white', 
                     self.position_on_map(self.position()), 
                     self.position_on_map(self.get_weapon_position()), 
                     5)
        super().draw()
    
    
    def get_weapon_position(self):
        weapon_x = self.x + self.cos_a * self.weapon_lenght
        weapon_y = self.y + self.sin_a * self.weapon_lenght
        return weapon_x, weapon_y
    
    