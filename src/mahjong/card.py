import itertools
from enum import Enum
import typing
from typing import List

"""
序數牌 (各4張)
0X01 - 0X09 1萬~9萬
0X01 - 0X19 1筒-9筒
0X01 - 0X29 1條-9條
字牌：東西南北中發白 (各4張)
0x31,0x32,0x33,0x34,0x35,0x36,0x37
花牌：春夏秋冬梅蘭菊竹
0x41,0x42,0x43,0x44,0x45,0x46,0x47,0x48
# 共144張
"""


class Card:
    def __init__(self) -> None:
        self.card_pool = []

    def card_initial(self) -> List:
        string = "0X"
        # 序數牌
        for num, i in itertools.product(range(0, 3), range(1, 10)):
            card_string = f"{string}{num}{i}"
            self.card_pool.extend([card_string] * 4)
            # self.card_pool.append(card_string)
        # 字牌
        for i in range(1, 8):
            card_string = f"{string}3{i}"
            # self.card_pool.append(card_string)
            self.card_pool.extend([card_string] * 4)
        # 花牌
        for i in range(1, 9):
            card_string = f"{string}4{i}"
            self.card_pool.append(card_string)
        return self.card_pool


if __name__ == "__main__":
    card = Card()
    stack = card.card_initial()
    print(len(stack))

    # class Card:
    #     def __init__(self, type: "CardType") -> None:
    #         self.type = type

    # class CardType(Enum):
    #     SUITS = "Suits"  # 字牌(萬筒條)
    #     HONORS = "Honors"  # 字牌(風牌+三元牌)
    #     BONUS = "Bonus"  # 花牌

    # class Suits:
    #     def __init__(self, suitsType: str, number: int) -> None:
    #         self.suitsType = suitsType
    #         self.number = number

    # class SuitType(Enum):
    #     WAN = "Wan"  # 萬
    #     DOT = "Dot"  # 筒
    #     STICK = "Stick"  # 條
