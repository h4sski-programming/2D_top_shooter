from game import Game
from character import Character


g = Game()
c = Character(game=g, position=(1.5, 1.5), hp=2, speed=2,
              color='orange', radius=10)


def test_character_type():
    assert type(c) == Character

    
def test_check_wall_colision():
    c.check_wall_colision(-1, -1)
    assert c.hit_wall(c.x, c.y) == True
    

def test_get_distance_to():
    assert c.get_distance_to(x=3.5, y=1.5) == 2
    assert c.get_distance_to(x=1.5, y=3.5) == 2
    assert c.get_distance_to(x=3.5, y=3.5) != 2