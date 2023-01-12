class Mock_Card:
    def __init__(self, num):
        self.number = num

    def get_number(self):
        return self.number


class Mock_Player:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Mahjong:
    def __init__(self):
        self.discord_tile = Mock_Card(1)
        self.winner = Mock_Player("one player")

    def decide_player_turn(self):
        return "turn"

    def deal_tile(self):
        return self.discord_tile

    def record_wind(self):
        return "current_wind"

    def draw(self):
        return False

    def get_winner(self):
        return self.winner
