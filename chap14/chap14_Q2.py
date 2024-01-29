"""
Squareクラスのオブジェクトをprint関数に渡したら、4辺それぞれの長さを出力しよう。
例えば、square(29)のようにオブジェクトを作ったら、print関数では 29 by 29 by 29 by 29 と出力しよう。
"""
class Square():
    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append((self.s1))

    def calculate_perimeter(self):
        return self.s1 * 4
    
    square_list = []


#square1 = Square(10)
#square2 = Square(20)
#square3 = Square(30)
square29 = Square(29)

#print(Square.square_list)

a_side = Square.square_list 
print(f"{a_side} by {a_side} by {a_side} by {a_side}")