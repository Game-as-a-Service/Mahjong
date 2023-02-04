from enum import Enum
import typing


class Card:
    def __init__(self, type: "CardType") -> None:
        self.type = type


class CardType(Enum):
    SUITS = "Suits"  # 字牌(萬筒條)
    HONORS = "Honors"  # 字牌(風牌+三元牌)
    BONUS = "Bonus"  # 花牌


class Suits:
    def __init__(self, suitsType: str, number: int) -> None:
        self.suitsType = suitsType
        self.number = number


class SuitType(Enum):
    WAN = "Wan"  # 萬
    DOT = "Dot"  # 筒
    STICK = "Stick"  # 條
