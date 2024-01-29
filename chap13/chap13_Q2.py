# Squareクラスにchange_sizeメソッドを定義して、そこに渡した数値の分だけSquareの横幅を増やしたり、減らしたり（マイナス値の場合）してみる。P169

class Square:
    def __init__(self, w, l):
        self.width = w
        self.length = l
    
    def change_size(self, new):
        self.new = new
        print(f"幅＝{self.width + self.new}, 長さ＝{self.length}")

a_Square = Square(100,100)
a_Square.change_size(200)
a_Square.change_size(-20)