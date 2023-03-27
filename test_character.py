from game import Game
from character import Character


g = Game()
c = Character(game=g, position=(1.5, 1.5), hp=2, speed=2,
              color='orange', radius=10)


def test_character_type():
    assert type(c) == Character

    
def test_check_wall_colision():
    start_x, start_y = c.x, c.y
    c.check_wall_colision(-1, -1)
    assert start_x == c.x
    assert start_y == c.y
    
    c.check_wall_colision(1, 0)
    assert c.x == start_x + 1
    c.x = 1.5
    
    c.check_wall_colision(0, 1)
    assert c.y == start_y + 1
    c.y = 1.5
    

def test_position():
    c.x, c.y = 1.5, 1.5
    position = c.position()
    assert position[0] == 1.5
    assert position[1] == 1.5
    
    c.x, c.y = -1.1, -1.2
    position = c.position()
    assert position[0] == -1.1
    assert position[1] == -1.2
    

def test_get_distance_to():
    c.x, c.y = 1.5, 1.5
    assert c.get_distance_to(x=3.5, y=1.5) == 2
    assert c.get_distance_to(x=1.5, y=3.5) == 2
    assert c.get_distance_to(x=3.5, y=3.5) != 2
    
    
    
    
    
    