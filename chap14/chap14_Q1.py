"""
Squareクラスにsquare_listクラス変数を追加し、そして、新しいSquareクラスのオブジェクトが作られるたびに、そのオブジェクトをこのリストに追加しよう。
"""
class Square():
    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self.s1 * 4)

    def calculate_perimeter(self):
        return self.s1 * 4
    
    square_list = []


square1 = Square(29)
square2 = Square(93)


print(Square.square_list)