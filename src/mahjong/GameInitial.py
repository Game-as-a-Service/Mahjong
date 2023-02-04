# step1:初始化：
#    決定玩家：四位玩家姓名:p1,p2,p3,p4
#    決定莊家與各風位玩家>例 p1(E), p2(S), p4(W), p3(N)因此p1為莊
#    洗牌、決定目前排池順序
# step2:發牌
#    從莊開始，每人發四張牌直到每人16張，莊再拿一張
# step4:開始補花(摸牌加補牌)

# w1,w2,w3... 一萬,兩萬,三萬...
# d1,d2,d3... 一筒...
# s1,s2,s3..
# e,s,w,n,r,g,w 東南西北中(red)發(green)白(white)
# spring,summmer,autumn,winter,plum,orchid,chrysanthemum,bamboo 春夏秋冬梅蘭菊竹

# 牌池 = Array[牌]
# class 牌
# class 數序牌:
#     繼承 class牌
# class 花牌:
#     繼承 class牌
# class 字牌:
#     繼承 class牌

# s_w1
# b_p
# name rule


# 麻將屬性
#   每位玩家名字 [p1,p2,p3,p4]
#   牌池剩餘張數 default 144 (蓋著)
#   排池剩餘順序:[w1,w2,w3,w4,w5,w6,w7,.....] #管理員144排剩下哪些排 #存str/obj
#   東風位 p1 (w1,w2,w3,w4) ->16
#   南風位 p2
#   西風位 p4
#   北風位 p3
#   莊家 p1 +1張
# 玩家屬性
#   玩家手牌
class Mahjong:
    def __init__(self, p1, p2, p3, p4) -> None:
        self.player = [p1, p2, p3, p4]
        self.cards_remaining = 144
        self.cards_remaining_order = [w1, w2, w3, w4, w5, e, s, n]
        self.east_position = p1
        self.south_position = p2
        self.west_position = p4
        self.north_posit

    def draw_card(self):
        self.cards_remaining -= 1
        self.cards_remaining_order
        self.banker = p1
