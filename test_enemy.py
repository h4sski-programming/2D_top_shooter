from game import Game
from settings import *
from enemy import Enemy_One, Enemys, Enemy_Two, Enemy_Tree

g = Game()
e_all = Enemys(g)
e_one = Enemy_One(game=g, position=(1.5, 1.5))
e_two = Enemy_Two(game=g, position=(2.5, 1.5))
e_tree = Enemy_Tree(game=g, position=(3.5, 1.5))


def test_generate_enemys_choise_list():
    assert len(e_all.enemys_choise_list) == ENEMYS_NUMBER + 1


def test_got_hit():
    start_hp = e_one.hp
    e_one.got_hit()
    assert  start_hp == e_one.hp + 1
    

def test_select_enemy():
    e_all.enemys_choise_list = [1, 1, 1]
    assert type(e_all.select_enemy()) == type(e_one)
    assert len(e_all.enemys_choise_list) == 2
    
    e_all.enemys_choise_list = [2, 2, 2]
    assert type(e_all.select_enemy()) == type(e_two)
    assert len(e_all.enemys_choise_list) == 2
    
    e_all.enemys_choise_list = [3, 3, 3]
    assert type(e_all.select_enemy()) == type(e_tree)
    assert len(e_all.enemys_choise_list) == 2