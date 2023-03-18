import pygame as pg
import random
import math

from settings import *
from character import Character
from bullet import Bullet


class Enemy(Character):
    def __init__(self, game, position, hp, speed, color, radius, agro_dist) -> None:
        super().__init__(game=game, position=position,
                       hp=hp, speed=speed,
                       color=color, radius=radius)
        self.weapon_lenght = 2      # 0.3
        self.bullets_list = []
        self.last_time_shoot = 0
        self.agro = False
        self.agro_distance = agro_dist
        self.alive = True
        
    
    def check_events(self):
        self.dx = 0
        self.dy = 0
        speed = self.speed * self.game.delta_time
        
        # moving
        if self.agro:
            # moving dx and dy values depended on speed
            dx = self.cos_a * speed
            dy = self.sin_a * speed
            self.check_wall_colision(dx, dy)
        
        # shooting
        # if keys[pg.K_SPACE]:
        #     if len(self.bullets_list) < PLAYER_BULLETS_NUMBER and \
        #         pg.time.get_ticks() - self.last_time_shoot >= PLAYER_FIRE_RATE:
        #         self.bullets_list.append(Bullet(self))
        #         self.last_time_shoot = pg.time.get_ticks()
    
    
    def collide_circle(self, position, radius):
        dx = position[0] - self.x
        dy = position[1] - self.y
        c = self.get_hypotenuse(dx, dy)
        if c <= self.radius + radius:
            return True
        return False
    
    def got_hit(self):
        self.hp -= 1
        print(f'Got hitted')
    
    
    def can_see_player(self):
        x = math.ceil(self.x)
        y = math.ceil(self.y)
        
    
    
    def update(self):
        super().update()
        
        if self.hp < 1:
            self.alive = False
        
        # for i, bullet in enumerate(self.bullets_list):
        #     if bullet.hit:
        #         self.bullets_list.pop(i)
        #     bullet.update()
        
        # dx and dy values towards player position
        dx = self.game.player.x - self.x
        dy = self.game.player.y - self.y
        c = self.get_hypotenuse(dx, dy)
        self.sin_a = dy / c
        self.cos_a = dx / c
        
        if c <= 4:
            self.agro = True
    
    
    def draw(self):
        # for bullet in self.bullets_list:
        #     bullet.draw()
        pg.draw.line(self.game.screen, self.color, 
                     self.position_on_map(self.position()), 
                     self.position_on_map(self.get_weapon_position()), 
                     5)
        super().draw()
    
    
    def get_weapon_position(self):
        weapon_x = self.x + self.cos_a * self.weapon_lenght
        weapon_y = self.y + self.sin_a * self.weapon_lenght
        return weapon_x, weapon_y


#######################################################


class Enemys:
    def __init__(self, game) -> None:
        self.game = game
        self.enemys_number = ENEMYS_NUMBER
        self.enemys_list = []
        self.spawns = {0: (8.5, 2.5),
                       1: (10.5, 10.5),
                       2: (18.5, 1.5),
                       3: (13.5, 1.5),
                       4: (19.5, 10.5),
                       5: (1.5, 10.5),
                       }
    
    def update(self):
        while len(self.enemys_list) <= self.enemys_number:
            rand_spawn = random.randint(0, len(self.spawns) - 1)
            self.enemys_list.append(Enemy_One(self.game, self.spawns[rand_spawn]))
        
        for i, enemy in enumerate(self.enemys_list):
            enemy.update()
            if not enemy.alive:
                self.enemys_list.pop(i)
    
    
    def draw(self):
        for enemy in self.enemys_list:
            enemy.draw()


#######################################################


class Enemy_One(Enemy):
    def __init__(self, game, position) -> None:
        super().__init__(game=game, position=position,
                       hp=3, speed=PLAYER_SPEED * 0.5,
                       color='blue', radius=10, agro_dist=4)


class Enemy_Two(Enemy):
    def __init__(self, game, position) -> None:
        super().__init__(game=game, position=position,
                       hp=8, speed=PLAYER_SPEED,
                       color='red', radius=10, agro_dist=6)