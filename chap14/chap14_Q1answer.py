# 理解不能　自分のコードと出力全然違う、なぜShapeを継承したクラスを使ったのか。
#　おそらく、Shapeを継承したクラスだから、出力がメモリアドレス的なやつになるのかな...
#　合否判定不可

class Shape():
    def what_am_i(self):
        print("I am a shape.")


class Square(Shape):
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.s1 * 4

    def what_am_i(self):
        super().what_am_i()
        print("I am a Square.")


a_square = Square(29)
print(Square.square_list)
another_square = Square(93)
print(Square.square_list)