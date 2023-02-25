from typing import List
from card import Card
import mahjong

# 麻將類別要做的事情：
# step1:初始化四位玩家:p1,p2,p3,p4 決定莊家與位置>例 p1(E)(莊), p2(S), p4(W), p3(N)因此p1為莊
# step2:初始化144張牌
# step2:發牌：從莊開始，每人發四張牌直到每人16張，莊再拿一張
# step3:開始補花(摸牌加補牌)


class Mahjong:
    def __init__(self) -> None:
        # self.player = player_list
        self.cards_remaining = 144
        self.stack = None
        # 莊家
        self.banker = None
        # 東風位的玩家名稱
        self.east_position = None
        # 南風位的玩家名稱
        self.south_position = None
        # 西風位的玩家名稱
        self.west_position = None
        # 北風位的玩家名稱
        self.north_position = None

    def player_init(self, player_list):
        self.banker = player_list[0]
        self.east_position = player_list[0]
        self.south_position = player_list[1]
        self.west_position = player_list[2]
        self.north_position = player_list[3]

    def start_card_init(self):
        self.stack = Card.card_initial().random()

    # 從 stack 裡面 index 開始發牌
    def draw_init(self, index):
        pass
