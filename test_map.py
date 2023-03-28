from game import Game
from map import Map

g = Game()
map = Map(g)


def test_is_wall():
    assert map.is_wall(position_yx=(0, 0)) == True
    assert map.is_wall(position_yx=(1, 1)) == False
    assert map.is_wall(position_yx=(2, 4)) == True
    assert map.is_wall(position_yx=(11, 20)) == False
    assert map.is_wall(position_yx=(11, 21)) == True
    assert map.is_wall(position_yx=(12, 20)) == True
    
    assert map.is_wall(position_yx=(-1, 0)) == False
    assert map.is_wall(position_yx=(0, -1)) == False
    assert map.is_wall(position_yx=(-1, -1)) == False