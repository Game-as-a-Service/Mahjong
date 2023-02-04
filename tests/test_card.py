import unittest
import sys

# sys.path.append('../src/..')
# sys.path.append('src')
# sys.path.append('src/mahjong')
# print(sys.path)


class TestCard(unittest.TestCase):
    # def setUp(self):
    #     card = Card()

    def test_card(self):
        from mahjong.card import Suits
        from mahjong.card import Card

        card = Card(Suits("Wan", 1))
        assert card.type.number == 1


if __name__ == "__main__":
    # sys.path.append('../src/..')
    # sys.path.append('src')
    # sys.path.append('src/mahjong')
    print(sys.path)
    unittest.main()
