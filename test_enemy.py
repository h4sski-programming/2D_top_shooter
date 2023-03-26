from game import Game
from enemy import Enemy_One

g = Game()
enem = Enemy_One(game=g, position=(1.5, 1.5))

def test_enemy_in_wall():
    pass