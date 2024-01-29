# RectangleとSquareクラスを作る。両方のクラスに、その図形の外周の長さを計算して返す calculate_perimeterメソッドを定義して、
# RectangleとSquareのオブジェクトを作ってそれぞれのcalculate_perimeterメソッドを呼び出してみる。(Rectang=長方形、Square=四角)

class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def calculate_perimeter(self):
        return self.length *2 + self.width *2
    
class Square(Rectangle):
    pass

a_Rectangle  = Rectangle(25,50)
print(a_Rectangle.calculate_perimeter())

a_Square = Square(20,20)
print(a_Square.calculate_perimeter())