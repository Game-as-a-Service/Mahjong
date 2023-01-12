from models.Mahjong import Mahjong

one = Mahjong()


def test_decide_player_turn():
    assert one.decide_player_turn() is "turn"


def test_deal_tile():
    _card = one.deal_tile()
    assert _card.get_number() is 1


def test_record_wind():
    assert one.record_wind() is "current_wind"


def test_draw():
    assert one.draw() is False


#
# def test_player():
#     _player = one.get_winner()
#     assert _player.get_name() is "one player"
