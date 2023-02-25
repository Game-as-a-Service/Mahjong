import typing
from card import Card

# 玩家
# id 編號
# name 名稱
# isbanker 莊家否
# bankerCount 連莊（default=1)
# hand 手牌

# Player 抽牌 / 打牌


class Player:
    def __init__(self, id: int, name: str, is_banker: bool, banker_count: int) -> None:
        self.id = id
        self.name = name
        self.is_banker = is_banker
        self.banker_count = banker_count
        self.hand = []

    def draw_card(self, cards: Card):
        pass

    def remove_card(self, cards: Card):
        pass


if __name__ == "__main__":
    pass
