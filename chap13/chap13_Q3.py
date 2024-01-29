# Shapeクラスを定義し、呼ばれたら"I am a shape"を返す、メソッドwhat_am_iを定義する。
# 前のチャレンジで定義した、RectangleとSquareのクラスを変更し、Shapeクラスを継承させる
# 継承後RectangleとSquareオブジェクトを生成し、メソッドwhat_am_iを呼んでみる

class Shape:
    def __init__(self):
        pass

    def what_am_i(self):
        return "I am shape"
    
class Rectangle(Shape):
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def calculate_perimeter(self):
        return self.length *2 + self.width *2
    
class Square(Shape):
    pass

s_Rectangle = Rectangle(20,10)
print(s_Rectangle.what_am_i())

s_Square = Square()                        #SquareはShapeを継承しているから、引数が空カッコになる。なぜなら自分も引数を要求しておらず、親クラスのShapeは引数が実質ない(self)だから。
print(s_Square.what_am_i())