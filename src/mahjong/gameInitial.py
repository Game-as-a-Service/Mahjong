# step1:先輸入四位玩家:p1,p2,p3,p4
# step2:決定莊家與位置>例 p1(E), p2(S), p4(W), p3(N)因此p1為莊
# 麻將屬性
#   每位玩家名字
#   牌池剩餘張數
#   東風位
#   南風位
#   西風位
#   北風位
# 玩家屬性
#   玩家手牌
# step3:從莊開始，每人發四張牌直到每人16張，莊再拿一張
# step4:開始補花(摸牌加補牌)

# w1,w2,w3... 一萬,兩萬,三萬...
# d1,d2,d3... 一筒...
# s1,s2,s3..
# e,s,w,n,r,g,w 東南西北中(red)發(green)白(white)
# spring,summmer,autumn,winter,plum,orchid,chrysanthemum,bamboo 春夏秋冬梅蘭菊竹


class Mahjong:
    def __init__(self, p1, p2, p3, p4) -> None:
        self.player = [p1, p2, p3, p4]
        self.cards_remaining = 144
        self.east_position = p1
        self.south_position = p2
