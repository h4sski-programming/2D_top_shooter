import pygame as pg
import sys

from settings import *
from map import Map
from player import Player
from enemy import Enemys


class Game:
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()
    
    
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.enemys = Enemys(self)
        # ppp = self.enemys.get_spawn()
        # print(ppp, self.map.is_wall(ppp))
    
    
    def update(self):
        pg.display.flip()
        self.delta_time =  self.clock.tick(FPS)
        pg.display.set_caption(f'2D TOP SHOOTER - fps:{self.clock.get_fps() :.1f}')
        
        self.player.update()
        self.enemys.update()
    
    
    def draw(self):
        self.screen.fill('black')
        self.map.draw()
        self.player.draw()
        self.enemys.draw()
    
    
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
    
    
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
    
    
if __name__ == '__main__':
    g = Game()
    g.run()

