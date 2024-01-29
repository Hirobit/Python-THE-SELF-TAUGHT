from random import shuffle

# このクラスは、トランプのカードを表す
class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]

    #インデックス操作とリストの数値を一致させる為、最初の２つの値はNoneになっている。　このアイディアのおかげでvalues[2]としたら"2"にアクセスすることができる
    values = [None, None,
              "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    
    def __init__(self, value, suit):
        """スーツもバリューも整数値です。"""
        self.value = value
        self.suit = suit

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.value:
                return True
            else:
                return False
        return False
    
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False
    
    def __repr__(self):
        value = self.values[self.value] + " of " + self.suits[self.suit]
        return value
    

#以下動作確認
"""ß
card1 = Card(10, 2)
card2 = Card(11, 3)
print(card1 < card2) #ダイアモンドの10 < クラブの11 はTrue


card1 = Card(10, 2)
card2 = Card(11, 3)
print(card1 > card2) #ダイアモンドの10 > クラブの11 はFalse

card = Card(3, 2)
print(card)         #__repr__を呼び出し、クラスオブジェクトの引数(ここだと3,2)に対応した、カードの数値とスート（カードのマーク）をクラス変数から取得してきている

"""

#以下Deckクラスの動作確認
"""
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

deck = Deck()
for card in deck.cards:
    print(card)
"""