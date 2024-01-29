# このクラスはプレイヤーを表す。プレイヤーの名前、持っているカード、ゲームに何回勝ったかという情報をもつ

class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name