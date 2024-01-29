"""
自分のコードは、what i amメソッドからreturnで, I am shaoeが返り値として戻ってくる。 Squareクラスは中身がpassで空、ただshapeを継承しているだけなので不正解と言われても反論できない
Q1のSquareクラスはRectangleを継承していたからそっちは正解。
答えのコードはメソッド内にprint関数を持っているので後からprintで囲わなくてもいい、出力は同じだがSquareクラスが引っかかるので40点というところ、
この問題の本質である、継承して親クラスのメソッドを使うは自分のコードでもできている。
"""

class Shape():
    def what_am_i(self):
        print("I am a shape.")


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2


class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

a_rectangle = Rectangle(20, 50)
a_square = Square(29)

a_rectangle.what_am_i()
a_square.what_am_i()