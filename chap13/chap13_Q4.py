# HorseクラスとRiderクラスを定義し、コンポジションを使って、馬(Horse)に騎手(Rider)を持たせる。

class Horse:
    def __init__(self, owner):
        self.owner = owner
    

class Rider:
    def __init__(self, zara):
        self.zara = zara

rider = Rider("アスラン・ザラ乗る。")
horse = Horse(rider)

print(horse.owner.zara)