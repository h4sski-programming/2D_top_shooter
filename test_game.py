from game import Game

def test_new_game():
    g = Game()
    g.new_game()
    assert g.map
    assert g.player
    assert g.enemys