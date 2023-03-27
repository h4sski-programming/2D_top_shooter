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
        self.weapon_lenght = 0.3
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
        if c <= self.radius / self.game.map.cell_width + radius:
            return True
        return False
    
    
    def got_hit(self):
        self.hp -= 1
    
    
    def can_see_player(self):
        x = math.floor(self.x)
        y = math.floor(self.y)
        
        # see diagram
        self.ctg_alpha = (self.dx) / (self.dy)
        
        # checking horizontal
        dx_local = self.dx / abs(self.dx)
        dy_local = 1 / self.ctg_alpha
        x_temp = self.x
        y_temp = self.y
        while self.get_distance_to(x=x_temp, y=y_temp) < self.get_distance_to(x=self.game.player.x, y=self.game.player.y):
            if self.game.map.is_wall(position_yx=(y_temp, x_temp)):
                return False
            else:
                x_temp += dx_local
                y_temp += dy_local
        return True
        
        
    
    def update_dx_dy(self):
        self.dx = self.game.player.x - self.x
        self.dy = self.game.player.y - self.y
    
    
    def update_sin_cos(self):
        c = self.get_hypotenuse(self.dx, self.dy)
        self.sin_a = self.dy / c
        self.cos_a = self.dx / c
    
    
    def update(self):
        super().update()
        
        if self.hp < 1:
            self.alive = False
        
        # for i, bullet in enumerate(self.bullets_list):
        #     if bullet.hit:
        #         self.bullets_list.pop(i)
        #     bullet.update()
        
        # dx and dy values towards player position
        self.update_dx_dy()
        self.update_sin_cos()
        
        if self.get_distance_to(x=self.game.player.x,
                                y=self.game.player.y) <= 4:
            # self.agro = True
            pass
        if not self.agro and self.can_see_player():
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
        self.generate_enemys_choise_list()
        print(self.enemys_choise_list)
    
    def update(self):
        while len(self.enemys_list) <= self.enemys_number:
            self.enemys_list.append(self.select_enemy())
        
        for i, enemy in enumerate(self.enemys_list):
            enemy.update()
            if not enemy.alive:
                self.enemys_list.pop(i)
    
    
    def generate_enemys_choise_list(self):
        self.enemys_choise_list = random.choices(population=[1, 2, 3],
                                                weights=[3, 2, 1],
                                                k=ENEMYS_NUMBER + 1)
        random.shuffle(self.enemys_choise_list)
        # print(self.enemys_choise_list)
        
    
    def select_enemy(self):
        if len(self.enemys_choise_list) < 1:
            self.generate_enemys_choise_list()
        chosen_enemy = self.enemys_choise_list.pop()
        # print(self.enemys_choise_list)
        if chosen_enemy == 1:
            return Enemy_One(self.game, self.get_spawn())
        if chosen_enemy == 2:
            return Enemy_Two(self.game, self.get_spawn())
        if chosen_enemy == 3:
            return Enemy_Tree(self.game, self.get_spawn())
    
    
    def get_spawn(self):
        while True:
            rand_x = random.randint(1, len(self.game.map.mini_map[0]) - 2)
            rand_y = random.randint(1, len(self.game.map.mini_map) - 2)
            distance_to_player = self.game.player.get_distance_to(x=rand_x, y=rand_y)
            
            if self.game.map.is_wall(position_yx=(rand_y, rand_x)) or \
                distance_to_player <= ENEMY_MIN_DISTANCE_TO_PLAYER:
                continue
            else:
                return (rand_x + 0.5, rand_y + 0.5)
    
    
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
                       hp=8, speed=PLAYER_SPEED * 0.8,
                       color='red', radius=10, agro_dist=6)


class Enemy_Tree(Enemy):
    def __init__(self, game, position) -> None:
        super().__init__(game=game, position=position,
                       hp=11, speed=PLAYER_SPEED * 0.3,
                       color='yellow', radius=10, agro_dist=8)

