from random import shuffle

# このクラスはデッキ(カード一式となる52枚のトランプ)を表す
class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
            shuffle(self.cards)

    def remove_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()
    
#以下動作確認
"""
# Cardクラスと組み合わせないと、appendの横のCardが定義できないと思われ、動作確認できなかった
# Cardクラスの方に持って行ってやったらできた。

deck = Deck()
for card in deck.cards:
    print(card)

"""